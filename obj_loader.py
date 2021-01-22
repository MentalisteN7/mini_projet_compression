import numpy as np

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
                    # vertex = np.matrix([round(vertex[0], 2), round(vertex[1], 2), round(vertex[2], 2)])
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

    def toOBJ(self):
        obj = []
        # SIZES = {"v": 13, "f": 4, "ev":14, "tv":14, "ef": 5, "efv": 4, "df":1, "ts": 6, "tf": 7, "s": 0, "#": 0}
        for vertex in self.vertices:
            obj += ['v ' + str(vertex)[1:-1]]
        for face in self.faces:
            obj += ['f ' + str(face).replace(",", "")[1:-1]]
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