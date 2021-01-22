from shutil import copyfile

from obj_loader import ObjLoader
from getListQ import getListQ, getListKp
from infoVertexVoisin import infoVertexVoisin
from get_optimal_contraction import get_optimal_contraction
from pairQueue import PairQueue
from simplify_obj import simplifyObj
from reverse_instruction import reverseInstruction

def generate_compressed_file(pathIn = 'bunny_origin.obj', pathOut = 'bunny_origin_compress.obj', targetSize=100, treshold=0, ):
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
    for v1_ind in range(len(obj.vertices)):
        v1 = obj.vertices[v1_ind]
        Q1 = listQ[v1_ind]
        for v2_ind in validPairs.dic_voisins:
            v2 = obj.vertices[v2_ind-1] #les indices en python commencent à 0 mais ceux des .obj commencent à 1
            Q2 = listQ[v2_ind-1]
            cost, v_bar = get_optimal_contraction(v1, v2, Q1, Q2)
            pairQueue.push((v1_ind+1,v2_ind, v_bar), cost)
    
    #5. Iteratively remove the pair (v1;v2) of least cost from the heap,contract this pair
    deletedVertices = []
    numVertices = len(obj.vertices)
    while (numVertices > targetSize) and (not pairQueue.isEmpty) :
        obj, listQ, validPairs, pairQueue, deletedVertices = \
            contraction_iteration(obj, listQ, validPairs, pairQueue, deletedVertices)
        numVertices -= 1
    
    
    efv = 'efv 1 3 4'
    v = 'v 0.0 0.0 0.0'
    f = 'f 1 2 3'
    ev = 'ev 453 -0.01 -0.98 0.79 -0.01 -0.45 0.58'
    tv = 'tv 1 1.0 1.0 1.0'
    ef = 'ef 1 1 2 4 1 2 3'
    df = 'df 1 1 2 4'
    s = 's 48'
    listInstruction = [efv, v, f, ev, tv, ef, df, s]
    
    debut = simplifyObj(listInstruction, pathIn)
    fin   = reverseInstruction(listInstruction)
    instructions = debut + fin
    
    obj_file_compress = open(pathOut, 'w')
    instructions = [e + '\n' for e in instructions]
    obj_file_compress.writelines(instructions)
    obj_file_compress.close()

    return 1

generate_compressed_file()
