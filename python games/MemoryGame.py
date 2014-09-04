# implementation of card game - Memory

import simplegui
import random

deck = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
exposed = []
for n in range(0, 16):
    exposed.append(False)

# helper function to initialize globals
def new_game():
    global state, counter, a, b
    state = 0
    a = 0
    b = 0
    counter = 0
    random.shuffle(deck)
    for n in range(0,16):
        exposed[n] = False
    label.set_text("Turns: 0")
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, deck, a, b, counter
    n = pos[0] // 50
    if exposed[n] == False:
        #exposed[n] = not exposed[n]
        if state == 0: 
            exposed[n] = True
            a = n
            state = 1 
        elif state == 1:
            exposed[n] = True
            counter += 1
            label.set_text("Turns: " + str(counter))
            b = n
            state = 2      
        else:     
            if deck[a] != deck[b]:
                exposed[a] = False
                exposed[b] = False
            exposed[n] = True
            a = n
            state = 1
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, pos, counter
    pos = 0  
   
    for card in range((len(deck))):       
        if exposed[card]:
            canvas.draw_text(str(deck[card]), (pos + 15,60), 50, "White")
            pos += 50     
        else: 
            canvas.draw_line((pos + 25,0), (pos + 25, 100), 50, "Green")
            canvas.draw_line((pos ,0), (pos , 100), 2, "White")
            pos += 50
                       
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
print deck


# Always remember to review the grading rubric