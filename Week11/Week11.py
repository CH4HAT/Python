from pathlib import Path
import json

"""
    pathlib - navigating, writing and reading files (alternate to .os path)
    file i/o - funnctions for reading/writing files
    JSON - javascript object notation (plain text format for snding/receiving storing data)
"""
"""
    Pathlib
    for anything related to the filesystem(list contents of a folder, create folder/directory, create a file, etc)  we have to create the path 

"""

test_directory = Path('./data2')  #the path object is loaction of something

test_directory.mkdir()  # makes a path and also generates an error if it already exists 

#or write this 

test_directory.mkdir(exist_ok=True)

test_file = test_directory.joinpath('text3.txt')
test_file.touch()

"""
    path methods 
    
"""

"""
    note: if no path object, use open()

    with open('somefile.txt) as file:
    
    also:
    file_get_contents() - read to a file
    file_put_contents() - write to a file 
"""


"""
    listing all files/folders of a particular location in the directory 


    path.glob('./*.py')  - this willl find all the python extension in the current directory


    path.glob('**/*.py') - search recursively through all * sub folders* for python files 
"""

for file in test_directory.glob('*.txt'):
    print(file.name)

"""
  JSON - Javascripct object notation
  (similar to python directory) - pair of keys and values, where the keys are strings

  {
    "firstname" :"chris",
    "rmail" : "whyareyougay@shemamail.com"
  }
"""
"""
    python methods of reading/writing json 
    reading:
    .load() -> read json into python directory
    .loads()   read json into a string

    writing
    .dump()    write json as an iobject
    .dumps()  write json as an string

    note: before reading/writing we have to open the file



"""


with open ('./data3/chahat.json','w') as file:
    j = json.load(file)
    print(j,type(j))
    print(j["firstname"])  