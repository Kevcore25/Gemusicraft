import notegen as mcn
from random import randint

noteValues = ["C","D","E","F","G","A","B"]

mcn.FOLDER = "composition" + str(randint(0,100))
mcn.NAMESPACE = None

def set_namespace(namespace: str):
    """Sets the namespace of the mcfunction"""
    mcn.NAMESPACE = namespace.lower()
def set_folder(folder: str):
    """Sets the folder of the mcfunction notes"""
    mcn.FOLDER = folder.lower()
def set_sound(soundID: str = "block.note_block.harp"):
    """Sets the sound"""
    mcn.SOUND = soundID
def set_volume(volume: int):
    """Sets the volume of the notes"""
    mcn.VOLUME = volume 
def set_sound_type(soundType: str):
    """Sets the category of the sound"""
    mcn.TYPE = soundType.lower()
def set_selector(selector: str):
    """Sets the player who will hear the melody"""
    mcn.SELECTOR = selector




def conv_note(note: str) -> str:
    """Convert a note into a supported version. E.g. Gb4 into g4 or F#4 into g4"""

    if len(note) == 3:
        n, a, b = tuple(note)
        
        if "#" in a+b: 
            nv = noteValues.index(n)
            n = noteValues[nv - 1].lower()
        elif "b" in a+b:
            n = n.lower()
        
        if a.isnumeric(): return n + a
        elif b.isnumeric(): return n + b
    elif len(note) == 2: return note
    elif len(note) == 1 and note.upper() in noteValues: return note + "4"
    else: return "--"

def check_note(note: str) -> bool:
    """Checks to see if a note is valid"""

    note = conv_note(note)

    if len(note) == 2:
        n, o = tuple(note)
        if n.upper() in noteValues and o.isnumeric():
            return True
        else: return False
    else:
        return False




result = []
def play(note: str) -> bool:
    """Plays a note in a notation like G4. Range: Gb3 - Gb5"""
    global result

    convNote = conv_note(note)
    if check_note(convNote):
        result.append("play " + convNote)
        return True
    else:
        print(f"[WARNING] Note {note} is invalid!")
        return False
        
def note(note: str) -> bool:
    """Alias for play command"""
    return play(note)

def wait(ticks: int) -> bool:
    """Waits an amount of ticks before playing another note"""
    global result

    if str(ticks).isnumeric():
        result.append("wait " + str(int(ticks)))
        return True
    else:
        print(f"[WARNING] Wait parameter incorrect ({ticks} is not numeric)")

def sleep(seconds: float) -> bool:
    """Waits an amount of seconds. It converts into ticks (which only supports integers), so it may be inaccurate"""
    return wait(round(seconds * 20))

def play_song(song: str) -> None:
    """Plays a song. The song must be written in PsC format"""
    global result
    for line in song.splitlines(): 
        result.append(line)

def run() -> bool:
    """Runs the played melody"""

    if mcn.NAMESPACE is not None:
        mcn.convertPsCToMCF(
            "\n".join(result)
        )
        print(f"Melody created! After reloading, use: function {mcn.NAMESPACE}:{mcn.FOLDER}/start to start!")
    else:
        print("[ERROR] Datapack namespace is not set! The melody will not generate.\nPlease set the namespace using set_namespace('your datapack namespace')")
        return False