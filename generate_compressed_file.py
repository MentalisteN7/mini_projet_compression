from obj_loader import ObjLoader
from shutil import copyfile

def generate_compressed_file(pathIn = 'bunny_origin.obj', pathOut = 'bunny_origin_compress.obj'):
    obj = ObjLoader(pathIn)
    copyfile(pathIn, pathOut)

    obj_file_compress = open(pathOut, 'a')
    
    obj_file_compress.write('1ere ligne à ajouter\n')
    obj_file_compress.writelines(['2eme ligne à ajouter\n', '3eme ligne à ajouter\n'])

    obj_file_compress.close()
    return 1

# generate_compressed_file()