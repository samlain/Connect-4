#Name: Connect 4 - Sam, Ivan, Cole, and Shivam
#Date: 11.9.22
#Project: Connect 4 Final

#imports
import pythonGraph
import random 

#functions
#graphics
#starts game
def start():
    #varibles 
    global arrow_visible
    #if the arrow is visible the function stops
    if arrow_visible == True:
        return
    pythonGraph.draw_rectangle(345, 5, 465, 45, 'GREEN', True)
    pythonGraph.draw_text('START', 350, 10, 'BLACK', 50)
    #if the user left clicks on the start button then the arrow becomes visible 
    if pythonGraph.mouse_button_down('LEFT'):
        x = pythonGraph.get_mouse_x()
        y = pythonGraph.get_mouse_y()
        if x > 345 and x < 465:
            if y > 5 and y < 45:
                arrow_visible = True
                
#clear window
def clear():
    pythonGraph.clear_window(('WHITE'))

#game board 
def board():
    #outter board
    pythonGraph.draw_rectangle(50, 50, 750, 650, 'BLUE', False, 10)
    #inner board horizontal lines 
    pythonGraph.draw_line(50, 150, 750, 150, 'BLUE', width = 10)
    pythonGraph.draw_line(50, 250, 750, 250, 'BLUE', width = 10)
    pythonGraph.draw_line(50, 350, 750, 350, 'BLUE', width = 10)
    pythonGraph.draw_line(50, 450, 750, 450, 'BLUE', width = 10)
    pythonGraph.draw_line(50, 550, 750, 550, 'BLUE', width = 10)
    #inner board vertical lines
    pythonGraph.draw_line(150, 50, 150, 650, 'BLUE', width = 10)
    pythonGraph.draw_line(250, 50, 250, 650, 'BLUE', width = 10)
    pythonGraph.draw_line(350, 50, 350, 650, 'BLUE', width = 10)
    pythonGraph.draw_line(450, 50, 450, 650, 'BLUE', width = 10)
    pythonGraph.draw_line(550, 50, 550, 650, 'BLUE', width = 10)
    pythonGraph.draw_line(650, 50, 650, 650, 'BLUE', width = 10)
    #loop to move the pieces to any spot
    x = 102 
    y = 102
    #loops all the columns of the board 
    for c in data_board:
        #loops all the rows in the columns
        for r in c:
            #if it is players turn then drop a red piece 
            if r == 1:
                pythonGraph.draw_circle(x, y, 35, 'RED', True)
            #if it is the computers turn then drop a yellow piece 
            elif r == 2:
                pythonGraph.draw_circle(x, y, 35, 'YELLOW', True)
            y += 100
        x += 100
        y = 102

#arrow that points at a column
def arrow():
    #varible
    global arrow_move_right
    #if the arrow is not visible then stop the function
    if arrow_visible == False:
        return
    pythonGraph.draw_line(102 + arrow_move_right, 5, 102 + arrow_move_right, 45, 'BLACK', width = 5)
    pythonGraph.draw_line(102 + arrow_move_right, 45, 112 + arrow_move_right, 30, 'BLACK', width = 5)
    pythonGraph.draw_line(102 + arrow_move_right, 45, 92 + arrow_move_right, 30, 'BLACK', width = 5)

#gameplay
#moves arrow to the right or left and drops pieces 
def arrow_right_left_or_return():
    #varibles
    global arrow_move_right, column, gameover, arrow_visible
    #if the game is over and the arrow is not visible then stop the function
    if gameover == True or arrow_visible == False:
        return
    #if the the user presses the right key then the arrow will move to the right
    if pythonGraph.key_pressed('right'):
        #the furthest column the user can go to the right is the seventh one 
        if column < 6:
            column += 1
            arrow_move_right += 100
    #if the the user presses the left key then the arrow will move to the left
    elif pythonGraph.key_pressed('left'):
        #the furthest column the user can go to the left is the zeroth one 
        if column > 0:
            column -= 1
            arrow_move_right -= 100
    #if the user presses the enter key then where ever the arrow is pointing a piece will drop there 
    elif pythonGraph.key_pressed('return'):
        drop_piece(column)
        
#makes win or lose text appear
def win_lose():
    #varibles
    global gameover, player
    #if the game is over then a message will appear
    if gameover == True:
        #if the game ended on the players turn then a losing message will appear
        if player == 1:
            pythonGraph.draw_text('YOU LOST!', 210, 320, 'RED', 100)
        #if the game ended on the computers turn then a winning message will appear
        else:
            pythonGraph.draw_text('YOU WON!', 235, 320, 'GREEN', 100)
            

