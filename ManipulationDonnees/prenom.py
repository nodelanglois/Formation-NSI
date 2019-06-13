import matplotlib.pyplot as pl
# christophe node-langlois

"""
Créer un dictionnaire contenant les prénoms et en valeurs des dictionnaires contennant année et occurence

Négliger les xxxx
"""

enfants = []
garcons = {}
filles = {}
# Question 1

with open('nat2017_court.txt', 'r', encoding="utf-8") as f:
    lignes = f.read().splitlines()
#print(lignes[:10])

enfants = [ligne.split('\t') for ligne in lignes[1:]]

#print(enfants[:10])   
for enfant in enfants:
    if enfant[0] == '1':
        if enfant[1] not in garcons.keys():
            if enfant[2] != 'XXXX':
                garcons[enfant[1]]={int(enfant[2]):int(enfant[3])}
        else :
            if enfant[2] != 'XXXX':
                garcons[enfant[1]][int(enfant[2])] = int(enfant[3])

    elif enfant[0] == '2':
        if enfant[1] not in filles.keys():
            if enfant[2] != 'XXXX':
                filles[enfant[1]]={int(enfant[2]):int(enfant[3])}
        else :
            if enfant[2] != 'XXXX':
                filles[enfant[1]][int(enfant[2])] = int(enfant[3])


#print(garcons['ADAM'])

def populaire(dic,debut,fin):
    listePopu = []
    for prenom in dic.keys():
        Nombre = 0
        for annee in range(debut,fin+1):
            if annee in dic[prenom].keys():
                Nombre += dic[prenom][annee]
        listePopu.append((prenom,Nombre))
    return sorted(listePopu, key=lambda listePopu : listePopu[1] , reverse=True)
    

print(populaire(garcons, 1900, 2017))
"""
liste = [1,2,3]
print(liste)
dico = {}

dico["A"]=liste[0]

print(dico)
"""
