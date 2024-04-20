"""Converts a string of notes into a folder of files for minecraft datapacks"""
# Version 1

# By default, all notes consectively are played as eighth notes.
# Tempo is a fixed of 3 ticks every note (because i do not want to do math and calculate tempo / 20 and stuff)
# Therefore, A1--A1 will play 2 A1 quarter notes  

# Each note is 2 lengths long
# Start a note by its letter, then the octave range (e.g. A4)
# Sharps are not made, but flats are. To use flat, type the lowercase of a letter (a1)

""" CONFIG """
# NAMESPACE
# The namespace of your Minecraft datapack
NAMESPACE = "cmd"

# FOLDER
# Forces it to be lowercase!
# This is the folder containing all the notes
FOLDER = "test"

# SOUND ID
# The ID to be played with using playsound
SOUND = "block.note_block." + "harp"

# VOLUME
# The volume of the sound
VOLUME = 1

# TYPE OF SOUND
# The category of the sound
TYPE = "neutral"

# SELECTOR
# Use @a if you want it to be heard for everyone
SELECTOR = "@a"

"""
EXAMPLES:
Using KN (convertKNToPsC, then convertPsCToMCF)

Play notes together with new lines (lets call them tracks)
Each track will play all at once, and then the next note will play
Use -- or 2 spaces to rest 1 beat
EXAMPLE:
convertPsCToMCF(convertFNToPsC([
    "C4--D4  E4",
    "E4  F4  G4"
]))

Using PsC:

Notes will be played together until a wait/wait is called
Commands:
play <note>: plays a note. notes can be seperated by spaces, which will act the same thing
wait <time>: rests for <time> beats
wait <ticks>: waits <ticks> ticks in minecraft. 20 ticks = 1 second

EXAMPLE:
convertPsCToMCF('''
play C4
play E4
wait 1

play D4 F4
wait 1

play E4 G4
''')

WHICH IS BETTER?:
KN is easier and quicker to write simple songs
PsC allows more customization (wait), and generally is more optimized
"""

import os
def convertKNToPsC(melody: list):
    PsC = []
    
    for beat in range(0, len(melody[0]), 2):
        waits = 0
        for m in melody:

            fullBeat = m[beat] + m[beat+1]

            if fullBeat in ("  ", "--"):
                waits += 1
            elif fullBeat.isnumeric():
                PsC.append("wait " + fullBeat)
                waits = -100
            else:
                PsC.append("play " + fullBeat)

        if waits == len(melody):
            PsC.append("wait 2")
        else:
            PsC.append("wait 1")

    return "\n".join(PsC)


UseCount = {
    "g3": 0,
    "G3": 1,
    "a3": 2,
    "A3": 3,
    "b3": 4,
    "B3": 5,
    "c4": 5,
    "C4": 6,
    "d4": 7,
    "D4": 8,
    "e4": 9,
    "E4": 10,
    "f4": 10,
    "F4": 11,
    "g4": 12,
    "G4": 13,
    "a4": 14,
    "A4": 15,
    "b4": 16,
    "B4": 17,
    "c5": 17,
    "C5": 18,
    "d5": 19,
    "D5": 20,
    "e5": 21,
    "E5": 22,
    "f5": 22,
    "F5": 23,
    "g5": 24,
}

def findTicks(amount: int):
    # beatsPerMin = TEMPO / 60
    # ticks = beatsPerMin * 20

    # return round(ticks / amount / 4)
    return round(3 * amount)
def convertPsCToMCF(PsC: str):
    """Converts the pseudocode format into mcfunction files"""
    try:
        os.mkdir(FOLDER)
    except: pass

    mcf = []
    mcfNotes = []
    fileNum = 0
    for line in PsC.splitlines():
        if line.lower().startswith("play"):
            notes = line.split("play ", 1)[1].split(" ")

            for note in notes:
                if note in UseCount:
                    mcf.append(f"execute as {SELECTOR} at @s run playsound {SOUND} {TYPE} @s ~ ~ ~ {VOLUME} {round(2 ** ((UseCount[note] - 12)/12), 6)}")
                    mcfNotes.append(note)
                else:
                    print(f"[WARN] Note {note} is invalid (skipped)!")

        elif line.lower().replace("_","").startswith("wait"):
            time = int(line.lower().replace("_","").split("wait ")[1])
            mcf.append(f"schedule function {NAMESPACE}:{FOLDER}/{fileNum+1} {time}t append")

            with open(os.path.join(FOLDER, str(fileNum)+".mcfunction"), "w") as f:
                f.write(
                    f"# Notes: {', '.join(mcfNotes)}\n" + "\n".join(mcf)
                ) 
            mcf, mcfNotes = [], []
            fileNum += 1

        elif line.lower().startswith("rest"):
            time = findTicks(int(line.split("wait ")[1]))
            mcf.append(f"schedule function {NAMESPACE}:{FOLDER}/{fileNum+1} {time}t")

            with open(os.path.join(FOLDER, str(fileNum)+".mcfunction"), "w") as f:
                f.write(
                    f"# Notes: {', '.join(mcfNotes)}\n" + "\n".join(mcf)
                ) 
            mcf, mcfNotes = [], []
            fileNum += 1

    
        elif line.isspace() or line == "": pass
        
        else: 
            print(f"[WARN] Line \"{line}\" is invalid!")

    # Final
    with open(os.path.join(FOLDER, str(fileNum)+".mcfunction"), "w") as f:
        f.write(
            f"# FINAL | Notes: {', '.join(mcfNotes)}\n" + "\n".join(mcf)
        ) 
    with open(os.path.join(FOLDER, "start.mcfunction"), "w") as f:
        f.write(f"# Starts the music\nfunction {NAMESPACE}:{FOLDER}/0") 
    with open(os.path.join(FOLDER, "stop.mcfunction"), "w") as f:
        f.write(f"# Stop the music\n" + "\n".join(f"schedule clear {NAMESPACE}:{FOLDER}/{i}" for i in range(fileNum))) 

    #print(f"Saved! Use function {NAMESPACE}:{FOLDER}/start to start!")
    return True


""" COMPOSING AREA """
# Write your code below here

# Example: BAG
#convertPsCToMCF(

#)
if "__main__" in __name__:
    import songs
    convertPsCToMCF(
        songs.C_SCALE + songs.D_SCALE + songs.E_SCALE
    )

    input("SAVED!")