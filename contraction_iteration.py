from typing import List
from pairQueue import PairQueue
from get_optimal_contraction import get_optimal_contraction
from obj_loader import ObjLoader, verticeTxt, faceTxt
import numpy as np

def contraction_iteration(model: ObjLoader, Qlist, validPairs, pairQueue: PairQueue, deletedVertices, instructions, vertexNb):
    """
    Réalise une itération de l'étape 5
    """

    toContract = pairQueue.pop(deletedVertices)
    v1_ind = toContract[0]
    v2_ind = toContract[1]
    v_bar = toContract[2]
    
    v1 = model.vertices[v1_ind-1]
    v2 = model.vertices[v2_ind-1]
    Q1 = Qlist[v1_ind-1]
    Q2 = Qlist[v2_ind-1]
    # _, v_bar = get_optimal_contraction(v1,v2, Q1, Q2) #ou v_bar = v_bar_list[indice] si on choisit de les stocker
    
    #v1 devient  v_bar
    instructions += ['ev ' + str(v1_ind- sum([int(e) for e in  np.array(deletedVertices)<v1_ind])) + ' ' + verticeTxt(v_bar) + ' ' + verticeTxt(model.vertices[v1_ind-1])]
    model.vertices[v1_ind-1] = v_bar
    Qlist[v1_ind] = Q1 + Q2
    
    #suppression des références à v2
    voisinage_v2 = validPairs.voisin_per_vertex.get(v2_ind)
    for voisin in voisinage_v2 :
        voisinage_voisin =  validPairs.voisin_per_vertex[voisin].copy()

        voisinage_voisin.remove(v2_ind)
        if not (v1_ind in voisinage_voisin): #on évite les redondances
            voisinage_voisin.append(v1_ind)
        validPairs.voisin_per_vertex[voisin] = voisinage_voisin

    ################ Bloc Instruction ################
    for i in range(len(instructions)):
        instruct = instructions[i]
        if instruct[:2] == 'df':
            df = [int(e) for e in instruct.split()[2:]]
            v2_ind_act = v2_ind - sum([int(e) for e in  np.array(deletedVertices)<v2_ind])

            dfXeqVertexNb = df[0] == vertexNb
            if v2_ind_act == df[0]:
                df[0] = vertexNb
            elif v2_ind_act < df[0] and df[0] < vertexNb or dfXeqVertexNb:
                df[0] -= 1

            dfXeqVertexNb = df[1] == vertexNb
            if v2_ind_act == df[1]:
                df[1] = vertexNb
            elif v2_ind_act < df[1] and df[1] < vertexNb or dfXeqVertexNb:
                df[1] -= 1

            dfXeqVertexNb = df[2] == vertexNb
            if v2_ind_act == df[2]:
                df[2] = vertexNb
            elif v2_ind_act < df[2] and df[2] < vertexNb or dfXeqVertexNb:
                df[2] -= 1

            instructions[i] = str(instruct.split()[:2] + df).replace(",", "").replace("'", "")[1:-1]
    for i in range(len(model.faces)):
        
        face = model.faces[i]
        if v2_ind in face and not hasIntersection(face, deletedVertices):
            instructions += ['df ' + str(i+1) + ' ' + faceTxt(face, v2_ind, vertexNb, deletedVertices)]
    instructions += ['dv ' + str(v2_ind) + ' ' + verticeTxt(model.vertices[v2_ind-1])]
    vertexNb -= 1
    ##################################################

    deletedVertices.append(v2_ind)
    #Les paires qui sont devenues invalides et qui sont à l'avant de la file sont nettoyées
    pairQueue.cleanFront(deletedVertices)
    
    #v1 reçoit les voisins de v2
    voisinage_v1 = validPairs.voisin_per_vertex[v1_ind].copy()
    for v in voisinage_v2:
        if (v != v1_ind) and not(v in voisinage_v1):
            voisinage_v1.append(v)
    validPairs.voisin_per_vertex[v1_ind] = voisinage_v1
    
    #recalcule des coûts des paires impliquant v1
    for voisin_ind in voisinage_v1:
        voisin = model.vertices[voisin_ind-1]
        Q1 = Qlist[v1_ind-1]
        Qvoisin = Qlist[voisin_ind-1]
        cost, v_bar =  get_optimal_contraction(v1, voisin, Q1, Qvoisin)
        pairQueue.push((v1_ind, voisin_ind, v_bar), cost)
    
    return model, Qlist, validPairs, pairQueue, deletedVertices, instructions, vertexNb

def hasIntersection(list1: List[int], list2: List[int]):
    for i in list1:
        if i in list2:
            return True
    return False
