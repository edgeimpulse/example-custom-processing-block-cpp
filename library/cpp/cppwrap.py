import cppyy
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
cppyy.add_include_path(os.path.join(current_dir))

sources = [
    'test.hpp',
]
for filename in sources:
    try:
        with open(os.path.join(current_dir,filename), 'r') as file:
            source = file.read()
        cppyy.cppdef(source)
    except FileNotFoundError as e:
        print("File not found:", filename)
        raise e
