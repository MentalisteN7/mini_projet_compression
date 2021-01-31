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

                        # index1 = line.find(" ") + 1
                        # index2 = line.find(" ", index1 + 1)
                        # index3 = line.find(" ", index2 + 1)
                        # vertex = np.array([float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1])])
                        vertex = np.array([float(x_coord), float(y_coord), float(z_coord)])
                        self.vertices.append(vertex)

                    elif command == "f":
                        string = line.replace("//", "/")
                        ##
                        vertex_1 = int(line_array[1])
                        vertex_2 = int(line_array[2])
                        vertex_3 = int(line_array[3])
                        # i = string.find(" ") + 1
                        face = [vertex_1, vertex_2, vertex_3]
                        # for item in range(string.count(" ")):
                        #     if string.find(" ", i) == -1:
                        #         face.append(int(string[i:-1]))
                        #         break
                        #     face.append(int(string[i:string.find(" ", i)]))
                        #     i = string.find(" ", i) + 1
                        ##
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
    return ''
    return 's ' + str(taille)

def verticeTxt(vertex) -> str:
    return str(vertex)[1:-1]

def faceTxt(face, oldVertexNb: int = Inf, newVertexNb: int = Inf, deletedVertices = []) -> str:
    if oldVertexNb != Inf and newVertexNb != Inf:
        face = (face[0]+int(face[0]==oldVertexNb)*(newVertexNb - oldVertexNb), 
                face[1]+int(face[1]==oldVertexNb)*(newVertexNb - oldVertexNb), 
                face[2]+int(face[2]==oldVertexNb)*(newVertexNb - oldVertexNb))

        v2_ind_act = oldVertexNb - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[0]])
        face = (face[0] - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[0]]) * int(face[0]!=newVertexNb), #probablement int(face[0]<newVertexNb)
                face[1] - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[1]]) * int(face[1]!=newVertexNb),
                face[2] - sum([int(e) for e in  np.array([oldVertexNb] + deletedVertices)<face[2]]) * int(face[2]!=newVertexNb))

        # face = (face[0]-int(any(face[0]>(np.array([oldVertexNb] + deletedVertices))) and face[0]!=newVertexNb)*max(1,len(deletedVertices)), 
        #         face[1]-int(any(face[1]>(np.array([oldVertexNb] + deletedVertices))) and face[1]!=newVertexNb)*max(1,len(deletedVertices)), 
        #         face[2]-int(any(face[2]>(np.array([oldVertexNb] + deletedVertices))) and face[2]!=newVertexNb)*max(1,len(deletedVertices)))
    
        # face = (face[0]-int(face[0]>oldVertexNb and face[0]!=newVertexNb), 
        #         face[1]-int(face[1]>oldVertexNb and face[1]!=newVertexNb), 
        #         face[2]-int(face[2]>oldVertexNb and face[2]!=newVertexNb))
    return str(face).replace(",", "")[1:-1]

def upFace(face, oldVertexNb: int, newVertexNb: int) -> str:
    face = (face[0]+int(face[0]==oldVertexNb)*(newVertexNb - oldVertexNb), 
            face[1]+int(face[1]==oldVertexNb)*(newVertexNb - oldVertexNb), 
            face[2]+int(face[2]==oldVertexNb)*(newVertexNb - oldVertexNb))

    face = (face[0]-int(face[0]>oldVertexNb and face[0]<newVertexNb), 
            face[1]-int(face[1]>oldVertexNb and face[1]<newVertexNb), 
            face[2]-int(face[2]>oldVertexNb and face[2]<newVertexNb))
    return face

def any(list: List[bool]):
    res = False
    for e in list:
        res = res or e
    return res