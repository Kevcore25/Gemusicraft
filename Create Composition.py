fileName = input("File name: ")

if not fileName.endswith(".py"): fileName = fileName + ".py"

with open(fileName, "x") as f:
    f.write('''from gemusicraft import *

"""
Note format: A 2-3 length string, like G4, or Ab3. Note must be capitialized, or it will be turned into a flat
The note range is Gb5 - Gb5
Basic commands of gemusicraft:

play(note) - Plays a note
wait(ticks) - Wait an amount of ticks before playing another note

set_namespace(datapack namespace) - Set the namespace of the folder
run() - Generates the melody for use in datapacks
"""

# Example:
play("C4")
wait(10)
play("D4")

set_namespace("cmd")
run()

''')
    
input("Done! Press enter to continue...")
exit() # No idea why i have this