##initialisations (ne fait pas partie de l'itération)
from pairQueue import PairQueue

pairQueue = PairQueue(pairList, costList)

deletedVertices = []

##itération
toContract = PairQueue.pop()
v1_ind = toContract[0]
v2_ind = toContract[1]

v1 = lapin.vertices[v1_ind-1]
v2 = lapin.vertices[v2_ind]-1]
Q1 = listQ[v1_ind-1]
G2 = listQ[v2_ind-1]
v_bar = get_optimal_contraction(v1,v2, Q1, Q2) #ou v_bar = v_bar_list[indice] si on choisit de les stocker

lapin.vertices[v1_ind-1] = v_bar
listQ[v1_ind] = Q1 + Q2
voisins_v2 = validPairs.dic_voisins.get(v2_ind)
for voisin in voisins_v2 :
    voisinage_voisin =  validPairs.dic_voisins[voisin]
    voisinage_voisin.remove(v2_ind)
    if not (v1_ind in voisinage_voisin):
        voisinage_voisin.append(v1_ind)
    validPairs.dic_voisins[voisin] = voisinage_voisin
    
deletedVertices.append(v2_ind)