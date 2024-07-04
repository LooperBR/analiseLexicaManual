import re

nomeRegex = {
    "inicio":[r"^🏫IFSULDEMINAS$",r"^(?:🏫|$)(?:I|$)(?:F|$)(?:S|$)(?:U|$)(?:L|$)(?:D|$)(?:E|$)(?:M|$)(?:I|$)(?:N|$)(?:A|$)(?:S|$)$"],
    "fim":[r"^🏫$",r"^🏫$"],
    "tipoVar":[r"^int|real|string|bool$",r"^(((i|$)(n|$)(t|$))|((r|$)(e|$)(a|$)(l|$))|((s|$)(t|$)(r|$)(i|$)(n|$)(g|$))|((b|$)(o|$)(o|$)(l|$)))$"],
    "var":[r"/^[a-z]+[a-z_0-9]*$/i",r"/^[a-z]+[a-z_0-9]*$/i"],
    "opRela":[r"^🐘|🐁|🐘🟰|🐁🟰|🟰🟰|❗🟰$",r"^🐘|🐁|🐘🟰|🐁🟰|🟰🟰|❗🟰$"],
    "opMat":[r"^✖️|➖|➗|➕$",r"^✖️|➖|➗|➕$"],
    "opAtrib":[r"^🟰$",r"^🟰$"],
    "opLog":[r"^✌️|🤞$",r"^✌️|🤞$"],
    "if":[r"^🔛$",r"^🔛$"],
    "else":[r"^🔚$",r"^🔚$"],
    "elseif":[r"^🔚🔛$",r"^🔚🔛$"],
    "while":[r"^🔄$",r"^🔄$"],
    "function":[r"^🌍$",r"^🌍$"],
    "booleans":[r"^✅|❗$",r"^✅|❗$"],
    "texto":[r"/^\".*\"$/",r"/^\".*\"$/"],
    "inteiro":[r"/^-?\d+$/",r"/^-?\d+$/"],
    "real":[r"/^-?\d+\.\d+$/",r"/^-?\d+\.\d+$/"],
    "abreParenteses":[r"^➡️$",r"^➡️$"],
    "fechaParenteses":[r"^⬅️$",r"^⬅️$"],
    "comentarios":[r"/^#️⃣.*#️⃣$/",r"/^#️⃣.*#️⃣$/"],
    "virgula":[r"^⏬$",r"^⏬$"],
    "break":[r"^❌$",r"^❌$"],
    "print":[r"^🎤$",r"^🎤$"],
    "input":[r"^❔$",r"^❔$"]
}


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

macumba = "🏫IFSULDEMINAS \
int idade 🟰 ❔➡️“Insira sua idade”⬅️ \
🔛➡️idade🐘🟰18⬅️➡️ \
🎤➡️“Maior de idade”⬅️ \
⬅️🔚➡️ \
🎤➡️“Menor de idade”⬅️ \
⬅️ \
🏫 "

saida = []
buffer = ""
previousMatch = []
currentError = ""

for i in range(len(macumba)):
    macumbaLinha = ""

    print(buffer)
    macumbaLinha=buffer+macumba[i]
    fm,pm = testa(macumbaLinha)
    
    print('main')
    
    if len(fm)==0 and len(pm)==0:
        print('sem saida')
        if len(previousMatch)>0:
            print(previousMatch)
            print(previousMatch[-1])
            saida.append([previousMatch[-1][0].group(),previousMatch[-1][1]])
            print(saida)
            print(buffer[previousMatch[-1][0].span()[1]:])
            buffer = buffer[previousMatch[-1][0].span()[1]:]
            previousMatch = []
        else:
            currentError+=macumbaLinha
            buffer = ''
            print('currentError ',currentError)
    else:
        if len(currentError)>0:
            saida.append([currentError,'erro'])
        for x in fm:
            previousMatch.append(x)
        print(previousMatch)
        buffer=macumbaLinha
    # if(testa(macumbaLinha)):
    #     buffer=macumbaLinha
    # else:
    #     if(testa(buffer)):
    #         print("nice")
    #         saida.append((buffer,"correto","teste"))
    #         buffer=macumba[i]
    #     else:
    #         print("fudeu")
    #         saida.append((buffer,"errado","teste"))
    #         buffer=macumba[i]
    #asd = input()

if(buffer!=""):
    if(testa(buffer)):
        print("nice")
        saida.append(buffer)
        buffer=""
    else:
        print("fudeu")
        saida.append(buffer)
        buffer=""

print(saida)