from typing import List
import numpy as np
from numpy.core.numeric import Inf

class ObjLoader(object):
    def __init__(self, fileName):
        self.vertices = []
        self.faces = []
        ##
        try:
            f = open(fileName)
            for line in f:
                line_array = line.split()
                if len(line_array) > 0:
                    command = line_array[0]
                    
                    if command == "v":
                        x_coord = line_array[1]
                        y_coord = line_array[2]
                        z_coord = line_array[3]
                        
                        vertex = np.array([float(x_coord), float(y_coord), float(z_coord)])
                        self.vertices.append(vertex)

                    elif command == "f":
                        vertex_1 = int(line_array[1])
                        vertex_2 = int(line_array[2])
                        vertex_3 = int(line_array[3])
                        
                        face = [vertex_1, vertex_2, vertex_3]
                        self.faces.append(tuple(face))

            f.close()
        except IOError:
            print(".obj file not found.")
    
    def updateFaces(self, deletedVertex: int):
        for j in range(len(self.faces)):
            if self.faces[j] != None:
                e = self.faces[j]
                self.faces[j] = (e[0]-int(e[0]>deletedVertex), 
                                 e[1]-int(e[1]>deletedVertex), 
                                 e[2]-int(e[2]>deletedVertex))

    def toOBJ(self):
        obj = []
        
        i = 0
        while i < len(self.vertices):
            if self.vertices[i].any() == None:
                self.updateFaces(i+1)
                self.vertices.pop(i)
            else :
                i += 1
        
        for vertex in self.vertices:
            obj += ['v ' + verticeTxt(vertex)]
        for face in self.faces:
            if face != None:
                obj += ['f ' + faceTxt(face)]
        obj += ['s ' + str(len(self.vertices)*13 + len(self.faces)*4)]
        return obj

def calculS(listInstruction) -> str:
    SIZES = {"v": 13, "f": 4, "ev":14, "tv":14, "ef": 5, "efv": 4, "df":1, "ts": 6, "tf": 7, "s": 0, "#": 0}
    taille = 0
    for inst in listInstruction:
        inst.replace("\n", "")
        if len(inst.split()) > 0:
            taille += SIZES[inst.split()[0]]
    # return ''
    return 's ' + str(taille)

def verticeTxt(vertex) -> str:
    return str(vertex)[1:-1]

def faceTxt(face, oldVertexNb: int = Inf, newVertexNb: int = Inf, deletedVertices = []) -> str:
    if oldVertexNb != Inf and newVertexNb != Inf:

        diff0 = int(face[0]!=oldVertexNb)
        diff1 = int(face[1]!=oldVertexNb)
        diff2 = int(face[2]!=oldVertexNb)
        face = (face[0]+int(face[0]==oldVertexNb)*(newVertexNb - oldVertexNb), 
                face[1]+int(face[1]==oldVertexNb)*(newVertexNb - oldVertexNb), 
                face[2]+int(face[2]==oldVertexNb)*(newVertexNb - oldVertexNb))

        face = (face[0] - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[0]]) * diff0,
                face[1] - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[1]]) * diff1,
                face[2] - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[2]]) * diff2)

    return str(face).replace(",", "")[1:-1]