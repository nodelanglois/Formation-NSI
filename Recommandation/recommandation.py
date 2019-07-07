from read_reco import load
from numpy import *

Xtrain = load('db.txt')
print(Xtrain)
 # 27 personnes et 87 films
print(Xtrain.shape)

NbUser = 13

def dist(x,y):
    return sqrt(sum((x-y)**2))

def nn(x, X):
    mind = dist(x,X[0])
    imind = 0
    for i in range(1,X.shape[0]):
        d = dist(x,X[i])
        if d<=mind and i!=NbUser:
            mind = d
            imind = i
    return imind


i = nn(NbUser,Xtrain)

print(Xtrain[NbUser])
#print(Xtrain[i])

