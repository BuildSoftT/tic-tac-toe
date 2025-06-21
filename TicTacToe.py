from tkinter import *
from tkinter import font
# Root is just variable name. Tk() creates main application window
root = Tk()
# Title of the window
root.title("Tic-Tac-Toe Game")
# size of the window
root.geometry("600x600")

"""
Tic-Tac-Toe Board:
-----column----
|    0  1  2
row  3  4  5
|    6  7  8

(Numbers represents buttons below)
Note, there should be no alphanumeric character on the button unless button is clicked. It should display 'O' or 'X' ONLY.
"""
# Initially empty list, but should have in order: [0,1,2,3,4,5,6,7,8]; True False only at each of these locations and tracks whether the button was clicked for each player.
P1button_List = []
P2button_List = []
# It is player 1's turn by default
Player1 = True
# keep track of button's index
index = 0
# Keep track of how many buttons were pressed
count = 0
# Initialize buttons and button lists with false values as default.
# 200 x 200 pixel button created & placed at column x row
# Multiply row and column by 200 due to size of button. Top-Left corner is the position of the button.
for row in range(3):
    for column in range(3):
        btn = Button(root)
        btn.config(command=lambda b=btn, i=index: on_button_click(b, i))
        btn.place(x = column * 200, y = row * 200, width = 200, height = 200)
        P1button_List.append(False)
        P2button_List.append(False)
        index += 1

# Initialization of players' turns

def switch_player_turn():
    global Player1
    if (Player1 == True):
        Player1 = False
    else:
        Player1 = True
# This function displays the winner and cleans window after winner has been declared
def win_prep():
    for widget in root.winfo_children():
        widget.destroy()
    if (Player1 == True):
        root.after(100, Label(root, text="Player 1 has Won!", font=("Arial", 30)).pack(pady=200))
        root.after(5000, root.destroy)
    else:
        root.after(100, Label(root, text="Player 2 has Won!", font=("Arial", 30)).pack(pady=200))
        root.after(5000, root.destroy)
# This function handles the draw case
def draw_prep():
    for widget in root.winfo_children():
        widget.destroy()
        root.after(100, Label(root, text="Draw!", font=("Arial", 30)).pack(pady=200))
        root.after(5000, root.destroy)
    
# This function was already initialized when button was created and will be executed once button is clicked.
# Should display 'X' or 'O' depends on which player is playing currently.
# Also checks for cases, such as win condition, draw condition.
def on_button_click(button, index):
    global Player1
    global count
    win = False
    # Check for edge case, where current player shouldn't be able to press other player's marked button.
    if (Player1 == True and P1button_List[index] == False and P2button_List[index] != True) or (Player1 == False and P2button_List[index] == False and P1button_List[index] != True):
        if Player1 == True:
            button.config(text="X", font=("Arial", 35))
            P1button_List[index] = True
            count += 1
        else:
            button.config(text="O", font=("Arial", 35))
            P2button_List[index] = True
            count += 1
        # Check for Win Conditions
        if (Player1 == True):
            #Diagonals \
            if P1button_List[0] != False and P1button_List[0] == P1button_List[4] == P1button_List[8]:
                win = True
            if P1button_List[2] != False and P1button_List[2] == P1button_List[4] == P1button_List[6]:
                win = True
        else:
            #Diagonals /
            if P2button_List[0] != False and P2button_List[0] == P2button_List[4] == P2button_List[8]:
                win = True
            if P2button_List[2] != False and P2button_List[2] == P2button_List[4] == P2button_List[6]:
                win = True
        if win != True:
            for num in range(3):
                if (Player1 == True):
                    #Check Column
                    if P1button_List[num] != False and P1button_List[num] == P1button_List[num + 3] == P1button_List[num + 6]:
                        win = True
                        break
                    #Check Row
                    if P1button_List[num * 3] != False and P1button_List[num * 3] == P1button_List[num * 3 + 1] == P1button_List[num * 3 + 2]:
                        win = True
                        break
                else:
                    #Check Column
                    if P2button_List[num] != False and P2button_List[num] == P2button_List[num + 3] == P2button_List[num + 6]:
                        win = True
                        break
                    #Check Row
                    if P2button_List[num * 3] != False and P2button_List[num * 3] == P2button_List[num * 3 + 1] == P2button_List[num * 3 + 2]:
                        win = True
                        break
        if win == True:
            root.after(200, win_prep)
            return
        #Check for Draw Condition
        if count == 9:
            root.after(200, draw_prep)
        switch_player_turn()
root.mainloop()