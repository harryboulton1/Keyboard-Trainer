from tkinter import *
import tkinter.font as tkFont
import time, random
from keys import *
from chords import *

interval_list = ["Unison", "Minor 2nd", "Major 2nd","Minor 3rd","Major 3rd",
                     "Perfect 4th","Tritone","Perfect 5th","Minor 6th",
                     "Major 6th","Minor 7th","Major 7th","Octave"]
il = interval_list

def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
    kwargs["smooth"] = True
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return user_canvas.create_polygon(points, **kwargs)

def gen_menu_button():
    d = height/2
    x1 = width*0.1
    y1 = (height*0.6)-d
    x2 = x1+(height*0.9-height*0.6)
    y2 = (height*0.9)-d

    menu_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    menu_text = user_canvas.create_text((x1+((x2-x1)/2)), (y1+((y2-y1)/2)), text="Menu", font=("Nueva Std", 48), anchor="c", fill="grey10")
    user_canvas.tag_bind(menu_button, "<Enter>", lambda e: user_canvas.itemconfig(menu_button, fill="#d3d3d3"))
    user_canvas.tag_bind(menu_button, "<Leave>", lambda e: user_canvas.itemconfig(menu_button, fill="#b7b7b7"))
    user_canvas.tag_bind(menu_button, "<Button-1>", main_menu)
    user_canvas.tag_bind(menu_text, "<Button-1>", main_menu)

    
