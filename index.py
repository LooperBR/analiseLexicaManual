import re

nomeRegex = {
    "inicio":[r"^🏫IFSULDEMINAS$",r"^(?:🏫|$)(?:I|$)(?:F|$)(?:S|$)(?:U|$)(?:L|$)(?:D|$)(?:E|$)(?:M|$)(?:I|$)(?:N|$)(?:A|$)(?:S|$)$"],
    "fim":[r"^🏫$",r"^🏫$"],
    "tipoVar":[r"^(int|real|string|bool)$",r"^(((i|$)(n|$)(t|$))|((r|$)(e|$)(a|$)(l|$))|((s|$)(t|$)(r|$)(i|$)(n|$)(g|$))|((b|$)(o|$)(o|$)(l|$)))$"],
    "var":[r"^[a-z]+[a-z_0-9]*$",r"^[a-z]+[a-z_0-9]*$"],
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
    for i in saida:
        print(i[0]," ",i[1])


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
        print('function')
        print(texto)
        print(x)
        print(re.search(y[0], texto))
        print(re.search(y[1], texto))
    
    return fullMatch,possibleMatch

def validaTudo(fm,pm):
    global saida
    global buffer
    global previousMatch
    global currentError
    if len(fm)==0 and len(pm)==0:
        print('sem saida')
        if len(previousMatch)>0:
            print("previousMatch",previousMatch)
            print("lastMatch",previousMatch[-1])
            saida.append([previousMatch[-1][0].group(),previousMatch[-1][1]])
            print("saida",saida)
            buffer = buffer[previousMatch[-1][0].span()[1]:]
            print("buffer after match",buffer)
            previousMatch = []
            if buffer == " ":
                buffer = ""
            if buffer != "":
                print("gambi ",buffer)
                fm,pm = testa(buffer)
                if(len(fm)!=0 or len(pm)!=0):
                    validaTudo(fm,pm)
            
        else:
            currentError+=buffer
            buffer = ''
            print('currentError ',currentError)
    else:
        if len(currentError)>0:
            saida.append([currentError,'erro'])
            currentError = ""
        for x in fm:
            previousMatch.append(x)
        print(previousMatch)
    #asd = input()
    return

macumba = "🏫IFSULDEMINAS \
int idade 🟰 ❔➡️\"Insira sua idade\"⬅️ \
🔛➡️idade🐘🟰18⬅️➡️ \
🎤➡️\"Maior de idade\"⬅️ \
⬅️🔚➡️ \
🎤➡️\"Menor de idade\"⬅️ \
⬅️ \
🏫 "


saida = []
buffer = ""
previousMatch = []
currentError = ""

for i in range(len(macumba)):

    print(buffer)
    buffer=buffer+macumba[i]
    fm,pm = testa(buffer)
    
    print('main')
    validaTudo(fm,pm)
    # if len(fm)==0 and len(pm)==0:
    #     print('sem saida')
    #     if len(previousMatch)>0:
    #         print("previousMatch",previousMatch)
    #         print("lastMatch",previousMatch[-1])
    #         saida.append([previousMatch[-1][0].group(),previousMatch[-1][1]])
    #         print("saida",saida)
    #         buffer = buffer[previousMatch[-1][0].span()[1]:]+macumba[i]
    #         if buffer == " ":
    #             buffer = ""
    #         print("buffer after match",buffer)
    #         previousMatch = []
    #     else:
    #         currentError+=macumbaLinha
    #         buffer = ''
    #         print('currentError ',currentError)
    # else:
    #     if len(currentError)>0:
    #         saida.append([currentError,'erro'])
    #         currentError = ""
    #     for x in fm:
    #         previousMatch.append(x)
    #     print(previousMatch)
    #     buffer=macumbaLinha
    #asd = input()

if(buffer!=""):
    fm,pm = testa(buffer)
    
    print('macumba fim')
    validaTudo(fm,pm)

print(saida)
printaSaida(saida)