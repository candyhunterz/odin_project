# Mini-project #6 - Blackjack

import simplegui
import random
import math
# load card sprite - 949x392 - source: jfitz.com
sound1 = simplegui.load_sound("https://www.dropbox.com/s/gpxm5lork4634cs/soundcoin.mp3?dl=1")
sound2 = simplegui.load_sound("https://www.dropbox.com/s/xk4bcyw5h5lh3nz/drwa1.mp3?dl=1")
play_sound2 = []
WIDTH_SCREEN  = 1024
HEIGHT_SCREEN = 700
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
Deck_image = simplegui.load_image("https://www.dropbox.com/s/wblurd2icoik8mf/table.png?dl=1")
DECK_SIZE = (1019,703)
DECK_SIZE_CENTER = (509.5,351.5)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
MOVE_WIDTH = []
MOVE_HEIGHT = []
ROTATE = []
FLIPS = []
ANIMATION = 30
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    
pos_player = [100,430]
pos_computer = [100,100]
pos_deck = [900,50]
pos_text = []
size_text = 30
#image coin
list_coin = []
Coin10 = simplegui.load_image("https://www.dropbox.com/s/onjcxv9w3mxpxpf/Coin10s.png?dl=1")
Coin10s = simplegui.load_image("https://www.dropbox.com/s/quv6b7zp5kk4hob/coin10s1.png?dl=1")
Coin20 = simplegui.load_image("https://www.dropbox.com/s/xhzohu0rrxheanc/coin20.png?dl=1")
Coin20s = simplegui.load_image("https://www.dropbox.com/s/c0tzlk9cuj7n55q/coin20s.png?dl=1")
Coin50 = simplegui.load_image("https://www.dropbox.com/s/56r2uwwquswwz15/coin50.png?dl=1")
Coin50s = simplegui.load_image("https://www.dropbox.com/s/it4c7dk6skndhq7/coin50s.png?dl=1")
Coin100 = simplegui.load_image("https://www.dropbox.com/s/har69v9re3l71dw/Coin100.png?dl=1")
Coin100s = simplegui.load_image("https://www.dropbox.com/s/tyxpix677cwass7/Coin100s.png?dl=1")
list_coin_hand = [Coin10 ,Coin20,Coin50,Coin100]
list_pos = [[800,620],[850,600],[900,580],[950,560]]
SIZE_COIN = [251,258]
SIZE_COIN_CENTER = [251/2,258/2] 
COIN_SIZE_DECK = [40,40]

# initialize some useful global variables
money_player = 100
money_use = 0
in_play = False
player = {}
computer = {}
text = "Hit or Stand ?"
win = ""
nextt = 0
save_index_player = 0
save_index_computer = 0
check = []
increase = 0
save = None
start = False
'''------------------------------ '''

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0]
        ,pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def draw_animation(self,canvas,pos,i,face,image_check):
        if image_check:
            card = card_images
            location = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        else:
            card = card_back
            location = CARD_BACK_CENTER
        canvas.draw_image(card,location
                    ,CARD_BACK_SIZE,[i*100+pos[0]+CARD_CENTER[0],pos[1]
                    +CARD_CENTER[1]],
                    (CARD_SIZE[0]-face,CARD_SIZE[1]))
    
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand  = []
        self.move  = []
        self.frame = []
        self.score = []
    def __str__(self):
        pass	# return a string representation of a hand
        
    def add_card(self,deck):
        # add a card object to a hand
        self.hand.append(deck)
        self.move.append(True)
        self.frame.append(0)
        self.score.append(0)
        for i in range(len(self.hand)):
            print self.hand[i].get_suit(),self.hand[i].get_rank()
    
    def get_value(self):
        Sum = 0
        count = 0
        for i in range(len(self.hand)):
            if VALUES[self.hand[i].get_rank()] == 1:
                count+=1
            else:
                Sum+=VALUES[self.hand[i].get_rank()]
        if count == 1 and Sum+11 <= 21:
             Sum+=11
        elif count == 1 and Sum+11 > 21:
            Sum+=1
            
        return Sum
        # count aces as f the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
    def get_length(self):
        return len(self.hand)
    
    def set_move(self,index,values):
        self.move[index] = values
        
    def get_move(self,index):
        return self.move[index]
    def draw_animation(self,canvas,pos,index,save_index,in_play = False):
        global sound2
        if play_sound2[index]:
            sound2.play()
            play_sound2[index] = False
        if self.move[save_index] is True:
            
            if self.frame[save_index] < ANIMATION - 1:
                
                self.frame[save_index]+=1
                move_width   = MOVE_WIDTH[index][self.frame[save_index]]
                move_height  = MOVE_HEIGHT[index][self.frame[save_index]]
                rotate 		 = ROTATE[index][self.frame[save_index]]
                canvas.draw_image(card_back,CARD_BACK_CENTER
                ,CARD_BACK_SIZE,[pos_deck[0] - move_width + CARD_BACK_CENTER[0],pos_deck[1] + move_height
                +CARD_BACK_CENTER[1]],CARD_BACK_SIZE,math.radians(rotate))
            elif self.frame[save_index] >= ANIMATION - 1 and not in_play:
                self.draw_flip(canvas,pos,save_index)
            else:
                self.move[save_index] = False
            
    def draw_flip(self,canvas,pos,save_index):
        
        if self.score[save_index] < ANIMATION - 1:
            self.score[save_index]+=1
            face = FLIPS[self.score[save_index]]   
            if self.score[save_index] < ANIMATION/2:
                self.hand[save_index].draw_animation(canvas,pos,save_index,face,False)
            else:
                self.hand[save_index].draw_animation(canvas,pos,save_index,face,True)
            if self.score[save_index] >= ANIMATION - 1:
                self.move[save_index] = False 
                
                
    def draw(self,canvas,pos,in_play = False):
         for i in range(len(self.hand)):
             if not self.move[i]:   
                if in_play and i == 0:
                    canvas.draw_image(card_back,CARD_BACK_CENTER,
                       CARD_BACK_SIZE,[i*pos[0]+100+CARD_BACK_CENTER[0],
                                            pos[1]+CARD_BACK_CENTER[1]],
                          CARD_BACK_SIZE)
                else:
                    self.hand[i].draw(canvas,[i*pos[0]+100,pos[1]])# draw a hand on the canvas, use the draw method for cards
                

        
