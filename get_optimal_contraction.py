from getListQ import getListKp, getListQ
from validPair import validPair
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

    q_inv = np.linalg.inv(q_tilt)
    vect_un = [0, 0, 0, 1]

    v_tilt = q_inv.dot(vect_un)

    print(v_tilt)

def __addition_tuple(v1,v2):
        v1_x = v1[0]
        v1_y = v1[1]
        v1_z = v1[2]

        v2_x = v2[0]
        v2_y = v2[1]
        v2_z = v2[2]

        v =  ( v1_x + v2_x, v1_y + v2_y, v1_z + v2_z )
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
    valid_pair_instance = validPair()
    valid_pair_instance.init_voisin(lapin)
    valid_pair_instance.init_proche(lapin)
    print(valid_pair_instance.voisins[0])
    v_pair_ind = valid_pair_instance.voisins[0]
    v1_ind = v_pair_ind[0]
    v2_ind = v_pair_ind[1]
    v1 = lapin.vertices[v1_ind]
    v2 = lapin.vertices[v2_ind]
    get_optimal_contraction(v1,v2,q1,q2)

if __name__ == "__main__":
    # execute only if run as a script
    main()
