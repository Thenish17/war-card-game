import random,itertools, tkinter
deck = list(itertools.product(range(2,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
player_one = []
player_two = []
for i in range(len(deck)):
    if i % 2 == 0:
        player_one.append(deck[i])
    else:
        player_two.append(deck[i])
print(player_one)
print("-----------------------------------------------------------------------------------------------------------------------------------")
print(player_two)

def remove_top_card():
    player_one.pop(0)
    player_two.pop(0)
def war():
    try:
        for i in range(3):
            remove_top_card()
    except IndexError:
        if len(player_one) > len(player_two):
            print("player one winds")
            exit()
        else:
            print("player two winds ")
            exit()
    compare_top_card()
def winner_takes(player):
    if player == "player_one":
        player_one.append(player_one[0])
        player_one.append(player_two[0])
    if player == "player_two":
        player_two.append(player_two[0])
        player_two.append(player_one[0])

def compare_top_card():
    if len(player_one) == 0:
        print("player one wins the game")
        exit()
    if len(player_two) == 0:
        print("player two wins")
        exit()
    print("len of one " + str(len(player_one)))
    print("len of two" + str(len(player_two)))
    print ("_-----------------------------------------------------------------------------------")
    print(player_one)
    print(player_two)
    print ("_-----------------------------------------------------------------------------------")
    if player_one[0][0] > player_two[0][0]:
        print("player one wins")
        winner_takes("player_one")
        remove_top_card()
    elif player_one[0][0] == player_two[0][0]:
        print("----------------------------------------------------------------------")
        print("war")
        
        war()
        print ("_-----------------------------------------------------------------------------------")
    else:
        winner_takes("player_two")
        print("player two wins")
        remove_top_card()
        



root = tkinter.Tk()
screen = tkinter.Canvas(root,width=700 , height= 700, bg= 'white')
next_button = tkinter.Button(root, text="next", command= compare_top_card)

next_button.pack()


root.mainloop()