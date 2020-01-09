from tkinter import *
import random
import time

master = Tk()
master.geometry("290x290")
master.resizable(False, False)
master.title("Tic Tac Toe")

print("Would you like to be x or o?")
player_1 = input("> ")
if player_1 == "x":
    print("Then computer will be o")
    computer_name = 'o'
if player_1 == 'o':
    print("Then computer will be x")
    computer_name = "x"
print("You will go first, then computer will go.")

tries = 0
won = False
squares = ["none", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
text = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x = 0
def reset(var):
    if var == 10:
        var = 1

def two_in_row(w, e, name):
    global x
    global text
    if e == 1 and x == 1:
        if text[w] == text[w+1] == name and squares[w+2] == 'empty':
            text[w+2] = computer_name
            squares[w+2] = 'full'
            text_update()
            x -= 1
        if text[w+2] == text[w+1] == name and squares[w] == 'empty':
            text[w] = computer_name
            squares[w] = 'full'
            text_update()
            x -= 1
        if text[w] == text[w+2] == name and squares[w+1] == 'empty':
            text[w+1] = computer_name
            squares[w+1] = 'full'
            text_update()
            x -=1
    if e == 2 and x == 1:
        if text[w] == text[w+3] == name and squares[w+6] == 'empty':
            text[w+6] = computer_name
            squares[w+6] = 'full'
            text_update()
            x -= 1
        if text[w+3] == text[w+6] == name and squares[w] == 'empty':
            text[w] = computer_name
            squares[w] = 'full'
            text_update()
            x -= 1
        if text[w] == text[w+6] == name and squares[w+3] == 'empty':
            text[w+3] = computer_name
            squares[w+3] = 'full'
            text_update()
            x -=1
    if e == 3 and x == 1:
        if text[w] == text[w+4] == name and squares[w+8] == 'empty':
            text[w+8] = computer_name
            squares[w+8] = 'full'
            text_update()
            x -= 1
        if text[w+4] == text[w+8] == name and squares[w] == 'empty':
            text[w] = computer_name
            squares[w] = 'full'
            text_update()
            x -= 1
        if text[w] == text[w+8] == name and squares[w+4] == 'empty':
            text[w+4] = computer_name
            squares[w+4] = 'full'
            text_update()
            x -=1
    if e == 4 and x == 1:
        if text[w] == text[w+2] == name and squares[w+4] == 'empty':
            text[w+4] = computer_name
            squares[w+4] = 'full'
            text_update()
            x -= 1
        if text[w+2] == text[w+4] == name and squares[w] == 'empty':
            text[w] = computer_name
            squares[w] = 'full'
            text_update()
            x -= 1
        if text[w] == text[w+4] == name and squares[w+2] == 'empty':
            text[w+2] = computer_name
            squares[w+2] = 'full'
            text_update()
            x -=1

def text_update():
    b1.config(text = text[1])
    b2.config(text = text[2])
    b3.config(text = text[3])
    b4.config(text = text[4])
    b5.config(text = text[5])
    b6.config(text = text[6])
    b7.config(text = text[7])
    b8.config(text = text[8])
    b9.config(text = text[9])

def computer():
    global x
    def con():
        global x
        x -= 1
        text_update()
    master.update()
    time.sleep(1)
    global x
    global text
    if won == False and x == 1:
        two_in_row(1, 1, computer_name)
        two_in_row(4, 1, computer_name)
        two_in_row(7, 1, computer_name)
        two_in_row(1, 2, computer_name)
        two_in_row(2, 2, computer_name)
        two_in_row(3, 2, computer_name)
        two_in_row(1, 3, computer_name)
        two_in_row(3, 4, computer_name)

        two_in_row(1, 1, player_1)
        two_in_row(4, 1, player_1)
        two_in_row(7, 1, player_1)
        two_in_row(1, 2, player_1)
        two_in_row(2, 2, player_1)
        two_in_row(3, 2, player_1)
        two_in_row(1, 3, player_1)
        two_in_row(3, 4, player_1)
        if x == 0:
            win_check()
    if x == 1 and squares[5] == 'empty':
        text[5] = computer_name
        squares[5] = 'full'
        con()
    if x == 1 and text[5] == player_1 and squares[3] == 'empty':
        text[3] = computer_name
        squares[3] = 'full'
        con()
    if x == 1 and text[5] == text[7] == player_1 and text[3] == computer_name and squares[1] == 'empty':
        text[1] = computer_name
        squares[1] = 'full'
        con()
    if x == 1 and text[3] == text[7] == player_1 and text[5] == computer_name and squares[2] == 'empty':
        text[2] = computer_name
        squares[2] = 'full'
        con()
    if x == 1 and text[1] == text[9] == player_1 and text[5] == computer_name and squares[2] == 'empty':
        text[2] = computer_name
        squares[2] = 'full'
        con()
    else:
        computer_rand()

def computer_rand():
    global x
    global text
    num = random.randint(1, 9)
    if squares[num] == 'empty' and x == 1:
        squares[num] = 'full'
        x -= 1
        text[num] = computer_name
        text_update()
        win_check()
    elif x == 1:
        computer_rand()

def move(y):
    global x
    global b1_square
    if x == 0 and squares[y] == 'empty':
        squares[y] = 'full'
        x += 1
        text[y] = player_1
        text_update()
        win_check()

def finish():
    time.sleep(2)
    global button_num
    while button_num < len(buttons):
        buttons[button_num].grid_forget()
        button_num += 1
        reset(button_num)

def win_check():
    master.update()
    global player_1
    global player_2
    global won
    if text[1] == text[2] == text[3] == 'x' or text[4] == text[5] == text[6] == 'x' or text[7] == text[8] == text[9] == 'x' or text[1] == text[4] == text[7] == 'x' or text[2] == text[5] == text[8] == 'x' or text[3] == text[6] == text[9] == 'x' or text[1] == text[5] == text[9] == 'x' or text[3] == text[5] == text[7] == 'x':
        if player_1 == 'x':
            print("Player 1, who was playing as x, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Player 1,\nwho was\nplaying as x,\nwon")
            win_text.config(font=('Helvetica', 50))
            win_text.pack()
            won = True
        if computer_name == 'x':
            print("Computer, who was playing as x, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Computer,\nwho was\nplaying as x,\nwon")
            win_text.config(font=('Helvetica', 50))
            win_text.pack()
            won = True
    elif text[1] == text[2] == text[3] == 'o' or text[4] == text[5] == text[6] == 'o' or text[7] == text[8] == text[9] == 'o' or text[1] == text[4] == text[7] == 'o' or text[2] == text[5] == text[8] == 'o' or text[3] == text[6] == text[9] == 'o' or text[1] == text[5] == text[9] == 'o' or text[3] == text[5] == text[7] == 'o':
        if player_1 == 'o':
            print("Player 1, who was playing as o, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Player 1,\nwho was\nplaying as o,\nwon")
            win_text.config(font=('Helvetica', 50))
            win_text.pack()
            won = True
        if computer_name == 'o':
            print("Computer, who was playing as o, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Computer,\nwho was\nplaying as o,\nwon")
            win_text.config(font=('Helvetica', 50))
            win_text.pack()
            won = True
    elif squares[1] == 'full' and squares[2] == 'full' and squares[3] == 'full' and squares[4] == 'full' and squares[5] == 'full' and squares[6] == 'full' and squares[7] == 'full' and squares[8] == 'full' and squares[9] == 'full':
        print('It is a tie')
        finish()
        win_text = Text(master)
        win_text.insert(INSERT, "It is a tie")
        win_text.config(font=('Helvetica', 50))
        win_text.pack()
        won = True
    elif x == 1:
        computer()


b1 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(1))
b2 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(2))
b3 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(3))
b4 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(4))
b5 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(5))
b6 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(6))
b7 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(7))
b8 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(8))
b9 = Button(master, width = 4, height = 2, text = ' ', command = lambda: move(9))

q = 0
buttons = [q, b1, b2, b3, b4, b5, b6, b7, b8, b9]
button_num = 1
while button_num < len(buttons):
    buttons[button_num].config(font=('Helvetica', 40))
    button_num += 1
    reset(button_num)

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)
b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)
b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)

master.mainloop()
