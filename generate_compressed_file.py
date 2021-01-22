from obj_loader import ObjLoader
from shutil import copyfile

def generate_compressed_file(pathIn = 'bunny_origin.obj', pathOut = 'bunny_origin_compress.obj'):
    obj = ObjLoader(pathIn)
    copyfile(pathIn, pathOut)

    obj_file_compress = open(pathOut, 'a')

    instructions = ['1ere ligne à ajouter', '2eme ligne à ajouter', '3eme ligne à ajouter']

    instructions = [e + '\n' for e in instructions]
    obj_file_compress.writelines(instructions)
    obj_file_compress.close()

    return 1

# generate_compressed_file()