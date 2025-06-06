import os
import shutil

def source_to_destination(source, destination):

    if os.path.exists(destination) == True:
        shutil.rmtree(destination)
        os.mkdir(destination)
    elif os.path.exists(destination) == False:
        os.mkdir(destination)

    src_files = os.listdir(source)
    for item in src_files:
        if os.path.isfile(os.path.join(source, item)) is True:
            shutil.copy(os.path.join(source, item), destination)
        else:
            source_to_destination(os.path.join(source, item), os.path.join(destination, item))
