#import codecs  # Utile pour spécifier l'encodage à l'ouverture
import matplotlib.pyplot as pl

#Programme travaillant sur le fichier
#des etablissements de l'education nationale
#disponible ici :
# https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/

#Lecture d'une table
Etablissements = []
with open('fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre.csv', "r", encoding ="utf-8") as f:
#with codecs.open('fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre.csv',"r","utf-8") as f:
    lignes = f.read().splitlines()
    print(lignes[:4])
    entete = lignes[0].split(';')
    for ligne in lignes[1:]:
        champs = ligne.split(";")
        d={}
        for i in range (len(entete)):
            d[entete[i]]=champs[i]
        Etablissements.append(d)

# Remarque :
# for ligne in f:
# -> ligne contient le caractère de fin de 
# ligne \n (et eventuellement \r)
# lignes = f.read().splitlines()
# for ligne in lignes :
# -> ligne ne contient pas le caractère de 
# fin de ligne.
# Ce serait plus "propre" de supprimer ce caractère.

##


#Filtrage d'une table

EtablissementsVersailles=[x for x in Etablissements if (x['Académie']=='Versailles')]
EtablissementsCergy=[x for x in Etablissements if (x['Académie']=='Versailles' and x['Commune'] == 'Cergy')]
EtablissementsMetropole = [x for x in Etablissements if (x['Code département']!= '' and int(x['Code département'])<100)]


#Tri de la table

EtablissementsVersaillesTries = sorted(EtablissementsVersailles, key = lambda etab:etab['Nature'])

# Ecriture dans un fichier de la table
def ecriture(table,nomFichier):
    with open(nomFichier, "w", encoding='utf-8') as f :
        entete = ""
        for x in table[0].keys() :
            #on sépare chaque champ avec un ;
            entete+=x+";"
        # on n'écrit pas le dernier ; 
        # de fin de ligne inutile
        f.write(entete[:-1]+'\n')
        for etab in table :
            ligne = ""
            for champ in etab.values():
                ligne+=champ+";"
            f.write(ligne[:-1]+'\n')
            
            
#Exemple d'utilisation
def affichePoints(listeEtab):
    latitudes = [float(x['Latitude']) for x in listeEtab if x['Latitude']!='']
    
    longitudes = [float(x['Longitude']) for x in listeEtab  if x['Longitude']!='']
    #Affichage en nuage de points
    pl.plot(longitudes,latitudes,'bo')
    pl.show()
    
#affichePoints(EtablissementsVersailles)
affichePoints(EtablissementsMetropole)
#affichePoints(Etablissements)

#ecriture(EtablissementsVersailles,"etablissementsVersailles.csv")
