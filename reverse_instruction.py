def reverseInstruction(listInstruction):
    """listInstruction = ['v -0.01 -0.99 0.79', 'f 165 95 99'] """

    reversedInstructions = [str] * len(listInstruction)
    for i in range(len(listInstruction)):
        instruction = listInstruction[i]
        instruction_array = instruction.split()
        command = instruction_array[0]
        indice_element = instruction_array[1]
        newInstruct = instruction
        
        if command == "efv":
            # Edit vertex from face (n°vertex in [1,2,3])
            # 'efv n°face n°vertex new_value
            # Prends une face, choisis un sommet, et le remplace avec un nouveau
            # Inverse: Prends une face, prends un nouveau et le remplace avec l'ancien

            old_vertex = instruction_array[2]
            new_vertex = instruction_array[3]
            newInstruct = 'efv ' + indice_element + ' ' + new_vertex + ' ' + old_vertex
            pass

        elif command == "v":
            # Un vertex a été créé. 
            # Inverse: delete ce vertex. MAIS comme ce vertex sera attaché à aucune face, on ne le delete pas.
            pass

        elif command == "f":
            # Une face a été créée
            # Inverse: Delete cette face
            newInstruct = 'df ' + indice_element
            pass

        elif command == "ev":
            # Edit vertex
            # Inverse: ne pas éditer, donc renvoyer le vertex d'origine
            # On doit récupérer les coordonnées d'origine
            x_coord = instruction_array[5]
            y_coord = instruction_array[6]
            z_coord = instruction_array[7]
            newInstruct = 'ev ' + indice_element + ' ' + x_coord + ' ' + y_coord + ' ' + z_coord

        elif command == "dv":
            # Delete vertex
            # Inverse: Create vertex
            x_coord = instruction_array[2]
            y_coord = instruction_array[3]
            z_coord = instruction_array[4]
            newInstruct = "v " + x_coord + ' ' + y_coord + ' ' + z_coord

        elif command == "tv":
            # Translate vertex
            # Inverse: Translate in the other sens
            x_coord = instruction_array[2]
            y_coord = instruction_array[3]
            z_coord = instruction_array[4]
            newInstruct = "tv " + indice_element + ' ' + str(-float(x_coord)) + ' ' + str(-float(y_coord)) + ' ' + str(-float(z_coord))
            pass

        elif command == "ef":
            # Edit face
            # Inverse: Ne pas éditer face
            x_coord = instruction_array[5]
            y_coord = instruction_array[6]
            z_coord = instruction_array[7]
            newInstruct = 'ef ' + indice_element + ' ' + x_coord + ' ' + y_coord + ' ' + z_coord

        elif command == "df":
            # Delete face
            # Inverse: Create face
            x_coord = instruction_array[2]
            y_coord = instruction_array[3]
            z_coord = instruction_array[4]
            newInstruct = "f " + x_coord + ' ' + y_coord + ' ' + z_coord

        elif command == "s":
            # Set memory
            # Balise utile pour certain papier, délire de bits, tout ça...
            # dizaine de balises à utiliser dans l'idéal. (abscisse des courbes)
            # A mettre à chaque grande étape, 3000 lignes de codes, on aura ça.
            # Pour compter la taille de vos fichiers (balises "s" dans vos codes), vous pouvez utiliser le dictionnaire suivant.
            # SIZES = {"v": 13, "f": 4, "ev":14, "tv":14, "ef": 5, "efv": 4, "df":1, "ts": 6, "tf": 7, "s": 0, "#": 0}
            # Inverse: Retirer memory
            # newInstruct = "s " + '-' + indice_element
            pass
        else:
            print('Unexpected value in reverse instruction')
        
        reversedInstructions[-(i+1)] = newInstruct
    # reversedInstructions.reverse()
    return reversedInstructions

def main():
    efv = 'efv 1 3 4'
    v = 'v 0.0 0.0 0.0'
    f = 'f 1 2 3'
    ev = 'ev 453 -0.01 -0.98 0.79 -0.01 -0.45 0.58'
    tv = 'tv 1 1.0 1.0 1.0'
    ef = 'ef 1 1 2 4 1 2 3'
    df = 'df 1 1 2 4'
    s = 's 48'
    listInstruction = [efv, v, f, ev, tv, ef, df, s]
    reverse = reverseInstruction(listInstruction)
    print('reverse = ', reverse)

if __name__ == "__main__":
    # execute only if run as a script
    main()