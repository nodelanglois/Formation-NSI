from random import randint
#print(randint(0,1))
L0 = [bool(randint(0,1)) for i in range(6) ]
print(L0)
L0 =[0 ,0 ,0,1 ,1 ,1 ]
L1 = [L0[0] and L0[1], L0[1] or L0[2], L0[0] and L0[4], L0[3] and L0[5], L0[3] or L0[5]]
print(L1)
L2 = [L1[1] or L1[2], L1[0] and L1[3], L1[1] and L0[4], L0[2] or L1[4]]
print(L2)
L3 = [L1[0] or L2[0], L2[0] and L2[1], L1[2] or L1[4], L2[2] and L1[3]]
print(L3)
L4 = [L3[0] and L3[1], L3[1] or L3[2], L3[0] or L2[1], L3[2] and L3[3], L2[2] or L2[3], L3[3] and L2[3]]
print(L4)


# utiliser & bit à bit et  | bit à bit