# define deck class 
class Deck:
    def __init__(self):
        pass	# create a Deck object
        self.deck = []
        
    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        global text
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                card = Card(SUITS[i],RANKS[j])
                self.deck.append(card)
        random.shuffle(self.deck)
    
    def deal_card(self):
        # deal a card object from the deck
        card = self.deck.pop()
        return card
    
    def drawdeck(self,canvas):
        for i in range(len(self.deck)):
            canvas.draw_image(card_back,CARD_BACK_CENTER\
                              ,CARD_BACK_SIZE,(pos_deck[0]-i/10+CARD_BACK_CENTER[0],
                              pos_deck[1]-i/10+CARD_BACK_CENTER[1]),CARD_BACK_SIZE)
    def __str__(self):
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    
    global nextt,in_play,player,computer,text,win
    global MOVE_WIDTH,MOVE_HEIGHT,ROTATE,check,money_player
    global save_index_player,save_index_computer,list_coin,money_use,play_sound2
    global deck,player,computer
    if start:
        deck = Deck()
        player = Hand()
        computer = Hand()
        text = "Hit or Stand ?"
        win = ""
        nextt,save_index_player,save_index_computer,money_use = 0,0,0,0
        deck.shuffle()
        
        MOVE_WIDTH,MOVE_HEIGHT,ROTATE,check,list_coin,play_sound2 = [],[],[],[],[],[]
        for i in range(2):
            player.add_card(deck.deal_card())
            animation(i,True)
            computer.add_card(deck.deal_card())
            animation(i,False)
        in_play = True
        if player.get_value()==21 :
            money_player+=money_use 
            in_play = False
        
def hit():
    # replace with your code below
    global computer,player,deck,in_play,win,text,money_player
    if in_play:
        animation(player.get_length(),True)
        player.add_card(deck.deal_card())
    
        if player.get_value()==21 :
            print "Score 21 , Player Win "
            win = "You Win."
            money_player+=money_use
            in_play = False
            text = "New Deal ?"
            computer.set_move(0,True)
        elif player.get_value()>21 :
            print "Bust , your score is " + str(player.get_value())
            in_play = False
            win = "You Lose."
            money_player-=money_use
            text = "New Deal ?"
            computer.set_move(0,True)
            
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global in_play,computer,deck,in_play,text,win,money_player
    if in_play:
        while computer.get_value() < 17:
            animation(computer.get_length(),False)
            computer.add_card(deck.deal_card())
        
        if computer.get_value() > 21:
            print "computer Busted"
            win = "You Win."
            money_player+=money_use
        else:
            if computer.get_value() > player.get_value() :
                print "computer win"
                win = "You Lose."
                money_player-=money_use
            elif computer.get_value() == player.get_value():
                win = "Push."
            else:
                print "Player win"
                win = "You Win."
                money_player+=money_use
        text = "New Deal ?"
        in_play = False
        computer.set_move(0,True)
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
def start():
    global start,money_use
    if money_use>0:
        start = True
