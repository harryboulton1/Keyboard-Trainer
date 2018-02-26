from keys import *

def start(exercise, gen_menu_button, event=None):
        exercise.user_canvas.delete('all')
        gen_menu_button()
        exercise.run()
        
class Exercise:
    def __init__(self, keyboard_canvas, user_canvas):
        self.keyboard_canvas = keyboard_canvas
        self.user_canvas = user_canvas

class Ex1(Exercise):
    def __init__(self, keyboard_canvas, user_canvas):
        super().__init__(keyboard_canvas, user_canvas)

    def run():

class Ex2(Exercise):
    def __init__(self, keyboard_canvas, user_canvas):
        super().__init__(keyboard_canvas, user_canvas)

    def run():

class Ex3(Exercise):
    def __init__(self, keyboard_canvas, user_canvas):
        super().__init__(keyboard_canvas, user_canvas)

class Ex4(Exercise):
    def __init__(self, keyboard_canvas, user_canvas):
        super().__init__(keyboard_canvas, user_canvas)

class Ex5(Exercise):
    def __init__(self, keyboard_canvas, user_canvas):
        super().__init__(keyboard_canvas, user_canvas)

class Ex6(Exercise):
    def __init__(self, keyboard_canvas, user_canvas):
        super().__init__(keyboard_canvas, user_canvas)

    def run()

    



    

####ex2 = Ex2()
##ex3 = Ex3()
##ex4 = Ex4()
##ex5 = Ex5()
##ex6 = Ex6()


def ex1(event=None):
    global correct, iterations, score, note
    user_canvas.delete('all')
    gen_menu_button()
        
    #Button Creation
    ex1_buttons = [] #Note Buttons
    nn = ["C","D","E","F","G","A","B","C#","Eb","F#","G#","Bb"] #Note Names
    comparators = ["c","d","e","f","g","a","b","cs","ds","fs","gs","as"] #Note Comparators

    w = width        #Screen Width
    h = height       #Screen Height
    d = height/2     #Vertical Displacement
    l = w*0.078      #Square Size
    ex1_coords = {nn[0]: (w*0.292, h*0.6-d, w*0.292+l, h*0.6-d+l),
                  nn[1]: (w*0.398, h*0.6-d, w*0.398+l, h*0.6-d+l),
                  nn[2]: (w*0.502, h*0.6-d, w*0.502+l, h*0.6-d+l),
                  nn[3]: (w*0.605, h*0.6-d, w*0.605+l, h*0.6-d+l),
                  nn[4]: (w*0.71, h*0.6-d, w*0.71+l, h*0.6-d+l),
                  nn[5]: (w*0.815, h*0.6-d, w*0.815+l, h*0.6-d+l),
                  nn[6]: (w*0.292, h*0.9-d-l, w*0.292+l, h*0.9-d),
                  nn[7]: (w*0.398, h*0.9-d-l, w*0.398+l, h*0.9-d),
                  nn[8]: (w*0.502, h*0.9-d-l, w*0.502+l, h*0.9-d),
                  nn[9]: (w*0.605, h*0.9-d-l, w*0.605+l, h*0.9-d),
                  nn[10]: (w*0.71, h*0.9-d-l, w*0.71+l, h*0.9-d),
                  nn[11]: (w*0.815, h*0.9-d-l, w*0.815+l, h*0.9-d)}

    def guess(comparator, event=None):
        global correct, iterations
        if comparator == note.name.replace("#","s").lower()[:-1]:
            correct += 1

        keyboard_canvas.itemconfig(note.key, fill='white' if note in white_notes else 'black')

        iterations += 1
        update_score()
        cont()

    
    i = 0
    for n in nn:
        ex1_buttons.append(CanvasButton(n, comparators[i]))
        i +=1


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
    