def main_menu(event=None):
    user_canvas.delete('all')
    for whitenote in white_notes:
        keyboard_canvas.itemconfig(whitenote.key, fill="white")
    for blacknote in black_notes:
        keyboard_canvas.itemconfig(blacknote.key, fill="black")
    keyboard_canvas.delete('blank')
    gen_menu_button()

    #Generate exercise buttons
    d = height/2
    x1 = width*0.4
    y1 = (height*0.6)-d
    x2 = x1+(width*0.161)
    y2 = (height*0.6+height*0.143)-d
    ex1_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex1_text = user_canvas.create_text(width*0.48, (height*0.671)-d, text="Exercise 1", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex1_button, "<Enter>", lambda e: user_canvas.itemconfig(ex1_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex1_button, "<Leave>", lambda e: user_canvas.itemconfig(ex1_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex1_button, "<Button-1>", lambda e: start(ex1))

    x1 = x2+(width*0.008)
    y1 = y1
    x2 = x2+(width*0.008)+(x2-(width*0.4))
    y2 = y2
    ex2_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex2_text = user_canvas.create_text(width*0.649, (height*0.671)-d, text="Exercise 2", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex2_button, "<Enter>", lambda e: user_canvas.itemconfig(ex2_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex2_button, "<Leave>", lambda e: user_canvas.itemconfig(ex2_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex2_button, "<Button-1>", lambda e: start(ex2))

    x1 = x2+(width*0.008)
    y1 = y1
    x2 = width*0.9
    y2 = y2
    ex3_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex3_text = user_canvas.create_text(width*0.82, (height*0.671)-d, text="Exercise 3", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex3_button, "<Enter>", lambda e: user_canvas.itemconfig(ex3_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex3_button, "<Leave>", lambda e: user_canvas.itemconfig(ex3_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex3_button, "<Button-1>", lambda e: start(ex3))

    d = height/2
    x1 = width*0.4
    y1 = (height*0.756)-d
    x2 = x1+(width*0.161)
    y2 = (height*0.9)-d
    ex4_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex4_text = user_canvas.create_text(width*0.48, (height*0.827)-d, text="Exercise 4", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex4_button, "<Enter>", lambda e: user_canvas.itemconfig(ex4_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex4_button, "<Leave>", lambda e: user_canvas.itemconfig(ex4_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex4_button, "<Button-1>", lambda e: start(ex4))

    x1 = x2+(width*0.008)
    y1 = y1
    x2 = x2+(width*0.008)+(x2-(width*0.4))
    y2 = y2
    ex5_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex5_text = user_canvas.create_text(width*0.649, (height*0.827)-d, text="Exercise 5", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex5_button, "<Enter>", lambda e: user_canvas.itemconfig(ex5_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex5_button, "<Leave>", lambda e: user_canvas.itemconfig(ex5_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex5_button, "<Button-1>", lambda e: start(ex5))

    x1 = x2+(width*0.008)
    y1 = y1
    x2 = width*0.9
    y2 = y2
    ex6_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex6_text = user_canvas.create_text(width*0.82, (height*0.827)-d, text="Exercise 6", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex6_button, "<Enter>", lambda e: user_canvas.itemconfig(ex6_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex6_button, "<Leave>", lambda e: user_canvas.itemconfig(ex6_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex6_button, "<Button-1>", lambda e: start(ex6))

    #Keyboard Only Button
    x1 = (width*0.1)+(height*0.9-height*0.6)+(width*0.008)
    y1 = (height*0.6)-d
    x2 = (width*0.4)-(width*0.008)
    y2 = (height*0.9)-d
    keyboard_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    keyboard_text = user_canvas.create_text((width*0.333), (y1+((y2-y1)/2)), text="Keyboard Only", font=("Nueva Std", 36), anchor="c", fill="grey10", justify='center', width=(x2-x1)*0.8)
    user_canvas.tag_bind(keyboard_button, "<Enter>", lambda e: user_canvas.itemconfig(keyboard_button, fill="#d3d3d3"))
    user_canvas.tag_bind(keyboard_button, "<Leave>", lambda e: user_canvas.itemconfig(keyboard_button, fill="#b7b7b7"))
    user_canvas.tag_bind(keyboard_button, "<Button-1>", kb_only)
    
    ex1.buttons = []
    ex2.chord_buttons = []
    ex2.tonic_buttons = []
    ex3.buttons = []
    ex4.buttons = []
    ex5.chord_buttons = []
    ex5.tonic_buttons = []
    

def kb_only(event=None):
    user_canvas.delete('all')
    gen_menu_button()
    
def start(exercise):
    user_canvas.delete('all')
    gen_menu_button()
    exercise.run()
    
class GuessButton:
    def __init__(self, exercise, name, coords, func, args, text_size):
        self.name = name
        self.rect = round_rectangle(*coords, fill='#b7b7b7')
        self.centre = (((coords[0]+coords[2])/2),((coords[1]+coords[3])/2))
        self.text = user_canvas.create_text(*self.centre, text=name, font=("Times", text_size), anchor="c", fill="grey10", width=width*0.071, justify='center')
        user_canvas.tag_bind(self.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.rect, fill="#d3d3d3"))
        user_canvas.tag_bind(self.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.rect, fill="#b7b7b7"))
        if exercise == ex1:
            user_canvas.tag_bind(self.rect, "<Button-1>", lambda e: func(args))
        if exercise == ex3 or exercise == ex4:
            user_canvas.tag_bind(self.rect, "<Button-1>", lambda e: func(*args))
        self.state = False
        







class Ex1:
    def __init__(self):
        d = height/2     #Vertical Displacement
        l = w*0.078      #Square Size
        self.coords = {note_names[0]: (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                       note_names[1]: (w*0.398, h*0.6-d, w*0.398+l, h*0.6-d+l),
                       note_names[2]: (w*0.502, h*0.6-d, w*0.502+l, h*0.6-d+l),
                       note_names[3]: (w*0.605, h*0.6-d, w*0.605+l, h*0.6-d+l),
                       note_names[4]: (w*0.71, h*0.6-d, w*0.71+l, h*0.6-d+l),
                       note_names[5]: (w*0.815, h*0.6-d, w*0.815+l, h*0.6-d+l),
                       note_names[6]: (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                       note_names[7]: (w*0.398, h*0.9-d-l, w*0.398+l, h*0.9-d),
                       note_names[8]: (w*0.502, h*0.9-d-l, w*0.502+l, h*0.9-d),
                       note_names[9]: (w*0.605, h*0.9-d-l, w*0.605+l, h*0.9-d),
                       note_names[10]: (w*0.71, h*0.9-d-l, w*0.71+l, h*0.9-d),
                       note_names[11]: (w*0.815, h*0.9-d-l, w*0.815+l, h*0.9-d)}

        self.buttons = []
        self.score = 0
        self.scoreboardloc = (self.coords[note_names[11]][-2], h*0.562-d)
        self.comparators = ["c","d","e","f","g","a","b","cs","ds","fs","gs","as"] #Note Comparators
        
    def run(self, event=None):
        keyboard_canvas.create_rectangle(0, 0, width, height/2, fill='', outline='', tag='blank')
        for i, n in enumerate(note_names):
            self.buttons.append(GuessButton(self, n, self.coords[n], self.guess, self.comparators[i], 36))

        self.correct = 0
        self.iterations = 0
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        self.scoreboard = user_canvas.create_text(*self.scoreboardloc, text=self.score, font=("Times", 28), anchor="e", fill="grey10")

        self.loop()

    def guess(self, comparator, event=None):
        if comparator == self.note.name.replace("#","s").lower()[:-1]:
            self.correct += 1

        keyboard_canvas.itemconfig(self.note.key, fill='white' if self.note in white_notes else 'black')
        self.iterations += 1
        self.update_score()
        self.loop()

    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
            
    def loop(self):
        self.note = random.choice(all_notes)
        keyboard_canvas.itemconfig(self.note.key, fill='red')

















class Ex2:
    def __init__(self):
        self.tonic_buttons = []
        self.chord_buttons  = []

        l = w*0.041
        d = height/2

        l2 = w*0.084
        h2 = h*0.076
        self.coords = {"c": (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                       "d": (w*0.344, h*0.6-d, w*0.344+l, h*0.6-d+l),
                       "e": (w*0.395, h*0.6-d, w*0.395+l, h*0.6-d+l),
                       "f": (w*0.445, h*0.6-d, w*0.445+l, h*0.6-d+l),
                       "g": (w*0.497, h*0.6-d, w*0.497+l, h*0.6-d+l),
                       "a": (w*0.548, h*0.6-d, w*0.548+l, h*0.6-d+l),
                       "b": (w*0.601, h*0.6-d, w*0.601+l, h*0.6-d+l),
                       "cs": (w*0.652, h*0.6-d, w*0.652+l, h*0.6-d+l),
                       "eb": (w*0.704, h*0.6-d, w*0.704+l, h*0.6-d+l),
                       "fs": (w*0.754, h*0.6-d, w*0.754+l, h*0.6-d+l),
                       "gs": (w*0.806, h*0.6-d, w*0.806+l, h*0.6-d+l),
                       "bb": (w*0.857, h*0.6-d, w*0.857+l, h*0.6-d+l),
                       

                       "Sus2": (w*0.292, h*0.708-d, w*0.292+l2, h*0.708-d+h2),
                       "Sus4": (w*0.395, h*0.708-d, w*0.395+l2, h*0.708-d+h2),
                       "Minor Triad": (w*0.502, h*0.708-d, w*0.502+l2, h*0.708-d+h2),
                       "Major Triad": (w*0.605, h*0.708-d, w*0.605+l2, h*0.708-d+h2),
                       "Diminished Triad": (w*0.710, h*0.708-d, w*0.710+l2, h*0.708-d+h2),
                       "Augmented Triad": (w*0.815, h*0.708-d, w*0.815+l2, h*0.708-d+h2),
                       "Sixth Chord": (w*0.292, h*0.821-d, w*0.292+l2, h*0.821-d+h2),
                       "Diminished 7th": (w*0.395, h*0.821-d, w*0.395+l2, h*0.821-d+h2),
                       "Half-Diminished 7th": (w*0.502, h*0.821-d, w*0.502+l2, h*0.821-d+h2),
                       "Minor 7th": (w*0.605, h*0.821-d, w*0.605+l2, h*0.821-d+h2),
                       "Major 7th": (w*0.710, h*0.821-d, w*0.710+l2, h*0.821-d+h2),
                       "Dominant 7th": (w*0.815, h*0.821-d, w*0.815+l2, h*0.821-d+h2)}

        self.scoreboardloc = (self.coords["bb"][-2], h*0.562-d)

    def select(self, button):
        
        if button in self.tonic_buttons:
            for tonic_button in self.tonic_buttons:
                user_canvas.itemconfig(tonic_button.rect, fill='#b7b7b7')
                user_canvas.tag_bind(tonic_button.rect, "<Enter>", lambda e, b=tonic_button: user_canvas.itemconfig(b.rect, fill="#d3d3d3"))
                user_canvas.tag_bind(tonic_button.rect, "<Leave>", lambda e, b=tonic_button: user_canvas.itemconfig(b.rect, fill="#b7b7b7"))
                tonic_button.state = False
        else:
            for chord_button in self.chord_buttons:
                user_canvas.itemconfig(chord_button.rect, fill='#b7b7b7')
                user_canvas.tag_bind(chord_button.rect, "<Enter>", lambda e, b=chord_button: user_canvas.itemconfig(b.rect, fill="#d3d3d3"))
                user_canvas.tag_bind(chord_button.rect, "<Leave>", lambda e, b=chord_button: user_canvas.itemconfig(b.rect, fill="#b7b7b7"))
                chord_button.state = False

        button.state = True            
        if button.state:  #On
            user_canvas.itemconfig(button.rect, fill='#26ff4d')
            user_canvas.tag_bind(button.rect, "<Enter>", lambda e: user_canvas.itemconfig(button.rect, fill="#7cff94"))
            user_canvas.tag_bind(button.rect, "<Leave>", lambda e: user_canvas.itemconfig(button.rect, fill="#26ff4d"))
        else:   #Off
            user_canvas.itemconfig(button.rect, fill='#b7b7b7')
            user_canvas.tag_bind(button.rect, "<Enter>", lambda e: user_canvas.itemconfig(button.rect, fill="#d3d3d3"))
            user_canvas.tag_bind(button.rect, "<Leave>", lambda e: user_canvas.itemconfig(button.rect, fill="#b7b7b7"))        

        root.update()
        self.check()

    def run(self):
        keyboard_canvas.create_rectangle(0, 0, width, height/2, fill='', outline='', tag='blank')


        self.correct = 0
        self.iterations = 0
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        self.scoreboard = user_canvas.create_text(*self.scoreboardloc, text=self.score, font=("Times", 28), anchor="e", fill="grey10")

        #Tonic Buttons
        self.tonics = (tonic.replace('#', 's').lower()for tonic in note_names)
        for i, tonic in enumerate(self.tonics):
            self.tonic_buttons.append(GuessButton(self, tonic[0].upper()+tonic[1:].replace('s', '#'), self.coords[tonic], None, None, 16))            
            user_canvas.tag_bind(self.tonic_buttons[i].rect, "<Button-1>", lambda e, i=i: self.select(self.tonic_buttons[i]))         

        for i, chord in enumerate(chord_types):
            self.chord_buttons.append(GuessButton(self, chord, self.coords[chord], None, None, 14))
            user_canvas.tag_bind(self.chord_buttons[i].rect, "<Button-1>", lambda e, i=i: self.select(self.chord_buttons[i]))

        self.loop()

    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
    
    def loop(self):
        self.chord = Chord()

        for note in self.chord.notes:
            keyboard_canvas.itemconfig(note.key, fill="red")

        self.update_score()
        root.update()

        self.iterations += 1



    def check(self):
        selected = {}
        for button in self.tonic_buttons:
            if button.state == True:
                selected["tonic"] = button
        for button in self.chord_buttons:
            if button.state == True:
                selected["chord"] = button

        if len(selected) == 2:
            
            if self.chord.tonicname == selected["tonic"].name.replace("Eb","D#").replace("Bb","A#") and self.chord.type == selected["chord"].name:
                self.correct += 1
            for note in self.chord.notes:
                keyboard_canvas.itemconfig(note.key, fill='white' if note in white_notes else 'black')
                keyboard_canvas.tag_bind(note.key, "<Enter>", lambda e: user_canvas.itemconfig(note.key, fill='#d3d3d3'))
                keyboard_canvas.tag_bind(note.key, "<Leave>", lambda e: user_canvas.itemconfig(note.key, fill="#b7b7b7"))
            for k, button in selected.items():
                user_canvas.itemconfig(button.rect, fill='#b7b7b7')
                user_canvas.tag_bind(button.rect, "<Enter>", lambda e: user_canvas.itemconfig(button.rect, fill='#d3d3d3'))
                user_canvas.tag_bind(button.rect, "<Leave>", lambda e: user_canvas.itemconfig(button.rect, fill='#b7b7b7'))

                button.state = False
            self.loop()














class Ex3:
    def __init__(self):
        d = height/2     #Vertical Displacement
        l = w*0.071      #Square Size
        self.coords = {"Comp.": (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                      il[0]: (w*0.383, h*0.6-d, w*0.383+l, h*0.6-d+l),
                      il[1]: (w*0.472, h*0.6-d, w*0.472+l, h*0.6-d+l),
                      il[2]: (w*0.560, h*0.6-d, w*0.560+l, h*0.6-d+l),
                      il[3]: (w*0.650, h*0.6-d, w*0.650+l, h*0.6-d+l),
                      il[4]: (w*0.739, h*0.6-d, w*0.739+l, h*0.6-d+l),
                      il[5]: (w*0.827, h*0.6-d, w*0.827+l, h*0.6-d+l),
                      il[6]: (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                      il[7]: (w*0.383, h*0.9-d-l, w*0.383+l, h*0.9-d),
                      il[8]: (w*0.472, h*0.9-d-l, w*0.472+l, h*0.9-d),
                      il[9]: (w*0.560, h*0.9-d-l, w*0.560+l, h*0.9-d),
                      il[10]: (w*0.650, h*0.9-d-l, w*0.650+l, h*0.9-d),
                      il[11]: (w*0.739, h*0.9-d-l, w*0.739+l, h*0.9-d),
                      il[12]: (w*0.827, h*0.9-d-l, w*0.827+l, h*0.9-d)}

        self.buttons = []
        self.score = 0
        self.scoreboardloc = (self.coords[il[12]][-2], h*0.562-d)
        self.note1 = random.choice(all_notes)
        self.note2 = random.choice(all_notes)

    def toggle_compbutton_state(self):
        self.compbutton.state = not self.compbutton.state

        if self.compbutton.state:  #On
            user_canvas.itemconfig(self.compbutton.rect, fill='#26ff4d')
            user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#7cff94"))
            user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#26ff4d"))
        else:   #Off
            user_canvas.itemconfig(self.compbutton.rect, fill='#b7b7b7')
            user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#d3d3d3"))
            user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#b7b7b7"))        

        root.update()
            
    def run(self):        
        keyboard_canvas.create_rectangle(0, 0, width, height/2, fill='', outline='', tag='blank')

        self.buttons.append(GuessButton(self, "Comp.", (self.coords["Comp."]), self.toggle_compbutton_state, (), 24,))
        self.compbutton = self.buttons[0]
        
        for i, n in enumerate(il):
            self.buttons.append(GuessButton(self, n, self.coords[n], self.guess, ((interval_list[i])), 26))
        
        self.correct = 0
        self.iterations = 0
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        self.scoreboard = user_canvas.create_text(*self.scoreboardloc, text=self.score, font=("Times", 28), anchor="e", fill="grey10")
        self.loop()

    def guess(self, *args):
        self.iterations += 1
        self.user_guess = "".join(c for c in args)
        if self.interval_num <= 12:
            if self.user_guess == self.interval and self.compbutton.state == False:
                self.correct+=1
        else:
            if self.user_guess == self.interval and self.compbutton.state == True:
                self.correct+=1
            
        self.loop()
    
    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
        root.update()

    def loop(self):
        self.update_score()
        self.compbutton.state = False                           
        user_canvas.itemconfig(self.compbutton.rect, fill='#b7b7b7')
        user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#d3d3d3"))
        user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#b7b7b7"))        

        for note in (self.note1, self.note2):
            keyboard_canvas.itemconfig(note.key, fill="white" if note in white_notes else "black")

        self.note1 = random.choice(all_notes)
        self.note2 = random.choice(all_notes)
        
        self.interval_num = abs(self.note1.pos-self.note2.pos)
        if self.interval_num <= 12:
            self.interval = interval_list[self.interval_num]
        else:
            self.interval = interval_list[self.interval_num-12]
        
        keyboard_canvas.itemconfig(self.note1.key, fill="red")
        keyboard_canvas.itemconfig(self.note2.key, fill="red")

        root.update()
























class Ex4:
    def __init__(self):
        d = height/2     #Vertical Displacement
        l = w*0.071      #Square Size
        self.coords = {"Comp.": (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                      il[0]: (w*0.383, h*0.6-d, w*0.383+l, h*0.6-d+l),
                      il[1]: (w*0.472, h*0.6-d, w*0.472+l, h*0.6-d+l),
                      il[2]: (w*0.560, h*0.6-d, w*0.560+l, h*0.6-d+l),
                      il[3]: (w*0.650, h*0.6-d, w*0.650+l, h*0.6-d+l),
                      il[4]: (w*0.739, h*0.6-d, w*0.739+l, h*0.6-d+l),
                      il[5]: (w*0.827, h*0.6-d, w*0.827+l, h*0.6-d+l),
                      il[6]: (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                      il[7]: (w*0.383, h*0.9-d-l, w*0.383+l, h*0.9-d),
                      il[8]: (w*0.472, h*0.9-d-l, w*0.472+l, h*0.9-d),
                      il[9]: (w*0.560, h*0.9-d-l, w*0.560+l, h*0.9-d),
                      il[10]: (w*0.650, h*0.9-d-l, w*0.650+l, h*0.9-d),
                      il[11]: (w*0.739, h*0.9-d-l, w*0.739+l, h*0.9-d),
                      il[12]: (w*0.827, h*0.9-d-l, w*0.827+l, h*0.9-d)}

        self.buttons = []
        self.score = 0
        self.scoreboardloc = (self.coords[il[12]][-2], h*0.562-d)

    def toggle_compbutton_state(self):
        self.compbutton.state = not self.compbutton.state

        if self.compbutton.state:  #On
            user_canvas.itemconfig(self.compbutton.rect, fill='#26ff4d')
            user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#7cff94"))
            user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#26ff4d"))

        else:   #Off
            user_canvas.itemconfig(self.compbutton.rect, fill='#b7b7b7')
            user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#d3d3d3"))
            user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#b7b7b7"))        

        root.update()
            
    def run(self):        
        keyboard_canvas.create_rectangle(0, 0, width, height/2, fill='', outline='', tag='blank')
        self.buttons.append(GuessButton(self, "Comp.", (self.coords["Comp."]), self.toggle_compbutton_state, (), 24,))
        self.compbutton = self.buttons[0]
        
        for i, n in enumerate(il):
            self.buttons.append(GuessButton(self, n, self.coords[n], self.guess, ((interval_list[i])), 26))
        
        self.correct = 0
        self.iterations = 0
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        self.scoreboard = user_canvas.create_text(*self.scoreboardloc, text=self.score, font=("Times", 28), anchor="e", fill="grey10")
        self.loop()

    def guess(self, *args):
        self.iterations += 1
        self.user_guess = "".join(c for c in args)
        if self.interval_num <= 12:
            if self.user_guess == self.interval and self.compbutton.state == False:
                self.correct+=1
        else:
            if self.user_guess == self.interval and self.compbutton.state == True:
                guess = True
                self.correct+=1
            
        self.loop()
    
    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
        root.update()

    def loop(self):
        self.update_score()

        self.compbutton.state = False
        user_canvas.itemconfig(self.compbutton.rect, fill='#b7b7b7')
        user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#d3d3d3"))
        user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#b7b7b7"))        

        root.update()


        self.note1 = random.choice(all_notes)
        self.note2 = random.choice(all_notes)
        self.interval_num = abs(self.note1.pos-self.note2.pos)
        if self.interval_num <= 12:
            self.interval = interval_list[self.interval_num]
        else:
            self.interval = interval_list[self.interval_num-12]

        self.note1.play()
        self.note2.play()
        











class Ex5:
    def __init__(self):
        self.chord_buttons  = []
        d = height/2
        l = w*0.08
        self.coords = {"Sus2": (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                       "Sus4": (w*0.395, h*0.6-d, w*0.395+l, h*0.6-d+l),
                       "Minor Triad": (w*0.502, h*0.6-d, w*0.502+l, h*0.6-d+l),
                       "Major Triad": (w*0.605, h*0.6-d, w*0.605+l, h*0.6-d+l),
                       "Diminished Triad": (w*0.710, h*0.6-d, w*0.710+l, h*0.6-d+l),
                       "Augmented Triad": (w*0.815, h*0.6-d, w*0.815+l, h*0.6-d+l),
                       "Sixth Chord": (w*0.292, h*0.9-l-d, w*0.292+l, h*0.9-d),
                       "Diminished 7th": (w*0.395, h*0.9-l-d, w*0.395+l, h*0.9-d),
                       "Half-Diminished 7th": (w*0.502, h*0.9-l-d, w*0.502+l, h*0.9-d),
                       "Minor 7th": (w*0.605, h*0.9-l-d, w*0.605+l, h*0.9-d),
                       "Major 7th": (w*0.710, h*0.9-l-d, w*0.710+l, h*0.9-d),
                       "Dominant 7th": (w*0.815, h*0.9-l-d, w*0.815+l, h*0.9-d)}

        self.scoreboardloc = (self.coords["Dominant 7th"][-2], h*0.562-d)

    def select(self, button):
        if button.name == self.chord.type:
            self.correct += 1
        self.update_score()
        self.loop()

    def run(self):
        keyboard_canvas.create_rectangle(0, 0, width, height/2, fill='', outline='', tag='blank')
        self.correct = 0
        self.iterations = 0
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        self.scoreboard = user_canvas.create_text(*self.scoreboardloc, text=self.score, font=("Times", 28), anchor="e", fill="grey10")

        #Tonic Buttons
        self.tonics = (tonic.replace('#', 's').lower()for tonic in note_names)
        for i, chord in enumerate(chord_types):
            self.chord_buttons.append(GuessButton(self, chord, self.coords[chord], None, None, 14))
            user_canvas.tag_bind(self.chord_buttons[i].rect, "<Button-1>", lambda e, i=i: self.select(self.chord_buttons[i]))

        self.loop()

    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
    
    def loop(self):
        self.chord = Chord()
        self.update_score()
        root.update()
        self.iterations += 1

        for note in self.chord.notes:
            note.play()    




        
# INITIALISATION
notes = {}

if __name__ == "__main__":
    root = Tk()
##    root.attributes("-fullscreen", True)
    root.geometry("1400x1000")
    root.update()
    root.wm_title("Keyboard Trainer")

    width = w = root.winfo_width()
    height = h = root.winfo_height()
    mid = height/2
    
    keyboard_canvas = Canvas(root, width=width, height=mid, bg = "grey60", highlightthickness=0)
    keyboard_canvas.pack()

    user_canvas = Canvas(root, width=width, height=mid, bg = "grey100", highlightthickness=0)
    user_canvas.pack()

    ex1 = Ex1()
    ex2 = Ex2()
    ex3 = Ex3()
    ex4 = Ex4()
    ex5 = Ex5()
#    ex6 = Ex6()

    #Keyboard Body Dimentions
    x1 = width/10 #Top left corner
    x2 = width-x1 #Top right corner
    y1 = mid/10 
    y2 = mid-y1
    keyboard_body_height = mid*0.8
    keyboard_body_width = width*0.8

    keyboard_body = keyboard_canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    keyboard_top = keyboard_canvas.create_rectangle(x1, y1, x2, y1+keyboard_body_height*0.5, fill="grey10")


    #White Note Placement
    white_note_width = keyboard_body_width*(1/15)
    white_note_start_x1 = x1
    white_note_start_y1 = y2
    white_note_start_x2 = x1+white_note_width
    white_note_start_y2 = y1+keyboard_body_height*0.5
    
    x1 = x1
    x2 = x1+white_note_width
    y1, y2 = y2, y1+keyboard_body_height*0.5
    for whitenote in white_notes:
        whitenote.key = keyboard_canvas.create_rectangle(x1, y1, x2, y2, fill="white", tag=whitenote.name)
        keyboard_canvas.tag_bind(whitenote.name, "<Enter>", lambda e, key=whitenote.key: keyboard_canvas.itemconfig(key, fill="#d3d3d3"))
        keyboard_canvas.tag_bind(whitenote.name, "<Leave>", lambda e, key=whitenote.key: keyboard_canvas.itemconfig(key, fill="white"))
        keyboard_canvas.tag_bind(whitenote.name, "<ButtonPress-1>", whitenote.play)
        x1, x2 = x2, x2+white_note_width


    #Black Note Placement
    black_note_width = white_note_width*0.5
    x1 = white_note_start_x1+white_note_width*0.75
    x2 = x1+black_note_width
    y1 = white_note_start_y2
    y2 = white_note_start_y1+((white_note_start_y2-white_note_start_y1)/2.15)
    
    m = (0,1,3,4,5,7,8,10,11,12)
    i=0
    for blacknote in black_notes:
        blacknote.key = keyboard_canvas.create_rectangle(x1+(m[i]*white_note_width), y1, x2+(m[i]*white_note_width), y2, fill="black", tag=blacknote.name)
        keyboard_canvas.tag_bind(blacknote.name, "<Enter>", lambda e, key=blacknote.key: keyboard_canvas.itemconfig(key, fill="grey20"))
        keyboard_canvas.tag_bind(blacknote.name, "<Leave>", lambda e, key=blacknote.key: keyboard_canvas.itemconfig(key, fill="black"))
        keyboard_canvas.tag_bind(blacknote.name, "<ButtonPress-1>", blacknote.play)
        i += 1


    #Changing mode functions
    def set_mode0(event=None):  # Changes playback mode. 0 = Piano, 1 = Beep
        global mode
        mode = 0
        keyboard_canvas.itemconfig(mode0, fill="#099bf4")
        keyboard_canvas.itemconfig(mode1, fill="#b4b4b4")

    def set_mode1(event=None):  # Changes playback mode. 0 = Piano, 1 = Beep
        global mode
        mode = 1
        keyboard_canvas.itemconfig(mode1, fill="#099bf4")
        keyboard_canvas.itemconfig(mode0, fill="#b4b4b4")        

    #Mode button placement
    x1 = width/7.25
    y1 = (mid/10+keyboard_body_height*0.5) - height/10
    w = width/26

    mode0 = keyboard_canvas.create_rectangle(x1,y1,x1+w, y1+w,fill="#099bf4")
    x1 = x1+(w*1.2)
    mode1 = keyboard_canvas.create_rectangle(x1,y1,x1+w, y1+w,fill="#b4b4b4")

    keyboard_canvas.tag_bind(mode0, "<ButtonPress-1>", set_mode0)
    keyboard_canvas.tag_bind(mode1, "<ButtonPress-1>", set_mode1)

    #Text Placement
    x = width-(width/10)
    y = (mid-mid/10)-(keyboard_body_height*0.5)
    xpad = -(width/50)
    ypad = -(height/50)
    font = tkFont.Font(family='Athelas', size=70, slant='italic')
    text = keyboard_canvas.create_text(x+xpad, y+ypad,text="Keyboard Trainer", font=font, fill="#099bf4", anchor="se")

    main_menu()
    
    
    root.mainloop()
