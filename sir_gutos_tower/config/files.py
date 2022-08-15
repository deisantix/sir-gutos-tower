import pathlib

directory_of_this_file = pathlib.Path(__file__).parent
source_directory = directory_of_this_file.parent

POV_WITCHER = source_directory.name + '/historia/pov-witcher.json'
