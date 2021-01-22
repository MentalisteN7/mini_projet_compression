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
    
    conditionnement = np.linalg.cond(q_barre)
    #Si q_aux est inversible, 
    if (conditionnement < 1e5):
        q_inv = np.linalg.inv(q_aux)
        vect_un = [0, 0, 0, 1]
        v_barre = q_inv.dot(vect_un)
        cost = v_barre.dot(q_barre).dot(v_barre.transpose())
        v_barre = v_barre[0:3] #on ne veut pas la représentation homogène
    
    #Si cela aussi échoue, choisir v_barre parmi les extrémités ou le milieu
    else:
        milieu = 0.5 * (v1 + v2)
        candidats = [v1, milieu, v2]
        vect_homogene = np.ones(4)
        cost = np.Inf
        imin = 0
        for i in range(3):
            vect_homogene[0:3] = candidats[i]
            costi = vect_homogene.dot(q_barre).dot(vect_homogene)
            if costi < cost:
                cost = costi
                imin = i
        v_barre = candidats[i]
        
    

    return cost, v_barre



# def __addition_tuple(v1,v2):
#         v1_x = v1[0]
#         v1_y = v1[1]
#         v1_z = v1[2]
# 
#         v2_x = v2[0]
#         v2_y = v2[1]
#         v2_z = v2[2]
# 
#         v =  ( v1_x + v2_x, v1_y + v2_y, v1_z + v2_z )
#         return v
# 
# def __division_tuple(v1,diviseur):
#         v1_x = v1[0] / 2
#         v1_y = v1[1] / 2
#         v1_z = v1[2] / 2
# 
#         v =  (v1_x, v1_y, v1_z)
#         return v
        
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
    error = get_optimal_contraction(v1,v2,q1,q2)
    print('error = ', error)
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
