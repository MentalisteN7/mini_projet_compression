
from obj_loader import ObjLoader
import numpy as np
import math


class infoVertexVoisin():

    def __init__(self):
        self.dic_voisins = {} # Stock les voisins des vertex, pas de doublon, donc derniers vertex (en indice), n'auront "pas de voisins" car déjà pris en compte dans les premiers

        self.proches = []
        self.voisin_per_vertex = {} # Stock tous les voisins de chaque vertex
        self.treshold = 1

    def init_voisin(self, lapin):
    # Construction de dic_voisins et voisin_per_vertex
        
        for face in lapin.faces:
            
            sorted_face = sorted(face)
            first_vertex = sorted_face[0]
            second_vertex = sorted_face[1]
            third_vertex = sorted_face[2]

            voisins_first = self.dic_voisins.get(first_vertex)
            if voisins_first == None:
                self.dic_voisins[first_vertex] = [second_vertex]
                self.dic_voisins[first_vertex] = self.dic_voisins[first_vertex] + [third_vertex]


                self.voisin_per_vertex[first_vertex] = [second_vertex]
                self.voisin_per_vertex[first_vertex] = self.voisin_per_vertex[first_vertex] + [third_vertex]
            
            else:
                is_second_vertex_in_first = second_vertex in voisins_first
                if not(is_second_vertex_in_first):
                    self.dic_voisins[first_vertex] = self.dic_voisins[first_vertex] + [second_vertex]

                    self.voisin_per_vertex[first_vertex] = self.voisin_per_vertex[first_vertex] + [second_vertex]

                is_third_vertex_in_first = third_vertex in voisins_first
                if not(is_third_vertex_in_first):
                    self.dic_voisins[first_vertex] = self.dic_voisins[first_vertex] + [third_vertex]

                    self.voisin_per_vertex[first_vertex] = self.voisin_per_vertex[first_vertex] + [third_vertex]

            voisins_second = self.dic_voisins.get(second_vertex)
            if voisins_second == None:
                self.dic_voisins[second_vertex] = [third_vertex]

                self.voisin_per_vertex[second_vertex] = [first_vertex]
                self.voisin_per_vertex[second_vertex] = self.voisin_per_vertex[second_vertex] + [third_vertex]
            
            else:
                is_third_vertex_in_second = third_vertex in voisins_second
                if not(is_third_vertex_in_second):
                    self.dic_voisins[second_vertex] = self.dic_voisins[second_vertex] + [third_vertex]

                    self.voisin_per_vertex[second_vertex] = self.voisin_per_vertex[second_vertex] + [third_vertex]
                
                voisins_vertex_first = self.voisin_per_vertex.get(first_vertex)
                if voisins_vertex_first == None:
                    # On ne passe normalement jamais dans cette boucle
                    self.voisin_per_vertex[second_vertex] = [first_vertex]
                else:
                    is_first_vertex_in_second = third_vertex in voisins_vertex_first
                    if not(is_first_vertex_in_second):
                        self.voisin_per_vertex[second_vertex] = self.voisin_per_vertex[second_vertex] + [first_vertex]

            #### set voisins of the third vertex
            voisins_third = self.voisin_per_vertex.get(third_vertex)
            if voisins_third == None:
                self.voisin_per_vertex[third_vertex] = [first_vertex]
                self.voisin_per_vertex[third_vertex] = self.voisin_per_vertex[third_vertex] + [second_vertex]
            
            else:
                is_first_vertex_in_third = first_vertex in voisins_third
                if not(is_first_vertex_in_third):
                    self.voisin_per_vertex[third_vertex] = self.voisin_per_vertex[third_vertex] + [first_vertex]

                is_second_vertex_in_third = second_vertex in voisins_third
                if not(is_second_vertex_in_third):
                    self.voisin_per_vertex[third_vertex] = self.voisin_per_vertex[third_vertex] + [second_vertex]

    
    def __norm_tuple(self,v1,v2):
        v1_x = v1[0]
        v1_y = v1[1]
        v1_z = v1[2]

        v2_x = v2[0]
        v2_y = v2[1]
        v2_z = v2[2]

        norm = math.sqrt( (v1_x - v2_x)**2 + (v1_y - v2_y)**2 + (v1_z - v2_z)**2 )
        return norm


    def init_proche(self, lapin):

        vertices_left = lapin.vertices

        ind_v1 = 1
        ind_v2 = 1

        for v1 in lapin.vertices:
            for v2 in vertices_left:
                distance = self.__norm_tuple(v1,v2)

                if (distance > 0 and distance < self.treshold):
                    self.proches.append((ind_v1, ind_v2))
                    # self.proches.append((ind_v2, ind_v1))

                ind_v2 = ind_v2 + 1

            ind_v1 = ind_v1 + 1
            del vertices_left[-1] # On ne repasse pas sur les premiers vertex déjà traités

        def init_voisin_per_vertex(self, lapin):
            k = 0
            
            for face in lapin.faces:
                # if True:
                k = k + 1
                first_vertex = face[0]
                second_vertex = face[1]
                third_vertex = face[2]




def main():
    obj = 'bunny_origin.obj'
    lapin = ObjLoader(obj)
    print(lapin.vertices[lapin.faces[0][0]])

    nb_vertices = len(lapin.vertices)

    valid_pair_instance = infoVertexVoisin()
    valid_pair_instance.init_voisin(lapin)
    # print(valid_pair_instance.voisins)

    v1 = lapin.vertices[0]
    v2 = lapin.vertices[1]
    # d = valid_pair_instance.norm_tuple(v1,v2)
    print(lapin.vertices[0])

    valid_pair_instance.init_proche(lapin)
    print(len(valid_pair_instance.proches))
    print(len(valid_pair_instance.dic_voisins))
    print('len(valid_pair_instance.voisin_per_vertex) = ', len(valid_pair_instance.voisin_per_vertex))
    # print((valid_pair_instance.dic_voisins))

if __name__ == "__main__":
    # execute only if run as a script
    main()