# draw handler    
def draw(canvas):
    global save,core,nextt,in_play,save_index_player,save_index_computer
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_image(Deck_image,DECK_SIZE_CENTER
                ,DECK_SIZE,[WIDTH_SCREEN/2,HEIGHT_SCREEN/2],
                [WIDTH_SCREEN,HEIGHT_SCREEN])
    for i in range(4):
        canvas.draw_image(list_coin_hand[i],SIZE_COIN_CENTER
                ,SIZE_COIN,list_pos[i],
                COIN_SIZE_DECK)
    
    for i in range(len(list_coin)):
        canvas.draw_image(list_coin[i],SIZE_COIN_CENTER
                ,SIZE_COIN,[850+i*6,390+i*4],
                [50,50])
   
    #[800,620],[850,600],[900,580],
    deck.drawdeck(canvas)
    canvas.draw_text("Blackjack",[WIDTH_SCREEN/2-HEIGHT_SCREEN/10,HEIGHT_SCREEN/20],size_text*1.5, "Aqua", "serif")
    if start:
        if nextt < player.get_length()+computer.get_length():
        
            if save_index_player < player.get_length() and player.move[save_index_player] and check[nextt]:
                player.draw_animation(canvas,pos_player,nextt,save_index_player)
                save = True
            
            elif save_index_computer < computer.get_length() and computer.move[save_index_computer] and not check[nextt] :
                if save_index_computer == 0:
                    computer.draw_animation(canvas,pos_computer,nextt,save_index_computer,in_play)
                else:    
                    computer.draw_animation(canvas,pos_computer,nextt,save_index_computer)
                save = False
            else:
                if save :
                    save_index_player+=1
                
                else :
                    save_index_computer+=1
                
                nextt+=1
            
    if not in_play :
        
        computer.draw_flip(canvas,pos_computer,0)
        
    player.draw(canvas,pos_player)
    canvas.draw_text("Player", (pos_player[0],pos_player[1]-30),size_text, "Black", "serif")
    canvas.draw_text(text,(pos_player[0]+100,pos_player[1]-30), size_text, "Black", "serif")
    computer.draw(canvas,pos_computer,in_play)
    canvas.draw_text("Dealer", (pos_computer[0],pos_computer[1]-30),size_text, "Black", "serif")
    canvas.draw_text(win,(pos_computer[0]+100,pos_computer[1]-30),size_text, "Black", "serif")
    canvas.draw_text("Your Money : " + str(money_player) +" $",(370,580),size_text*1.2, "Red", "serif")

# function animation for Deck and Card

def animation(length,p):
    global MOVE_WIDTH,MOVE_HEIGHT,ROTATE,check,play_sound2
    l1,l2,l3 = [],[],[]
    height = pos_player[1] if p else pos_computer[1]
    
    for i in range(ANIMATION):
        move_width = int(((pos_deck[0]-(length*100+100))/ANIMATION ) * (i+1))
        move_height = int(((height - pos_deck[1] )/ANIMATION ) * (i+1))
        rotate = (i+1)*9
        l1.append(move_width)
        l2.append(move_height)
        l3.append(rotate)
    play_sound2.append(True)
    MOVE_WIDTH.append(l1)
    MOVE_HEIGHT.append(l2)
    ROTATE.append(l3)
    check.append(p)
    
    
def flip_up():
    global FLIPS
    for i in range(ANIMATION):
        if i < ANIMATION / 2:
            card = int((CARD_SIZE[0] / ANIMATION * 2) * i + 1)
        elif i >= ANIMATION / 2:
            card = CARD_SIZE[0] - int((CARD_SIZE[0] / ANIMATION * 2) * (i + 1 - ANIMATION / 2))
        FLIPS.append(card) 

# mouse click handler event        
def distance_coin(pos1,pos2):
    return math.sqrt( (pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

def mouse_click(pos):
    global money_use,list_coin
    if in_play:
        if money_use<100 and money_use<money_player:
            sound1.play()
            if distance_coin(list_pos[0],pos) < 20 and money_use+10<=money_player:
                list_coin.append(Coin10s)
                money_use +=10
            elif distance_coin(list_pos[1],pos) < 20 and money_use+10<=money_player:
                list_coin.append(Coin20s)
                money_use +=20
            elif distance_coin(list_pos[2],pos) < 20 and money_use+50<=money_player:
                list_coin.append(Coin50s)
                money_use +=50
            elif distance_coin(list_pos[3],pos) < 20 and money_use+100<=money_player:
                list_coin.append(Coin100s)
                money_use +=100
                
deck = None
player = None
computer = None
# initialization frame
frame = simplegui.create_frame("Blackjack",WIDTH_SCREEN,HEIGHT_SCREEN)
frame.set_canvas_background("Green")
#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
#frame.add_button("Start", stand, 200)
frame.set_mouseclick_handler(mouse_click)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
deal()
flip_up()
# remember to review the gradic rubric
