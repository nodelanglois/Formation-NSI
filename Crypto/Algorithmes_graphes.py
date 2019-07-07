# Les graphes vont êtres représentés par un couple (S, A) ou un triplet (S, A, P)
# avec S qui est un itérable sur les sommets,
# par exemple S = 'ABCDE' pour des sommets qui sont des lettres
# ou S = ['France', 'Espagne', 'Italie', 'Belgique']
# lorsque les sommets ont des noms plus compliqués.
# Si besoin, on peut transformer S en liste ou en ensemble,
#  avec list(S) ou set(S)
# A est également un itérable sur les arêtes, éventuellement orientées
# exemple 1 : graphe non orienté :
#         A = [ {'A', 'B'}, {'B', 'C'} ]
# exemple 2 : graphe orienté :
#         A =  [ ('A', 'B'), ('B', 'C') ]
# P est la pondération, dans l'ordre des arêtes

# Exemple

S = 'ABCDES'
A = [ {'E', 'A'}, {'E', 'B'}, {'A', 'B'}, {'A', 'D'}, {'B', 'C'}, {'A', 'C'}, {'C', 'D'},\
       {'C', 'S'}, {'D', 'S'}, {'B', 'D'}]
P = [     3     ,     2     ,     3     ,     2     ,     5     ,     3     ,     2     ,\
           2    ,      2,          4]
G = (S, A, P)

def sommets(G):
    return G[0]

def aretes(G):
    return G[1]
    
def poids(a, G):
    j = aretes(G).index(a)
    return G[2][j]
    
def degre(sommet, G):
    if not(sommet in sommets(G)):
        print('Ce sommet n est pas dans le graphe')
        return -1 #erreur
    degre = 0
    for a in aretes(G):
        if sommet in a:
            degre += 1
    return degre

def voisins(sommet, G):
    return [s for s in sommets(G) if {sommet, s} in aretes(G)]

def Dijkstra(dep, arr, G):
    infinity = 1e100  # on y est presque ...
    L = [(0, dep, None)] #sommets à traiter (distance à l'origine, sommet, source)
    for s in sommets(G):
        if s != dep:
            L.append((infinity, s, None))
    fini = [] #sommets traités
    while L != []:
        dist, som, prov = L[0]
        fini.append(L[0])
        L = L[1:]
        for s in voisins(som, G):
            a = {s, som}
            p = poids(a, G) 
            for i in range(len(L)):
                (d1, s1, s2) = L[i]
                if s1 == s:
                    if dist + p < d1:
                        L[i] = (dist + p, s, som)
                    break
        L.sort()
    return fini
                
def WP(G):
    nb_couleur = 0
    L = [(degre(s, G), s) for s in sommets(G)]
    L.sort()
    L = [s for (d, s) in L] #on ne garde que les sommets
    coloriage = dict()
    while L != []:
        nb_couleur += 1
        s = L.pop() #sommet de plus haut degre
        coloriage[s] = nb_couleur
        for s1 in L[::-1]: #dans l ordre decroissant
            flag = True
            for s2 in voisins(s1, G):
                if s2 in coloriage and coloriage[s2] == nb_couleur:
                    flag = False
                    break
            if flag:
                coloriage[s1] = nb_couleur
        L = [s for s in L if s not in coloriage]
    return coloriage
         
         
                  
        
    

