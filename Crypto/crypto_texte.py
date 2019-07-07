# Cf chapitre 2 : document cryto .pdf
texte="quejaimeafaireapprendrecenombreutileauxsages"
L=[(texte.count(c),c) for c in set(texte)]
L.sort()
print(L[-5:])
#Print liste des bigrammes :

Paires ={}
N = len(texte)
for i in range(N-2):
    bg1 = texte[i:i+2]
    Paires[bg1] = 1
    for j in range(i+1, N-1):
        bg2 = texte[j:j+2]
        if bg1 == bg2:
            if bg1 not in Paires.keys():
                Paires[bg1] = 2
            else:
                Paires[bg1] += 1
                    
print(Paires)
