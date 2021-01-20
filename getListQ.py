from typing import Tuple
from obj_loader import ObjLoader
import numpy as np

# obj = 'bunny_origin.obj'
# lapin = ObjLoader(obj)

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
    norm = np.sqrt(a*a + b*b + c*c)
    a = a / norm
    b = b / norm
    c = c / norm
    d = - (a*v1[0] + b*v1[1] + c*v1[2])
    
    return (a, b, c, d)

def getListKp(obj: ObjLoader):
    listKp = []
    for face in obj.faces:
        v1 = obj.vertices[face[0]-1]
        v2 = obj.vertices[face[1]-1]
        v3 = obj.vertices[face[2]-1]
        a, b, c, d = getPlaneEquation(v1, v2, v3)
        listKp += [getKp(a, b, c, d)]
    return listKp

def getListQ(obj: ObjLoader, listKp):
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
# listKp = getListKp(lapin)
# listQ = getListQ(lapin, listKp)
# print(listQ[0])