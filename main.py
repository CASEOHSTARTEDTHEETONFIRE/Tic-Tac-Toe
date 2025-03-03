import os
print("Hello, Casoh!")
tic_tac_toe = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("- - - - - - - - - - - - - - -  ")
print("Tic Tac Toe game.")
print("- - - - - - - - - - - - - - -  ")
# input function: a command in python that has the computer ask a question or tell you something and gives you the ability to respond back
name = input("Type your name or else im gonna call u a bot: ")
CPU = ""
piece = input(" X or O")
if piece == "X":
  CPU = "O"
if piece == "O":
  CPU = "X"
#Input functions converts ur response in2 a string (str),
#how to save a input function -- make a variable n store it AND SAVE FILE.
print("hello " + name)

while True:
    # prints the tic tac toe board
    print("--------------")
    print(str(tic_tac_toe[0]) + "|" + str(tic_tac_toe[1]) + "|" +
        str(tic_tac_toe[2]))
    print("-----")
    print(str(tic_tac_toe[3]) + "|"+ str(tic_tac_toe[4])+"|"+str(tic_tac_toe[5]))
    print("-----")4
    print(str(tic_tac_toe[6])+"|"+ str(tic_tac_toe[7]) +"|"+ str(tic_tac_toe[8]))
    position = input("where do u want to place your piece?")
    # input saves the data as strings. :)
    # keeps asking to put a valid response until the user puts a valid response
    while position not in "1,2,3,4,5,6,7,8,9" and len(position) > 1:
        print("pls choose a VALID response!!!!!!!!!! :-)")
        position = input("where do u want to place your piece?")
    # place the piece in the designated positionß
    tic_tac_toe[int(position) - 1] = piece
    os.system('clear')


