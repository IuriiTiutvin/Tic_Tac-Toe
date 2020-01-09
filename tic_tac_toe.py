from tkinter import *

master = Tk()
master.geometry("290x290")
master.resizable(False, False)
master.title("Tic Tac Toe")

print("Would player 1 like to be x or o?")
player_1 = input("> ")
if player_1 == "x":
    print("Then player 2 will be o")
    player_2 = 'o'
if player_1 == 'o':
    print("Then player 2 will be x")
    player_2 = "x"
print("Player 1 will go first, then player 2 can go.")

def reset(var):
    if var == 9:
        var = 0

text = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
squares = ["none", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
current_turn = 1

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

def change(x):
    global squares
    global current_turn
    global player_1
    global player_2
    if current_turn == 1 and squares[x] == "empty":
        text[x] = player_1
        text_update()
        current_turn += 1
        squares[x] = "full"
    elif current_turn == 2 and squares[x] == "empty":
        text[x] = player_2
        text_update()
        current_turn -= 1
        squares[x] = "full"
    win_check()

def finish():
    global button_num
    while button_num < len(buttons):
        buttons[button_num].grid_forget()
        button_num += 1
        reset(button_num)

def win_check():
    global player_1
    global player_2
    if text[1] == text[2] == text[3] == 'x' or text[4] == text[5] == text[6] == 'x' or text[7] == text[8] == text[9] == 'x' or text[1] == text[4] == text[7] == 'x' or text[2] == text[5] == text[8] == 'x' or text[3] == text[6] == text[9] == 'x' or text[1] == text[5] == text[9] == 'x' or text[3] == text[5] == text[7] == 'x':
        if player_1 == 'x':
            print("Player 1, who was playing as x, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Player 1, who was playing as x, won")
            win_text.pack()
        if player_2 == 'x':
            print("Player 2, who was playing as x, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Player 2, who was playing as x, won")
            win_text.pack()
    elif text[1] == text[2] == text[3] == 'o' or text[4] == text[5] == text[6] == 'o' or text[7] == text[8] == text[9] == 'o' or text[1] == text[4] == text[7] == 'o' or text[2] == text[5] == text[8] == 'o' or text[3] == text[6] == text[9] == 'o' or text[1] == text[5] == text[9] == 'o' or text[3] == text[5] == text[7] == 'o':
        if player_1 == 'o':
            print("Player 1, who was playing as o, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Player 1, who was playing as o, won")
            win_text.pack()
        if player_2 == 'o':
            print("Player 2, who was playing as o, won.")
            finish()
            win_text = Text(master)
            win_text.insert(INSERT, "Player 2, who was playing as o, won")
            win_text.pack()
    elif squares[1] == 'full' and squares[2] == 'full' and squares[3] == 'full' and squares[4] == 'full' and squares[5] == 'full' and squares[6] == 'full' and squares[7] == 'full' and squares[8] == 'full' and squares[9] == 'full':
        print('It is a tie')
        finish()
        win_text = Text(master)
        win_text.insert(INSERT, "It is a tie")
        win_text.pack()

b1 = Button(master, width = 4, height = 2, text = text[1], command = lambda: change(1))
b2 = Button(master, width = 4, height = 2, text = text[2], command = lambda: change(2))
b3 = Button(master, width = 4, height = 2, text = text[3], command = lambda: change(3))
b4 = Button(master, width = 4, height = 2, text = text[4], command = lambda: change(4))
b5 = Button(master, width = 4, height = 2, text = text[5], command = lambda: change(5))
b6 = Button(master, width = 4, height = 2, text = text[6], command = lambda: change(6))
b7 = Button(master, width = 4, height = 2, text = text[7], command = lambda: change(7))
b8 = Button(master, width = 4, height = 2, text = text[8], command = lambda: change(8))
b9 = Button(master, width = 4, height = 2, text = text[9], command = lambda: change(9))

buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
button_num = 0
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
