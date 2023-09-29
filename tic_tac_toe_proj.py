#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:25:57 2023

@author: sofiafrenkknaul
"""

"""
Course: Python for Scientists (Part-I)
"""
#%%
def author():
    '''
    return your name
    '''
    return 'Sofia Frenk-Knaul'
#%%
import random
import copy
# %%
def DrawBoard(Board):
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
    for i in range(0, len(Board)):
        for j in range(0, len(Board[i])):
            print(Board[i][j], end='')
            if j < (len(Board[i])-1):
                print('|', end='')
            else:
                print()
        if i < (len(Board)-1):
            print('-+-+-')    
                
    #pass
#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        (1) return True  if Board[i][j] is empty (' ')
        (2) return False if Board[i][j] is not empty
        (3) return False if i or j is invalid (e.g. i = -1 or 100)
        think about the order of (1) (2) (3)
    '''
    if (i<0 and i>2) or (j<0 and j>2):
        return False
    
    for row in range(0, len(Board)):
        for col in range(0, len(Board[row])):
            if i == row and j == col:
                if Board[i][j] == ' ':
                    return True
                else:
                    return False
    #pass
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    content_counter = 0;
    for i in range(0, len(Board)):
        for j in range(0, len(Board[i])):
            if Board[i][j] != ' ':
                content_counter += 1
    return content_counter            
    #pass
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    number_of_pieces = GetNumberOfChessPieces(Board)
    if (number_of_pieces == 9):
        return True
    else:
        return False
    #pass
#%%
def IsBoardEmpty(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    number_of_pieces = GetNumberOfChessPieces(Board)
    if (number_of_pieces == 0):
        return True
    else:
        return False
    #pass
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag at the location (row, col)
    '''
    print("Choice: ", Choice)
    row, col = Choice
    print('row: ', row)
    print('col: ', col)
    for i in range(0, len(Board)):
        for j in range(0, len(Board[i])):
            if i==row and j==col:
                Board[i][j] = Tag
    #pass
#%%
def HumanPlayer(Tag, Board):
    '''
    Parameters: 
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        a while loop is needed, see HumanPlayer in rock-papper-scissors
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    #i_valid_values = [0,1,2]
    #j_valid_values = [0,1,2]
    while True:
        print('make your choice:')
        try:
            i = int(input())
            j = int(input())
            print('row = ', i)
            print()
            print('col = ', j)
            #check if place not occupied
            check_space = IsSpaceFree(Board, i, j)
            if check_space != False:
                ChoiceOfHumanPlayer = (i, j)
                print('HumanPlayer(', Tag, ') has made the choice')
                return ChoiceOfHumanPlayer
            else:
                print('Space (', i, ',', j, ') is occupied. Pls try again.')
        except:
            print('Oops! That is not a valid number. Try again...')
        
    #pass
#%%
def ComputerPlayer(Tag, Board, N=1):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N: think N steps ahead, default N=1
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if the spot is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
    
    winning_options = [((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
                       ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                       ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))]
    OppositeTag = ''
    if(Tag == 'X'):
        OppositeTag = 'O'
    elif(Tag == 'O'):
        OppositeTag = 'X'
        
    corners_list = [(0,0), (0,2), (2,0), (2,2)]    
    while True:
        check_if_empty = IsBoardEmpty(Board)
        if check_if_empty == True:
            random_index = random.randint(0, 3)
            ChoiceOfComputerPlayer = corners_list[random_index]
            print('ComputerPlayer(', Tag, ') has made the choice')
            return ChoiceOfComputerPlayer
    
        for coord_tuple in corners_list:
            x, y = coord_tuple
            single_piece = GetNumberOfChessPieces(Board)
            if single_piece == 1 and Board[x][y] == OppositeTag:
                ChoiceOfComputerPlayer = (1, 1)
                print('ComputerPlayer(', Tag, ') has made the choice')
                return ChoiceOfComputerPlayer
         
        for tuple_trio in winning_options:  #  for ( char c :  str_var)
            pos1, pos2, pos3 = tuple_trio
            coordX1, coordY1 = pos1
            coordX2, coordY2 = pos2
            coordX3, coordY3 = pos3
            if Board[coordX1][coordY1] == Tag and Board[coordX1][coordY1] == Board[coordX2][coordY2]:
                if Board[coordX3][coordY3] == ' ':
                    ChoiceOfComputerPlayer = (coordX3, coordY3)
                    print('ComputerPlayer(', Tag, ') has made the choice')
                    return ChoiceOfComputerPlayer
                elif Board[coordX1][coordY1] == Tag and Board[coordX1][coordY1] == Board[coordX3][coordY3]:
                    if Board[coordX2][coordY2] == ' ':
                        ChoiceOfComputerPlayer = (coordX2, coordY2)
                        print('ComputerPlayer(', Tag, ') has made the choice')
                        return ChoiceOfComputerPlayer
                    elif Board[coordX2][coordY2] == Tag and Board[coordX2][coordY2] == Board[coordX3][coordY3]:
                        if Board[coordX1][coordY1] == ' ':
                            ChoiceOfComputerPlayer = (coordX1, coordY1)
                            print('ComputerPlayer(', Tag, ') has made the choice')
                            return ChoiceOfComputerPlayer  
         
        for tuple_trio in winning_options:  #  for ( char c :  str_var)
            pos1, pos2, pos3 = tuple_trio
            coordX1, coordY1 = pos1
            coordX2, coordY2 = pos2
            coordX3, coordY3 = pos3
            if Board[coordX1][coordY1] == OppositeTag and Board[coordX1][coordY1] == Board[coordX2][coordY2]:
                if Board[coordX3][coordY3] == ' ':
                    ChoiceOfComputerPlayer = (coordX3, coordY3)
                    print('ComputerPlayer(', Tag, ') has made the choice')
                    return ChoiceOfComputerPlayer
                if Board[coordX1][coordY1] == OppositeTag and Board[coordX1][coordY1] == Board[coordX3][coordY3]:
                    if Board[coordX2][coordY2] == ' ':
                        ChoiceOfComputerPlayer = (coordX2, coordY2)
                        print('ComputerPlayer(', Tag, ') has made the choice')
                        return ChoiceOfComputerPlayer
                if Board[coordX2][coordY2] == OppositeTag and Board[coordX2][coordY2] == Board[coordX3][coordY3]:
                    if Board[coordX1][coordY1] == ' ':
                        ChoiceOfComputerPlayer = (coordX1, coordY1)
                        print('ComputerPlayer(', Tag, ') has made the choice')
                        return ChoiceOfComputerPlayer
                
        rand_x_coord = random.randint(0, 2)
        rand_y_coord = random.randint(0, 2)
        check_space = IsSpaceFree(Board, rand_x_coord, rand_y_coord)
        
        if check_space != False:
            ChoiceOfComputerPlayer = (rand_x_coord, rand_y_coord)
            print('ComputerPlayer(', Tag, ') has made the choice')
            return ChoiceOfComputerPlayer
        else:
            print('Space (', rand_x_coord, ',', rand_y_coord, ') is occupied. Pls try again.')
            continue
    #pass
#%%
def Judge(Board):
    '''
    Parameter:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
            use a if-statment to check if three 'X'/'O' in a row
        (2) if no one wins, then check if it is a tie
            note: if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''

    winning_options = [((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
                       ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                       ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))]
    
    #dict_example = {"fruit":"apple",  "sport":"soccer", "planet":"earth"}
    #print(dict_example['fruit']) 
    
    #loop through each touple element in winning_options
    for tuple_trio in winning_options:
        #create a set for the symbols X and O - if any adjacent three cells has a symbol, a single one will be stored in the set
        symbols = set()
        #loop through a touple elemet 
        for pos in tuple_trio:
            #extract the elemets of the sub-touples
            x, y = pos
            #use elements of the sub-touples as coordinates to access elements in the Board
            symbols.add(Board[x][y])
        #make a list out of the symbols set so it can be iterated through    
        symbols_l = list(symbols)
        #if the element in the symbol list is not an empty space and the symbols set has a length of one (bc there were 3 adj symbols)
        if symbols_l[0] != ' ' and len(symbols) == 1:
            #access the element of the list of symbols - either X or O - which will be a key in the dictiorary used to return the number value assoc to the key
            return {"X":1, "O":2}[ symbols_l[0] ]

        board_full = IsBoardFull(Board)
    
    if board_full == True:
        return 3
    return 0 
'''    
    for tuple_trio in winning_options:  #  for ( char c :  str_var)
        pos1, pos2, pos3 = tuple_trio
        coordX1, coordY1 = pos1
        coordX2, coordY2 = pos2
        coordX3, coordY3 = pos3
        if Board[coordX1][coordY1] != ' ' and (Board[coordX1][coordY1] == Board[coordX2][coordY2] and 
        Board[coordX1][coordY1] == Board[coordX3][coordY3]):
            if Board[coordX1][coordY1] == 'X':
                return 1
            elif Board[coordX1][coordY1] == 'O':
                return 2
'''            
           
    #pass
#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    #options from judge: 0(in progress), 1(x wins), 2(o wins), 3(tie)
    if Outcome == 0:
        print('the game is still in progress')
    elif Outcome == 1:
        print('PlayerX (', NameX, 'X) wins ')
    elif Outcome == 2:
        print('PlayerO (', NameO, 'O) wins')
    elif Outcome == 3:
        print('it is a tie')
    #pass
#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX  = ComputerPlayer
        PlayerO = HumanPlayer
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer
        PlayerX = HumanPlayer
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Wellcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first()

    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # (1)  get a choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get a choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    while True:
        ChoiceX = PlayerX('X', Board)
        UpdateBoard(Board, 'X', ChoiceX)
        DrawBoard(Board)
        judge_X = Judge(Board)
        ShowOutcome(judge_X, NameX, NameO)
        if judge_X == 1 or judge_X == 2 or judge_X == 3:
            break;
        
        ChoiceO = PlayerO('O', Board)
        UpdateBoard(Board, 'O', ChoiceO)
        DrawBoard(Board)
        judge_O = Judge(Board)
        ShowOutcome(judge_O, NameX, NameO)
        if judge_O == 1 or judge_O == 2 or judge_O == 3:
            break;
    #pass
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()
