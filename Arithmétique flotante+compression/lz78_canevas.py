#fichier = open(germinal.txt", "r")
#texte = fichier.read()
#fichier.close()
texte = "ABRABADABRA"

def compression(texte):
    sortie = []
    dic = {'': 0}
    cpt = 1
    mot = ""
    for lettre in texte:
        mot += lettre
        if mot not in dic.keys():
            dic[mot] = cpt
            cpt += 1
            sortie.append((dic[mot[:-1]], lettre))
            mot = ""
    sortie.append((0, mot))
    return sortie
    
           
def decompression(code):
    sortie = ''
    liDic = ['']
    texte = ""
    cpt = 0
    for num, lettre in code:
        texte = liDic[num] + lettre
        liDic.append(texte)
        sortie += texte
    return sortie


def ecritureFichier(code nomFichier):
    with open(nomFichier, "w", encoding="utf-8") as f:
        for nb, lettre in code:
            if lettre == "\n":
                lettre = "\n"
            f.write(lettre+str(nb))


print(compression(texte))
print(decompression(compression(texte)))
#code=compression(germinal)
#decode=decompression(code)


#print(decode[0:1000])

#print("Longueur de germinal :",len(germinal))
#print("Longueur de la version compressee  :", len(code))
