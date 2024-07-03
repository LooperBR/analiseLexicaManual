import re

nomeRegex = {
    "inicio":[r"🏫IFSULDEMINAS",r"(?:🏫|$)(?:I|$)(?:F|$)(?:S|$)(?:U|$)(?:L|$)(?:D|$)(?:E|$)(?:M|$)(?:I|$)(?:N|$)(?:A|$)(?:S|$)"],
    "fim":r"🏫",
    "tipoVar":r"int|real|string|bool",
    "var":r"/^[a-z]+[a-z_0-9]*$/i",
    "opRela":r"🐘|🐁|🐘🟰|🐁🟰|🟰🟰|❗🟰",
    "opMat":r"✖️|➖|➗|➕ ",
    "opAtrib":r"🟰",
    "opLog":r"✌️|🤞",
    "if":r"🔛",
    "else":r"🔚",
    "elseif":r"🔚🔛",
    "while":r"🔄",
    "function":r"🌍",
    "booleans":r"✅|❗",
    "texto":r"/^\".*\"$/",
    "inteiro":r"/^-?\d+$/",
    "real":r"/^-?\d+\.\d+$/",
    "abreParenteses":r"➡️",
    "fechaParenteses":r"⬅️",
    "comentarios":r"/^#️⃣.*#️⃣$/",
    "virgula":r"⏬",
    "break":r"❌",
    "print":r"🎤",
    "input":r"❔"
}


def testa(texto):
    print("fudeu")
    regex = "^🏫$"
    
    return re.search(regex, texto)

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

for i in range(len(macumba)):
    macumbaLinha = ""

    print(buffer)
    if(buffer==""):
        buffer=macumba[i]
    else:
        macumbaLinha=buffer+macumba[i]
        if(testa(macumbaLinha)):
            buffer=macumbaLinha
        else:
            if(testa(buffer)):
                print("nice")
                saida.append((buffer,"correto","teste"))
                buffer=macumba[i]
            else:
                print("fudeu")
                saida.append((buffer,"errado","teste"))
                buffer=macumba[i]
    asd = input()

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