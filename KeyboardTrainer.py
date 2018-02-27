from tkinter import *
import tkinter.font as tkFont
import time, random
from keys import *

def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return user_canvas.create_polygon(points, **kwargs, smooth=True)

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
    user_canvas.tag_bind(ex2_button, "<Button-1>", lambda e: start(ex2, gen_menu_button))

    x1 = x2+(width*0.008)
    y1 = y1
    x2 = width*0.9
    y2 = y2
    ex3_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex3_text = user_canvas.create_text(width*0.82, (height*0.671)-d, text="Exercise 3", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex3_button, "<Enter>", lambda e: user_canvas.itemconfig(ex3_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex3_button, "<Leave>", lambda e: user_canvas.itemconfig(ex3_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex3_button, "<Button-1>", lambda e: start(ex3, gen_menu_button))

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
    user_canvas.tag_bind(ex5_button, "<Button-1>", lambda e: start(ex5, gen_menu_button))

    x1 = x2+(width*0.008)
    y1 = y1
    x2 = width*0.9
    y2 = y2
    ex6_button = round_rectangle(x1,y1,x2,y2, fill="#b7b7b7")
    ex6_text = user_canvas.create_text(width*0.82, (height*0.827)-d, text="Exercise 6", font=("Nueva Std", 28), anchor="c", fill="grey10")
    user_canvas.tag_bind(ex6_button, "<Enter>", lambda e: user_canvas.itemconfig(ex6_button, fill="#d3d3d3"))
    user_canvas.tag_bind(ex6_button, "<Leave>", lambda e: user_canvas.itemconfig(ex6_button, fill="#b7b7b7"))
    user_canvas.tag_bind(ex6_button, "<Button-1>", lambda e: start(ex6, gen_menu_button))

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
    
    ex4.buttons = []

def kb_only(event=None):
    user_canvas.delete('all')
    gen_menu_button()
    
def start(exercise):
    user_canvas.delete('all')
    gen_menu_button()
    exercise.run()
    
class GuessButton:
    def __init__(self, exercise, name, coords, func, args, text_size):
        self.rect = round_rectangle(*coords, fill='#b7b7b7')
        self.centre = (((coords[0]+coords[2])/2),((coords[1]+coords[3])/2))
        self.text = user_canvas.create_text(*self.centre, text=name, font=("Times", text_size), anchor="c", fill="grey10", width=width*0.071, justify='center')
        user_canvas.tag_bind(self.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.rect, fill="#d3d3d3"))
        user_canvas.tag_bind(self.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.rect, fill="#b7b7b7"))
        if exercise == ex1:
            user_canvas.tag_bind(self.rect, "<Button-1>", lambda e: func(args))
        if exercise == ex4:
            user_canvas.tag_bind(self.rect, "<Button-1>", lambda e: func(*args))

        

#        user_canvas.tag_bind(self.rect, "<Button-1>", lambda e: some_fucntiion))

#        GuessButton(self, name, coords, comaprator, some_function(args))

class Ex1:
    def __init__(self):
        self.name = "Exercise 1"
        self.buttons = []

        w = width        #Screen Width
        h = height       #Screen Height
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

        self.cont()

    def guess(self, comparator, event=None):
        print(comparator, self.note.name, self.note.name.replace("#","s").lower()[:-1])
        if comparator == self.note.name.replace("#","s").lower()[:-1]:
            self.correct += 1

        keyboard_canvas.itemconfig(self.note.key, fill='white' if self.note in white_notes else 'black')
        self.iterations += 1
        self.update_score()
        self.cont()

    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
            
    def cont(self):
        self.note = random.choice(all_notes)
        keyboard_canvas.itemconfig(self.note.key, fill='red')

