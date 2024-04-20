
BAG = """
play B4
wait 10

play A4
wait 10

play G4
wait 20

play B4
wait 10

play A4
wait 10

play G4
wait 20

play G4
wait 10
play G4
wait 10

play A4
wait 10
play A4
wait 10

play B4
wait 10

play A4
wait 10

play G4
wait 10
"""

def simple(notes: str, wait: int):
    result = []
    notes = notes.split(",")
    for note in notes:
        result.append(f"play {note}\nwait {wait}\n")

    return "\n".join(result)

C_SCALE = simple("C4,D4,E4,F4,G4,A4,B4,C5,B4,A4,G4,F4,E4,D4,C4", 3)
D_SCALE = simple("D4,E4,g4,G4,A4,B4,d5,D5,d5,B4,A4,G4,g4,E4,D4", 3)
E_SCALE = simple("E4,g4,a4,A4,B4,d5,e5,E5,e5,d5,B4,A4,a4,g4,E4", 3)