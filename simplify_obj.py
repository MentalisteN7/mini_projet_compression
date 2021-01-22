from obj_loader import ObjLoader
from shutil import copyfile

def simplify_obj(pathIn = 'bunny_origin.obj', listInstruction):
    for i in range(len(listInstruction)):
        instruction = listInstruction[i]
        newInstruct = instruction
        
        if instruction[:3] == "efv":
            # Edit vertice from face (n°vertice in [1,2,3])
            # 'efv n°face n°vertice new_value
            pass

        elif instruction[:2] == "v ":
            pass

        elif instruction[:2] == "f ":
            pass

        elif instruction[:2] == "ev":
            # Edit vertice
            pass
        elif instruction[:2] == "tv":
            # Translate vertice
            pass
        elif instruction[:2] == "ef":
            # Edit face
            pass
        elif instruction[:2] == "df":
            # Delete face
            pass
        elif instruction[:2] == "ts":
            # Triangle strips
            pass
        elif instruction[:2] == "tf":
            # Triangle fans
            pass
        elif instruction[:2] == "s ":
            # Set memory
            pass
        else:
            print('Unexpected value in reverse instruction')

        reversedInstructions[-(i+1)] = newInstruct
    return reversedInstructions

listInstruction = ['ev 453 -0.01 -0.98 0.79','df 1']
print(reverseInstruction(listInstruction))