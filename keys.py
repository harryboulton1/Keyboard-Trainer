import os

frequencies = {"C3":131, "C#3":140, "D3":148, "D#3":156, "E3":165, "F3":175,
               "F#3":185, "G3":196, "G#3":208, "A3":220, "A#3":233, "B3":245,
               "C4":261, "C#4":277, "D4":294, "D#4":311, "E4":330, "F4":349,
               "F#4":370, "G4":392, "G#4":415, "A4":440, "A#4":466, "B4":494, "C5":523}
mode = 0
class Key:    
    def __init__(self, name):
        self.name = name
        self.freq = frequencies[name]
        if os.name == 'nt':
            self.location = "sounds\\"+name.replace("#","s").lower()+".wav"
        if os.name == 'posix':
            self.location = "sounds/"+name.replace("#","s").lower()+".wav"
        self.state = False
        self.key = object
        self.pos = int #EXERCISE 4

    def __repr__(self):
        return self.name

    @property
    def root(self):
        return self.name[:-1]

    def press(self, event=None):
        global state
        if self.state:
            self.state = False
        else:
            self.state = True
        self.play()

    if os.name == 'nt':
        import winsound
        def play(self, event=None):
            print(mode)

            if mode == 0:
                winsound.PlaySound(self.location, winsound.SND_ALIAS)
            else:
                winsound.Beep(self.freq, 1000)

    if os.name == 'posix':
        
        def play(self, event=None):
            import subprocess
            subprocess.call(["afplay", self.location])

c3 = Key("C3")
cs3 = Key("C#3")
d3 = Key("D3")
ds3 = Key("D#3")
e3 = Key("E3")
f3 = Key("F3")
fs3 = Key("F#3")
g3 = Key("G3")
gs3 = Key("G#3")
a3 = Key("A3")
as3 = Key("A#3")
b3 = Key("B3")
c4 = Key("C4")
cs4 = Key("C#4")
d4 = Key("D4")
ds4 = Key("D#4")
e4 = Key("E4")
f4 = Key("F4")
fs4 = Key("F#4")
g4 = Key("G4")
gs4 = Key("G#4")
a4 = Key("A4")
as4 = Key("A#4")
b4 = Key("B4")
c5 = Key("C5")

white_notes = (c3, d3, e3, f3, g3, a3, b3, c4, d4, e4, f4, g4, a4, b4, c5)
black_notes = (cs3, ds3, fs3, gs3, as3, cs4, ds4, fs4, gs4, as4)
note_order = (c3, cs3, d3, ds3, e3, f3, fs3, g3, gs3, a3, as3, b3, c4, cs4,
             d4, ds4, e4, f4, fs4, g4, gs4, a4, as4, b4, c5)
all_notes = note_order
note_names = ["C","D","E","F","G","A","B","C#","Eb","F#","G#","Bb"]
comparators = ["c","d","e","f","g","a","b","cs","ds","fs","gs","as"]



pos = 1
for note in all_notes:
    note.pos = pos
    pos+=1
