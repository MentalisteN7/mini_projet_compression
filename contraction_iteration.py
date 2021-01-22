##initialisations (ne fait pas partie de l'itération)
from pairQueue import PairQueue

pairQueue = PairQueue(pairList, costList)

deletedVertices = []

##itération
toContract = pairQueue.pop()
v1_ind = toContract[0]
v2_ind = toContract[1]

v1 = lapin.vertices[v1_ind-1]
v2 = lapin.vertices[v2_ind]-1]
Q1 = listQ[v1_ind-1]
Q2 = listQ[v2_ind-1]
_, v_bar = get_optimal_contraction(v1,v2, Q1, Q2) #ou v_bar = v_bar_list[indice] si on choisit de les stocker

#v1 devient  v_bar
lapin.vertices[v1_ind-1] = v_bar
listQ[v1_ind] = Q1 + Q2

#suppression des références à v2
voisinage_v2 = validPairs.voisin_per_vertex.get(v2_ind)
for voisin in voisinage_v2 :
    voisinage_voisin =  validPairs.voisin_per_vertex[voisin]
    voisinage_voisin.remove(v2_ind)
    if not (v1_ind in voisinage_voisin): #on évite les redondances
        voisinage_voisin.append(v1_ind)
    validPairs.voisin_per_vertex[voisin] = voisinage_voisin
deletedVertices.append(v2_ind)

#v1 reçoit les voisins de v2
voisinage_v1 = validPairs.voisin_per_vertex[v1_ind]
for v in voisinage_v2:
    if (v != v1_ind) and not(v in voisinage_v1):
        voisinage_v1.append(v)
validPairs.voisin_per_vertex[v1_ind] = voisinage_v1

#recalcul des coûts des paires impliquant v1
for voisin_ind in voisinage_v1:
    voisin = lapin.vertices[voisin_ind-1]
    Q1 = listQ[v1_ind-1]
    Qvoisin = listQ[voisin_ind-1]
    cost, _ =  get_optimal_contraction(v1,voisin, Q1, Qvoisin)
    pairQueue.push((v1_ind, voisin_ind), cost)
    
