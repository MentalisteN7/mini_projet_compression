from getListQ import getListKp, getListQ
from infoVertexVoisin import infoVertexVoisin
from typing import Tuple
from obj_loader import ObjLoader
import numpy as np


# v1,v2: tuples 3x1
# q1,q2: ??
def get_optimal_contraction(v1,v2,q1,q2):
    q_tilt = q1 + q2
    q_tilt[3,:] = 0
    q_tilt[3,3] = 1

    # v_tilt = __addition_tuple(v1,v2)

    determinant = np.linalg.det(q_tilt)

    if (determinant == 0):
        q_inv = np.linalg.inv(q_tilt)
        vect_un = [0, 0, 0, 1]
        v_tilt = q_inv.dot(vect_un)
        v_trans =  v_tilt.transpose()
        aux = v_tilt.dot(q_inv)
        error = aux.dot(v_trans)

    else:
        q_inv = np.linalg.inv(q_tilt)
        v_tilt = __addition_tuple(v1,v2)
        v_tilt = __division_tuple(v_tilt, 2)
        v_tilt = v_tilt +  (1,)
        v_tilt = np.asarray(v_tilt)
        v_trans =  v_tilt.transpose()
        aux = v_tilt.dot(q_inv)
        error = aux.dot(v_trans)

    return error



def __addition_tuple(v1,v2):
        v1_x = v1[0]
        v1_y = v1[1]
        v1_z = v1[2]

        v2_x = v2[0]
        v2_y = v2[1]
        v2_z = v2[2]

        v =  ( v1_x + v2_x, v1_y + v2_y, v1_z + v2_z )
        return v

def __division_tuple(v1,diviseur):
        v1_x = v1[0] / 2
        v1_y = v1[1] / 2
        v1_z = v1[2] / 2

        v =  (v1_x, v1_y, v1_z)
        return v
        
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
