from shutil import copyfile

from obj_loader import ObjLoader
from getListQ import getListQ, getListKp
from infoVertexVoisin import infoVertexVoisin
from get_optimal_contraction import get_optimal_contraction
from pairQueue import PairQueue

def generate_compressed_file(pathIn = 'bunny_origin.obj', pathOut = 'bunny_origin_compress.obj', targetSize=100, treshold=0, ):
    obj = ObjLoader(pathIn)
    copyfile(pathIn, pathOut)

    obj_file_compress = open(pathOut, 'a')

    instructions = ['1ere ligne à ajouter', '2eme ligne à ajouter', '3eme ligne à ajouter']

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
    for v1_ind in range(len(obj.vertices)):
        v1 = obj.vertices(v1_ind)
        Q1 = listQ[v1_ind]
        for v2_ind in validPairs.dic_voisins:
            v2 = obj.vertices[v2_ind-1] #les indices en python commencent à 0 mais ceux des .obj commencent à 1
            Q2 = listQ[v2_ind-1]
            cost, _ = get_optimal_contraction(v1, v2, Q1, Q2)
            pairQueue.push((v1_ind+1,v2_ind, cost))
    
    #5. Iteratively remove the pair (v1;v2) of least cost from the heap,contract this pair
    deletedVertices = []
    numVertices = len(obj.vertices)
    while (numVertices > targetSize) and (not pairQueue.isEmpty) :
        obj, listQ, validPairs, pairQueue, deletedVertices = \
            contraction_iteration(obj, listQ, validPairs, pairQueue, deletedVertices)
        numVertices -= 1
    

    instructions = [e + '\n' for e in instructions]
    obj_file_compress.writelines(instructions)
    obj_file_compress.close()

    return 1

# generate_compressed_file()