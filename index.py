import re

nomeRegex = {
    "inicio":[r"^🏫IFSULDEMINAS$",r"^(?:🏫|$)(?:I|$)(?:F|$)(?:S|$)(?:U|$)(?:L|$)(?:D|$)(?:E|$)(?:M|$)(?:I|$)(?:N|$)(?:A|$)(?:S|$)$"],
    "fim":[r"^🏫$",r"^🏫$"],
    "var":[r"^[a-z]+[a-z_0-9]*$",r"^([a-z]|$)+([a-z_0-9]|$)*$"],
    "tipoVar":[r"^(int|real|string|bool)$",r"^(((i|$)(n|$)(t|$))|((r|$)(e|$)(a|$)(l|$))|((s|$)(t|$)(r|$)(i|$)(n|$)(g|$))|((b|$)(o|$)(o|$)(l|$)))$"],
    "opRela":[r"^(🐘|🐁|🐘🟰|🐁🟰|🟰🟰|❗🟰)$",r"^(🐘|🐁|🐘🟰|🐁🟰|🟰🟰|❗🟰)$"],
    "opMat":[r"^✖️|➖|➗|➕$",r"^✖️|➖|➗|➕$"],
    "opAtrib":[r"^🟰$",r"^🟰$"],
    "opLog":[r"^✌️|🤞$",r"^✌️|🤞$"],
    "if":[r"^🔛$",r"^🔛$"],
    "else":[r"^🔚$",r"^🔚$"],
    "elseif":[r"^🔚🔛$",r"^🔚🔛$"],
    "while":[r"^🔄$",r"^🔄$"],
    "function":[r"^🌍$",r"^🌍$"],
    "booleans":[r"^✅|❗$",r"^✅|❗$"],
    "texto":[r"^\"[^\"]*\"$",r"^(\"|$)([^\"]|$)*(\"|$)$"],
    "inteiro":[r"^-?\d+$",r"^(-|$)?(\d|$)+$"],
    "real":[r"/^-?\d+\.\d+$/",r"/^-?\d+\.\d+$/"],
    "abreParenteses":[r"^➡️$",r"^(➡️|➡)$"],
    "fechaParenteses":[r"^⬅️$",r"^(⬅️|⬅)$"],
    "comentarios":[r"/^#️⃣.*#️⃣$/",r"/^#️⃣.*#️⃣$/"],
    "virgula":[r"^⏬$",r"^⏬$"],
    "break":[r"^❌$",r"^❌$"],
    "print":[r"^🎤$",r"^🎤$"],
    "input":[r"^❔$",r"^❔$"]
}

def printaSaida(saida):
    global saida2
    for i in saida:
        print("Token:<",i[0],",",i[1],"> Linha: ",i[2]," - Coluna ",i[3]," -")
        saida2+="Token:"+i[0]+","+i[1]+" Linha: "+str(i[2])+" - Coluna "+str(i[3])+" <br/>"


def testa(texto):
    fullMatch = []
    possibleMatch = []
    for x, y in nomeRegex.items():
        
        m = re.search(y[0], texto)
        if m != None:
            fullMatch.append([m,x])

        m = re.search(y[1], texto)
        if m != None:
            possibleMatch.append(m)
        #print('function')
        #print(texto)
        #print(x)
        #print(re.search(y[0], texto))
        #print(re.search(y[1], texto))
    
    return fullMatch,possibleMatch

def validaTudo(fm,pm):
    global saida
    global buffer
    global previousMatch
    global currentError
    global linha
    global char
    if len(fm)==0 and len(pm)==0:
        #print('sem saida')
        if len(previousMatch)>0:
            #print("previousMatch",previousMatch)
            #print("lastMatch",previousMatch[-1])
            saida.append([previousMatch[-1][0].group(),previousMatch[-1][1],linha,char-len(previousMatch[-1][0].group())])
            #print("saida",saida)
            buffer = buffer[previousMatch[-1][0].span()[1]:]
            #print("buffer after match",buffer)
            previousMatch = []
            if buffer == " ":
                buffer = ""
            if buffer != "":
                #print("gambi ",buffer)
                fm,pm = testa(buffer)
                if(len(fm)!=0 or len(pm)!=0):
                    validaTudo(fm,pm)
            
        else:
            currentError+=buffer
            buffer = ''
            #print('currentError ',currentError)
    else:
        if len(currentError)>0:
            saida.append([currentError,'erro',linha,char])
            currentError = ""
        for x in fm:
            previousMatch.append(x)
        #print(previousMatch)
    #asd = input()
    return


def lexer(macumba):

    global saida
    global saida2
    global buffer
    global previousMatch
    global currentError
    global linha
    global char

    saida = []
    saida2 = ""
    buffer = ""
    previousMatch = []
    currentError = ""
    linha = 0
    char = 0

    for i in range(len(macumba)):
        char+=1
        #print(buffer)
        buffer=buffer+macumba[i]
        if(buffer == "\n"):
            linha+=1
            char=0
            buffer = ""
            continue
        if(buffer == " "):
            buffer = ""
            continue
        fm,pm = testa(buffer)
        print(linha," ",char)
        #print('main')
        validaTudo(fm,pm)

    if(buffer!=""):
        fm,pm = testa(buffer)
        
        print('macumba fim')
        validaTudo(fm,pm)
    
    if(buffer!=""):
        saida.append([buffer,'erro',linha,char])

    print(saida)
    printaSaida(saida)
    return saida2

entrada = "🏫IFSULDEMINAS \n\
int idade 🟰 ❔➡️\"Insira sua idade\"⬅️ \n\
🔛➡️idade🐘🟰18⬅️➡️ \n\
🎤➡️\"Maior de idade\"⬅️ \n\
⬅️🔚➡️ \n\
🎤➡️\"Menor de idade\"⬅️ \n\
⬅️ \n\
🏫 2.a3 \n"

lexer(entrada)