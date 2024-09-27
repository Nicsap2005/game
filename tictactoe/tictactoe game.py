import tkinter as tk

counter = 0
player = "X"

board = [["","",""],
         ["","",""],
         ["","",""]
        ]

def rules():
    global board
    global player
    button = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
    checkboard = [j for i in board for j in i]
    if "" not in (board[0][0],board[0][1],board[0][2]) and board[0][0]==board[0][1]==board[0][2]:
        player_label.config(text=f"WINNER: {board[0][0]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                 ["","",""],
                 ["","",""]]
        for i in button:
            i.config(text='')
        
            
    elif "" not in (board[1][0],board[1][1],board[1][2]) and board[1][0]==board[1][1]==board[1][2]:
        player_label.config(text=f"WINNER: {board[1][0]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                 ["","",""],
                 ["","",""]]
        for i in button:
            i.config(text='')
            
    elif "" not in (board[2][0],board[2][1],board[2][2]) and board[2][0]==board[2][1]==board[2][2]:
        player_label.config(text=f"WINNER: {board[2][0]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')
        
    if "" not in (board[0][0], board[1][0], board[2][0]) and board[0][0]==board[1][0]==board[2][0]:    
        player_label.config(text=f"WINNER: {board[0][0]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')
            
    elif "" not in (board[0][1], board[1][1], board[2][1]) and board[0][1]==board[1][1]==board[2][1]:
        player_label.config(text=f"WINNER: {board[0][1]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')
    elif "" not in (board[0][2], board[1][2], board[2][2]) and board[0][2]==board[1][2]==board[2][2]:    
        player_label.config(text=f"WINNER: {board[0][2]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')
        
    if "" not in (board[0][0],board[1][1],board[2][2]) and board[0][0]==board[1][1]==board[2][2]:    
        player_label.config(text=f"WINNER: {board[0][0]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')
    elif "" not in(board[0][2], board[1][1], board[2][0]) and board[0][2]==board[1][1]==board[2][0]:
        player_label.config(text=f"WINNER: {board[0][2]}\nNEXT TURN: {player}",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')
            
    elif "" not in checkboard and  len(checkboard) == 9:
        player_label.config(text="DRAW",fg='Black')
        board = [["","",""],
                ["","",""],
                ["","",""]]
        for i in button:
            i.config(text='')

def reset():
    button = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
    global board
    global player
    global counter
    player = "X"
    counter = 0
    board = [["","",""],
            ["","",""],
            ["","",""]]
    player_turn()
    for i in button:
        i.config(text='')
    
def player_turn():
    global player
    if counter % 2 == 1:
        player = "O"
        fc = 'Blue'
    else:
        player = "X"
        fc = 'Red'
    player_label.config(text=f"{player} TURN",fg=fc)      
        
def button_one():
    global counter
    global board
    print(board)
    if board[0][0] == "":
        board[0][0] = player
        if player == "X":
            button1.config(text=player,fg='Red')
        else:
            button1.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")
        
def button_two():
    global counter
    global board
    print(board)
    if board[0][1] == "":
        board[0][1] = player
        if player == "X":
            button2.config(text=player,fg='Red')
        else:
            button2.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")
        
def button_three():
    global counter
    global board
    print(board)
    if board[0][2] == "":
        board[0][2] = player
        if player == "X":
            button3.config(text=player,fg='Red')
        else:
            button3.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")
    
def button_four():
    global counter
    global board
    print(board)
    if board[1][0] == "":
        board[1][0] = player
        if player == "X":
            button4.config(text=player,fg='Red')
        else:
            button4.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")

def button_five():
    global counter
    global board
    print(board)
    if board[1][1] == "":
        board[1][1] = player
        if player == "X":
            button5.config(text=player,fg='Red')
        else:
            button5.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")

def button_six():
    global counter
    global board
    print(board)
    if board[1][2] == "":
        board[1][2] = player
        if player == "X":
            button6.config(text=player,fg='Red')
        else:
            button6.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")

def button_seven():
    global counter
    global board
    print(board)
    if board[2][0] == "":
        board[2][0] = player
        if player == "X":
            button7.config(text=player,fg='Red')
        else:
            button7.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")

def button_eight():
    global counter
    global board
    print(board)
    if board[2][1] == "":
        board[2][1] = player
        if player == "X":
            button8.config(text=player,fg='Red')
        else:
            button8.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")

def button_nine():
    global counter
    global board
    print(board)
    if board[2][2] == "":
        board[2][2] = player
        if player == "X":
            button9.config(text=player,fg='Red')
        else:
            button9.config(text=player,fg='Blue')
        counter += 1
        player_turn()
        rules()
        warning_label.config(text='')
    else:
        warning_label.config(text="pick another one!")

        
root = tk.Tk()
root.config(bg="#2ef051")
root.title("TICTACTOE")

player_label = tk.Label(root,width=20,height=5,font=('Arial',15),text=f"{player} TURN",fg='Red',bg="#2ef051")
player_label.grid(row=0,column=0,columnspan=4)

warning_label = tk.Label(root,font=('Arial',20) ,text='',bg="#2ef051")
warning_label.grid(row=1, column=0,columnspan=4)


r,c = 2,0
w,h = 16,8
button1 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_one,bg="#2ef051",borderwidth=2, relief="solid")
button1.grid(row=r, column=c, padx=0, pady=0)

button2 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_two,bg="#2ef051",borderwidth=2, relief="solid")
button2.grid(row=r, column=c+1, padx=0, pady=0)

button3 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_three,bg="#2ef051",borderwidth=2, relief="solid")
button3.grid(row=r, column=c+2, padx=0, pady=0)

button4 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_four,bg="#2ef051",borderwidth=2, relief="solid")
button4.grid(row=r+1, column=c  , padx=0, pady=0)

button5 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_five,bg="#2ef051",borderwidth=2, relief="solid")
button5.grid(row=r+1, column=c+1, padx=0, pady=0)

button6 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_six,bg="#2ef051",borderwidth=2, relief="solid")
button6.grid(row=r+1, column=c+2, padx=0, pady=0)

button7 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_seven,bg="#2ef051",borderwidth=2, relief="solid")
button7.grid(row=r+2, column=c  , padx=0, pady=0)

button8 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_eight,bg="#2ef051",borderwidth=2, relief="solid")
button8.grid(row=r+2, column=c+1, padx=0, pady=0)

button9 = tk.Button(root, width=w, height=h, text='',font=('Arial',10), command=button_nine,bg="#2ef051",borderwidth=2, relief="solid")
button9.grid(row=r+2, column=c+2, padx=0, pady=0)

reset_button = tk.Button(root, width=w, height=h, text='RESET',font=('Arial',10),command=reset,bg="#2ef051")
reset_button.grid(row=5, column=2, padx=0, pady=0)

root.mainloop()