#checks the board to see if anyone has won
def check_win(column, player):
    #varibles
    global data_board, gameover, row 
    #vertical win
    for c in range(0, 3):
        if data_board[column][c] == player and data_board[column][c + 1] == player and data_board[column][c + 2] == player and data_board[column][c + 3] == player:
            return True
    #horizontal win
    for c in range(0, 4):
        if data_board[c][row] == player and data_board[c + 1][row] == player and data_board[c + 2][row] == player and data_board[c + 3][row] == player:
            return True
    #negative diagonal win
    for c in range(0, 3):
        for newrow in range(3, 7):
            if data_board[newrow][c] == player and data_board[newrow - 1][c + 1] == player and data_board[newrow - 2][c + 2] == player and data_board[newrow - 3][c + 3] == player:
                return True  
    #positive diagonal win
    for c in range(0, 3):
        for newrow in range(0, 4):
            if data_board[newrow][c] == player and data_board[newrow + 1][c + 1] == player and data_board[newrow + 2][c + 2] == player and data_board[newrow + 3][c + 3] == player:
                return True
    return False

#resets the board 
def new_game():
    pythonGraph.draw_rectangle(300, 655, 500, 695, 'RED', True)
    pythonGraph.draw_text('NEW GAME', 305, 660, 'BLACK', 50)
    #if the user left clicks on the new game button then the board will reset to the begininng
    if pythonGraph.mouse_button_down('LEFT'):
        x = pythonGraph.get_mouse_x()
        y = pythonGraph.get_mouse_y()
        #if the user press between the x-coordinates of 300 and 500 and...
        if x > 300 and x < 500:
            #if the user press between the y-coordinates of 655 and 695 then the game will restart to default setting and the arrow will disappear 
            if y > 655 and y < 695:
                restart()
                arrow_visible = True
           
#drops pieces into the board 
def drop_piece(col):
    #varibles 
    global data_board, player, gameover, row
    #get column list for col 
    c = data_board[col]    
    i = 0
    #looping through the column looking for a non-zero
    while i < 6 and c[i] == 0:
        i += 1
    #if no open spaces is in this column then stop this function 
    if i == 0:
        return
    #point to last open space 
    i -= 1
    #place piece in board 
    c[i] = player
    data_board[col] = c
    row = i
    #if the player or computer wins then the game is over 
    if check_win(col, player) == True:
        gameover = True
    #if it is the players turn then the computer will play after
    if player == 1:
        player = 2
    #if it is the computers turn then the player will play after
    elif player == 2:
        player = 1
        
#computer logic 
def computers_turn():
    #varibles
    global gameover, player, data_board, row
    #if it is the computers turns and the game is not over then the computer will try to win or try to block the player from winning
    if player == 2 and gameover == False:
        #logic
        #for a winning move, looks in each column 
        for column_ai in range(0, 7):
            #get index for open space
            c = data_board[column_ai]    
            i = 0
            while i < 6 and c[i] == 0:
                i += 1
            if i == 0:
                continue 
            i -= 1
            #temporarily place computer piece in board 
            data_board[column_ai][i] = 2
            row = i
            #if the computer won then stop the function 
            if check_win(column_ai, 2):
                #remove temporary piece 
                data_board[column_ai][i] = 0
                drop_piece(column_ai)
                return
            data_board[column_ai][i] = 0
        #for blocking a winning move, looks in each column
        for column_ai in range(0, 7):
            c = data_board[column_ai]    
            i = 0
            while i < 6 and c[i] == 0:
                i += 1
            if i == 0:
                continue 
            i -= 1
             #temporarily places player piece in board 
            data_board[column_ai][i] = 1
            row = i
            #if the computer won then stop the function
            if check_win(column_ai, 1):
                #remove temporary piece 
                data_board[column_ai][i] = 0
                drop_piece(column_ai)
                return
            data_board[column_ai][i] = 0
        #no winning or blocking move available do a random move
        column_ai = random.randint(0, 6)
        drop_piece(column_ai)
        
            
#restart all varibles to inital conditions 
def restart():
    #varibles
    global arrow_move_right, column, arrow_visible, data_board, player, count, gameover, row
    arrow_move_right = 0
    column = 0
    row = 0
    player = 1
    count = 0
    arrow_visible = False
    gameover = False
    data_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    
def main():
    restart()
    #varibles
    global arrow_move_right, column, arrow_visible, data_board, player, count, gameover, row
    #open window
    pythonGraph.open_window(800, 700)
    #name
    pythonGraph.set_window_title('Connect 4')
    #clear window
    pythonGraph.clear_window(pythonGraph.create_color(255, 255, 255))
    #commands
    while pythonGraph.window_not_closed():
        clear()
        start()
        board()
        arrow()
        arrow_right_left_or_return()
        win_lose()
        new_game()
        computers_turn()
        pythonGraph.update_window()
        
if __name__ == '__main__':
    main()