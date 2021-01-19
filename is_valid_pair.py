
from obj_loader import ObjLoader
import numpy as np


class validPair():

    def __init__(self):
        self.voisins = []
        self.proches = []
        self.treshold = 5

    def init_voisin(self, lapin):
        k = 0
        # valid_pair.append((1,2))
        # Contruction matrice d'adjacence
        for face in lapin.faces:
            # if True:
            k = k + 1
            first_vertex = face[0]
            second_vertex = face[1]
            third_vertex = face[2]

            self.voisins.append((first_vertex,second_vertex))  # first -> second
            self.voisins.append((second_vertex,first_vertex))  # second -> second

            self.voisins.append((first_vertex,third_vertex))  # first -> third
            self.voisins.append((third_vertex,first_vertex))  # third -> first

            self.voisins.append((second_vertex,third_vertex))  # second -> third
            self.voisins.append((third_vertex,second_vertex))  # third -> second

            # adjacence_matrix[first_vertex-1][second_vertex-1] = 1 # first -> second
            # adjacence_matrix[second_vertex-1][first_vertex-1] = 1 # second -> first

            # adjacence_matrix[first_vertex-1][third_vertex-1] = 1 # first -> third
            # adjacence_matrix[third_vertex-1][first_vertex-1] = 1 # third -> first

            # adjacence_matrix[second_vertex-1][third_vertex-1] = 1 # second -> third
            # adjacence_matrix[third_vertex-1][second_vertex-1] = 1 # third -> second

    def init_proche(self, lapin):

        for vertex in lapin.vertices:


            distance = self.norm_tuple(v1,v2)
    
    def norm_tuple(self,v1,v2):
        v1_x = v1[0]
        v1_y = v1[1]
        v1_z = v1[2]

        v2_x = v2[0]
        v2_y = v2[1]
        v2_z = v2[2]

        norm = (v1_x - v2_x)

        norm = v1_x - v2_x

        return norm



obj = 'bunny_origin.obj'
lapin = ObjLoader(obj)
print(lapin.vertices[lapin.faces[0][0]])

nb_vertices = len(lapin.vertices)

valid_pair_instance = validPair()
valid_pair_instance.init_voisin(lapin)
# print(valid_pair_instance.voisins)

v1 = lapin.vertices[0]
v2 = lapin.vertices[1]
valid_pair_instance.norm_tuple(v1,v2)
print(lapin.vertices[0])