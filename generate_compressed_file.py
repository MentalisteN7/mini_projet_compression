from typing import List
from obj_loader import ObjLoader, calculS
from getListQ import getListQ, getListKp
from infoVertexVoisin import infoVertexVoisin
from get_optimal_contraction import get_optimal_contraction
from pairQueue import PairQueue
from simplify_obj import simplifyObj
from reverse_instruction import reverseInstruction
from contraction_iteration import contraction_iteration

def generate_compressed_file(pathIn = 'assets/bunny_origin.obj', pathOut = 'bunny_origin_compress.obj', targetSize=100, treshold=0, ):
    obj = ObjLoader(pathIn)

    #1. Compute the Q matrices for all the initial vertices.
    listKp = getListKp(obj)
    listQ = getListQ(obj, listKp)
    
    #2.  Select all valid pairs.
    validPairs = infoVertexVoisin()
    validPairs.treshold = treshold
    validPairs.init_voisin(obj)
    
    #3. Compute the optimal contraction target v_bar and the cost for each valid pair (v1,v2)
    #4. Place all the pairs in a heap keyed on cost with the minimum cost pair at the top.
    pairQueue = PairQueue([], [])
    # print(validPairs.dic_voisins)
    for v1_ind in range(len(obj.vertices)):
        v1 = obj.vertices[v1_ind]
        Q1 = listQ[v1_ind]
        for v2_ind in validPairs.dic_voisins[v1_ind+1]:
            v2 = obj.vertices[v2_ind-1] #les indices en python commencent à 0 mais ceux des .obj commencent à 1
            Q2 = listQ[v2_ind-1]
            cost, v_bar = get_optimal_contraction(v1, v2, Q1, Q2)
            pairQueue.push((v1_ind+1,v2_ind, v_bar), cost)
    
    #5. Iteratively remove the pair (v1;v2) of least cost from the heap,contract this pair
    deletedVertices = []
    instructions = []
    numVertices = len(obj.vertices)
    vertexNb = numVertices
    
    while (numVertices > targetSize) and (not pairQueue.isEmpty()) :
        obj, listQ, validPairs, pairQueue, deletedVertices, instructions, vertexNb = \
            contraction_iteration(obj, listQ, validPairs, pairQueue, deletedVertices, instructions, vertexNb)
        numVertices -= 1
    
    debut = simplifyObj(instructions, pathIn)
    fin   = reverseInstruction(instructions)
    for i in range(1,10):
        ind = int(i * len(fin)/10)
        fin.insert(ind, calculS(fin[:ind]))
    fin.append(calculS(fin))
    instructions = debut + fin

    obj_file_compress = open(pathOut, 'w')
    instructions = [e + '\n' for e in instructions]
    obj_file_compress.writelines(instructions)
    obj_file_compress.close()

    return 1

# generate_compressed_file()
# generate_compressed_file(pathIn='assets/triangle.obj', targetSize=1)
generate_compressed_file(pathOut = '../obja/assets/bunny_origin_compress.obj', targetSize=400, treshold=0)
# generate_compressed_file(pathOut = 'bunny_origin_compress.obj', targetSize=400, treshold=0)
generate_compressed_file(pathIn="assets/crate.obj", pathOut = '../obja/assets/crate_compress.obj', targetSize=4, treshold=0)
# generate_compressed_file(pathIn="../obja/assets/cube.obj", pathOut = '../obja/assets/cube_compress.obj', targetSize=3, treshold=0)
