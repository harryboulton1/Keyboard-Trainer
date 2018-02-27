from keys import *


def round_rectangle1(user_canvas, x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return user_canvas.create_polygon(points, **kwargs, smooth=True)

def start(exercise, gen_menu_button, event=None):
        exercise.user_canvas.delete('all')
        gen_menu_button()
        exercise.run(exercise)
        
class GuessButton:
    def __init__(self, name, coords, user_canvas):
        self.name = name
        self.coords = coords
        self.rect = round_rectangle1(user_canvas, *self.coords, fill='#b7b7b7')
        self.centre = (((self.coords[0]+self.coords[2])/2),((self.coords[1]+self.coords[3])/2))
        self.text = user_canvas.create_text(*self.centre, text=self.name, font=("Times", 36), anchor="c", fill="grey10")
        user_canvas.tag_bind(self.rect, "<Enter>", lambda e: user_canvas.itemconfig(self.rect, fill="#d3d3d3"))
        user_canvas.tag_bind(self.rect, "<Leave>", lambda e: user_canvas.itemconfig(self.rect, fill="#b7b7b7"))
        user_canvas.tag_bind(self.rect, "<Button-1>", lambda e: guess(comparator))

class Exercise:
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        self.keyboard_canvas = keyboard_canvas
        self.user_canvas = user_canvas
        self.width = width
        self.height = height

 
class Ex1(Exercise):
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        super().__init__(keyboard_canvas, user_canvas, width, height)

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

    def run(ex1, event=None):

        def guess(comparator, event=None):
            global correct, iterations
            if comparator == note.name.replace("#","s").lower()[:-1]:
                correct += 1

            keyboard_canvas.itemconfig(note.key, fill='white' if note in white_notes else 'black')

            iterations += 1
            update_score()
            cont()

        
 


        #Scoreboard
        correct = 0
        iterations = 0
        score = "Score:  "+str(correct)+" / "+str(iterations)
        scoreboard = user_canvas.create_text(ex1_coords[nn[11]][-2], h*0.562-d, text=score, font=("Times", 28), anchor="e", fill="grey10")

        def update_score():
            global score
            score = "Score:  "+str(correct)+" / "+str(iterations)
            user_canvas.itemconfig(scoreboard, text=score)

        #Exercise start
        def cont():
            global note
            note = random.choice(all_notes)                           
            keyboard_canvas.itemconfig(note.key, fill='red')

        cont()


class Ex2(Exercise):
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        super().__init__(keyboard_canvas, user_canvas, width, height)

    def run():
        pass

class Ex3(Exercise):
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        super().__init__(keyboard_canvas, user_canvas, width, height)

class Ex4(Exercise):
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        super().__init__(keyboard_canvas, user_canvas, width, height)

class Ex5(Exercise):
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        super().__init__(keyboard_canvas, user_canvas, width, height)

class Ex6(Exercise):
    def __init__(self, keyboard_canvas, user_canvas, width, height):
        super().__init__(keyboard_canvas, user_canvas, width, height)

