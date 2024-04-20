print("Creates a datapack with functions folder")

name = input("Datapack name (optional): ")

packversion = input("Datapack version: ")

funcfolder = input("Function namespace: ")



import os
from os import mkdir



join = os.path.join

def mkfile(file: str, value: str = ""):
    with open(file, "w") as f:
        f.write(value)


mkdir(name)
mkdir(join(name, "data"))
mkfile(join(name, "pack.mcmeta"), f'''{{
    "pack": {{
        "pack_format": {packversion},
        "description": "The default data for Minecraft"
    }}
}}''')

mkdir(join(name, "data", funcfolder))
mkdir(join(name, "data", funcfolder, "functions"))