class Ex4:
    def __init__(self):
        self.name = "Exercise 4"
        self.coords = []
        self.buttons = []
        self.note1 = self.note2 = None
        self.score = 0
        self.interval_list = ["Unison",
                              "Minor 2nd",
                              "Major 2nd",
                              "Minor 3rd",
                              "Major 3rd",
                              "Perfect 4th",
                              "Tritone",
                              "Perfect 5th",
                              "Minor 6th",
                              "Major 6th",
                              "Minor 7th",
                              "Major 7th",
                              "Octave"]
        
        self.il = self.interval_list

        w = width        #Screen Width
        h = height       #Screen Height
        d = height/2     #Vertical Displacement
        l = w*0.071      #Square Size
        363-292
        self.coords = {"Comp.": (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                      self.il[0]: (w*0.383, h*0.6-d, w*0.383+l, h*0.6-d+l),
                      self.il[1]: (w*0.472, h*0.6-d, w*0.472+l, h*0.6-d+l),
                      self.il[2]: (w*0.560, h*0.6-d, w*0.560+l, h*0.6-d+l),
                      self.il[3]: (w*0.650, h*0.6-d, w*0.650+l, h*0.6-d+l),
                      self.il[4]: (w*0.739, h*0.6-d, w*0.739+l, h*0.6-d+l),
                      self.il[5]: (w*0.827, h*0.6-d, w*0.827+l, h*0.6-d+l),
                      self.il[6]: (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                      self.il[7]: (w*0.383, h*0.9-d-l, w*0.383+l, h*0.9-d),
                      self.il[8]: (w*0.472, h*0.9-d-l, w*0.472+l, h*0.9-d),
                      self.il[9]: (w*0.560, h*0.9-d-l, w*0.560+l, h*0.9-d),
                      self.il[10]: (w*0.650, h*0.9-d-l, w*0.650+l, h*0.9-d),
                      self.il[11]: (w*0.739, h*0.9-d-l, w*0.739+l, h*0.9-d),
                      self.il[12]: (w*0.827, h*0.9-d-l, w*0.827+l, h*0.9-d)}

        self.scoreboardloc = (self.coords[self.il[12]][-2], h*0.562-d)
        self.compbutton_state = False

    def toggle_compbutton_state(self):
        self.compbutton_state = not self.compbutton_state

        if self.compbutton_state:  #On
            user_canvas.itemconfig(self.compbutton.rect, fill='#26ff4d')
            user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#7cff94"))
            user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#26ff4d"))

        else:   #Off
            user_canvas.itemconfig(self.compbutton.rect, fill='#b7b7b7')
            user_canvas.tag_bind(self.compbutton.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#d3d3d3"))
            user_canvas.tag_bind(self.compbutton.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.compbutton.rect, fill="#b7b7b7"))        

        root.update()
        
        print(self.compbutton_state) ########=-=-=-=-=-=-=-=-=
        
    def run(self):        
        keyboard_canvas.create_rectangle(0, 0, width, height/2, fill='', outline='', tag='blank')
        self.buttons.append(GuessButton(self, "Comp.", (self.coords["Comp."]), self.toggle_compbutton_state, (), 24,))
        self.compbutton = self.buttons[0]
        
        for i, n in enumerate(self.il):
            self.buttons.append(GuessButton(self, n, self.coords[n], self.guess, ((self.interval_list[i])), 26))
        
        self.correct = 0
        self.iterations = 0
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        self.scoreboard = user_canvas.create_text(*self.scoreboardloc, text=self.score, font=("Times", 28), anchor="e", fill="grey10")
        self.cont()

    def guess(self, *args):
        self.iterations += 1
        self.user_guess = "".join(c for c in args)
        if self.interval_num <= 12:
            if self.user_guess == self.interval and self.compbutton_state == False:
                self.user_guess = True
                self.correct+=1
        else:
            if self.user_guess == self.interval and self.compbutton_state == True:
                guess = True
                self.correct+=1
            
        self.cont()
    
    def update_score(self):
        self.score = "Score:  "+str(self.correct)+" / "+str(self.iterations)
        user_canvas.itemconfig(self.scoreboard, text=self.score)
        root.update()

    def cont(self):
        self.update_score()
        user_canvas.itemconfig(self.buttons[0].rect, fill='#b7b7b7')
        root.update()

        self.compbutton_state = False

        self.note1, self.note2 = random.sample(all_notes, 2)
        self.interval_num = abs(self.note1.pos-self.note2.pos)
        if self.interval_num <= 12:
            self.interval = self.interval_list[self.interval_num]
        else:
            self.interval = self.interval_list[self.interval_num-12]

        self.note1.play()
        self.note2.play()
        
def run(exercise):
    exercise.run()

# INITIALISATION
notes = {}

if __name__ == "__main__":
    root = Tk()
    root.attributes("-fullscreen", True)
    root.update()
    root.wm_title("Keyboard Trainer")

    width = root.winfo_width()
    height = root.winfo_height()
    mid = height/2
    
    keyboard_canvas = Canvas(root, width=width, height=mid, bg = "grey60", highlightthickness=0)
    keyboard_canvas.pack()

    user_canvas = Canvas(root, width=width, height=mid, bg = "grey100", highlightthickness=0)
    user_canvas.pack()

    ex1 = Ex1()
    ex4 = Ex4()
##    ex2 = Ex2()
##    ex3 = Ex3()
##    ex4 = Ex4()
##    ex5 = Ex5()
##    ex6 = Ex6()

    
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
        keyboard_canvas.tag_bind(whitenote.name, "<ButtonPress-1>", whitenote.press)
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
        keyboard_canvas.tag_bind(blacknote.name, "<ButtonPress-1>", blacknote.press)
        i += 1


    #Changing mode functions
    mode = 0
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
