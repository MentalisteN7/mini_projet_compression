from obj_loader import ObjLoader
import numpy as np

def simplify_obj(listInstruction, pathIn = 'bunny_origin.obj'):
    obj = ObjLoader(pathIn)

    for instruction in listInstruction:
        
        if instruction[:3] == "efv":
            # Edit vertice from face (n°vertice in [1,2,3])
            # 'efv n°face n°vertice new_value
            
            listI = instruction.split()
            indiceFace = int(listI.pop(1)) - 1
            indice123  = int(listI.pop(1)) - 1
            indiceVertice = obj.faces[indiceFace][indice123]
            vertex = np.array([float(listI[i]) for i in range(1,len(listI))])
            obj.vertices[indiceVertice] = vertex

        elif instruction[:2] == "v ":
            # Declare vertice
            
            listI = instruction.split()
            vertex = np.array([float(listI[i]) for i in range(1,len(listI))])
            obj.vertices.append(vertex)

        elif instruction[:2] == "f ":
            # Declare face

            listI = instruction.split()
            face = np.array([int(listI[i]) for i in range(1,len(listI))])
            obj.faces.append(tuple(face))

        elif instruction[:2] == "ev":
            # Edit vertice
            
            listI = instruction.split()
            indice = int(listI.pop(1)) - 1
            vertex = np.array([float(listI[i]) for i in range(1,len(listI))])
            obj.vertices[indice] = vertex
            
        elif instruction[:2] == "tv":
            # Translate vertice
            
            listI = instruction.split()
            indice = int(listI.pop(1)) - 1
            vertex = np.array([float(listI[i]) for i in range(1,len(listI))])
            obj.vertices[indice] += vertex

        elif instruction[:2] == "ef":
            # Edit face
            
            listI = instruction.split()
            indice = int(listI.pop(1)) - 1
            face = np.array([int(listI[i]) for i in range(1,len(listI))])
            obj.vertices[indice] = face
            
        elif instruction[:2] == "df":
            # Delete face
            
            listI = instruction.split()
            indice = int(listI.pop(1)) - 1
            obj.faces[indice] = None

        elif instruction[:2] == "ts":
            # Triangle strips
            print('Triangle strips was unexpected and not implemented')
            pass
        elif instruction[:2] == "tf":
            # Triangle fans
            print('Triangle fans was unexpected and not implemented')
            pass
        elif instruction[:2] == "s ":
            # Set memory
            pass
        else:
            print('Unexpected value in reverse instruction')


    return obj.toOBJ()


if __name__ == "__main__":
    # execute only if run as a script
    # listInstruction = ['ev 453 -0.01 -0.98 0.79','df 1']
    # instruction = 'efv 1 165 -0.01 -0.98 0.79'
    # obj = ObjLoader('bunny_origin.obj')