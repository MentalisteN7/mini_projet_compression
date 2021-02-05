from getListQ import getListKp, getListQ
from infoVertexVoisin import infoVertexVoisin
from typing import Tuple
from obj_loader import ObjLoader
import numpy as np


# v1,v2: tuples 3x1
# q1,q2: ??
def get_optimal_contraction(v1,v2,q1,q2):
    q_barre = q1 + q2
    q_aux = q_barre
    q_aux[3,:] = 0
    q_aux[3,3] = 1
    
    conditionnement = np.linalg.cond(q_aux)
    #Si q_aux est inversible, 
    if (conditionnement < 1 / np.finfo(q_aux.dtype).eps) :
        q_inv = np.linalg.inv(q_aux)
        vect_un = [0, 0, 0, 1]
        v_barre = q_inv.dot(vect_un)
        cost = v_barre.dot(q_barre).dot(v_barre.transpose())
        cost = cost.item()
        v_barre = np.squeeze(np.asarray(v_barre))[0:3] #on ne veut pas la représentation homogène
    
    else:
        # print("cas non inversible activé pour v1= " + str(v1) + " v2= " + str(v2))
        #Si q_aux n'est pas inversible, prendre le sommet optimal sur le segment v1,v2
        v1_hom = np.ones(4)
        v2_hom = np.ones(4)
        v1_hom[0:3] = v1
        v2_hom[0:3] = v2
        cout_v1 = v1_hom.dot(q_barre).dot(v1_hom).item()
        cout_v2 = v2_hom.dot(q_barre).dot(v2_hom).item()
        cout_v1v2 = v1_hom.dot(q_barre).dot(v2_hom).item()
        #cela revient à trouver le minimum d'un polynôme de degré 2 dans [0,1]
        a = cout_v1 - 2*cout_v1v2 + cout_v2
        b = 2*(cout_v1v2 - cout_v2)
        # c = cout_v2 #on n'a pas besoin de c pour les calculs
        
        #le seul cas intéressant est celui où a > 0 et -b/2a est dans [0,1]
        if a > 0 :
            alpha = -b / (2*a)
        else :
            alpha = -1
        
        if 0 <= alpha <= 1:
            v_barre = alpha * v1_hom + (1-alpha)*v1_hom
            cost = v_barre.dot(q_barre).dot(v_barre)
            cost = cost.item()
            v_barre = v_barre[0:3]
        
        #Si cela aussi échoue, choisir v_barre parmi les extrémités ou le milieu
        else:
            milieu_hom = 0.5* (v1_hom + v2_hom)
            cout_milieu = milieu_hom.dot(q_barre).dot(milieu_hom).item()
            #On s'arrange pour que le milieu soit choisi dans les cas ambigus
            candidats = [(cout_v1, 1, v1_hom), (cout_milieu, 0, milieu_hom), (cout_v2, 2, v2_hom)]
            paire_min = min(candidats)
            cost = paire_min[0]
            v_barre = paire_min[2][0:3]

    return cost, v_barre
        
def main():
    obj = 'bunny_origin.obj'
    lapin = ObjLoader(obj)

    # STEP 1:
    listKp = getListKp(lapin)
    listQ = getListQ(lapin, listKp)
    q1 = listQ[0]
    q2 = listQ[1]
    # print(listQ[0])

    # STEP 2:
    valid_pair_instance = infoVertexVoisin()
    valid_pair_instance.init_voisin(lapin)
    valid_pair_instance.init_proche(lapin)
    print(valid_pair_instance.dic_voisins[1])
    v_pair_ind = valid_pair_instance.dic_voisins[1]
    v1_ind = v_pair_ind[0]
    v2_ind = v_pair_ind[1]
    v1 = lapin.vertices[v1_ind]
    v2 = lapin.vertices[v2_ind]
    cost, v_barre = get_optimal_contraction(v1,v2,q1,q2)
    print('cost = ', cost)
    print('v_barre', v_barre)
    # test =  np.asarray(lapin.vertices)
    # print(test)
    # print(lapin.faces)

    # dic = {}
    # dic[1] = [5]
    # dic[1] = dic[1] + [3]
    # print(dic.get(2))
    
    # print(dic)

if __name__ == "__main__":
    # execute only if run as a script
    main()
