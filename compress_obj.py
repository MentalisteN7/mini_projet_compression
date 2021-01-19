from typing import Tuple
from obj_loader import ObjLoader
import numpy as np

obj = 'bunny_origin.obj'

lapin = ObjLoader(obj)
# 1.  Compute the Q matrices for all the initial vertices.

def getKp(a, b, c, d):
    return [[a*a, a*b, a*c, a*d],
            [a*b, b*b, b*c, b*d],
            [a*c, b*c, c*c, c*d],
            [a*d, b*d, c*d, d*d]]

def getPlaneEquation(v1, v2, v3):
    a = (v2[1] - v1[1]) * (v3[2] - v1[2]) - (v3[1] - v1[1])*(v2[2] - v1[2])
    b = (v2[2] - v1[2]) * (v3[0] - v1[0]) - (v3[2] - v1[2])*(v2[0] - v1[0])
    c = (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v3[0] - v1[0])*(v2[1] - v1[1])
    d = - (a*v1[0] + b*v1[1] + c*v1[2])

    tot = (a + b + c + d)
    return (a/tot, b/tot, c/tot, d/tot)

def getListKp(obj: ObjLoader):
    listKp = []
    for face in obj.faces:
        v1 = obj.vertices[face[0]-1]
        v2 = obj.vertices[face[1]-1]
        v3 = obj.vertices[face[2]-1]
        a, b, c, d = getPlaneEquation(v1, v2, v3)
        listKp += [getKp(a, b, c, d)]
    return listKp

def getListQ(obj: ObjLoader, listK):
    listQ = []
    for vertex_index in range(1,len(obj.vertices) + 1):
        Q = np.matrix([[0., 0., 0., 0.],
                       [0., 0., 0., 0.],
                       [0., 0., 0., 0.],
                       [0., 0., 0., 0.]])

        for face_index in range(len(obj.faces)):
            if vertex_index in obj.faces[face_index]:
                Q += np.matrix(listKp[face_index])

        listQ += [Q]
    return listQ

# a, b, c, d = planeEquation(lapin.vertices[lapin.faces[0][0]], lapin.vertices[lapin.faces[0][1]], lapin.vertices[lapin.faces[0][2]])
# kp = Kp(a, b, c, d)
listKp = getListKp(lapin)
listQ = getListQ(lapin, listKp)
print(listQ[0])
# print(listKp[1])
# 2.  Select all valid pairs.
# 3.  Compute the optimal contraction target Nv for each valid pair.v1;v2/. 
# The errorNvT.Q1CQ2/Nv of this target vertex becomes the cost of contracting that pair.
# 4.  Place all the pairs in a heap keyed on cost with the minimumcost pair at the top.
# 5.  Iteratively remove the pair.v1;v2/of least cost from the heap,contract this pair, and update the costs of all valid pairs involv-ingv1.