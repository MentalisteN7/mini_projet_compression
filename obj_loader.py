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
                if line[:2] == "v ":
                    index1 = line.find(" ") + 1
                    index2 = line.find(" ", index1 + 1)
                    index3 = line.find(" ", index2 + 1)

                    vertex = np.array([float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1])])
                    self.vertices.append(vertex)

                elif line[0] == "f":
                    string = line.replace("//", "/")
                    ##
                    i = string.find(" ") + 1
                    face = []
                    for item in range(string.count(" ")):
                        if string.find(" ", i) == -1:
                            face.append(int(string[i:-1]))
                            break
                        face.append(int(string[i:string.find(" ", i)]))
                        i = string.find(" ", i) + 1
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
    return 's ' + str(taille)

def verticeTxt(vertex) -> str:
    return str(vertex)[1:-1]

def faceTxt(face, oldVertexNb: int = Inf, newVertexNb: int = Inf) -> str:
    if oldVertexNb != Inf and newVertexNb != Inf :
        face = (face[0]+int(face[0]==oldVertexNb)*(newVertexNb - oldVertexNb), 
                face[1]+int(face[1]==oldVertexNb)*(newVertexNb - oldVertexNb), 
                face[2]+int(face[2]==oldVertexNb)*(newVertexNb - oldVertexNb))

        face = (face[0]-int(face[0]>oldVertexNb and face[0]!=newVertexNb), 
                face[1]-int(face[1]>oldVertexNb and face[1]!=newVertexNb), 
                face[2]-int(face[2]>oldVertexNb and face[2]!=newVertexNb))
    return str(face).replace(",", "")[1:-1]