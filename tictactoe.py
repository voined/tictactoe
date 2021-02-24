import random
import time

board1 = [' ',' ',' ']
board2 = [' ',' ',' ']  #the board
board3 = [' ',' ',' ']


  #game over checker




def tictactoe():

    winner = ''
    is_x = True
    game_over = False
    
    while game_over == False:
        
        
        user_row = int(input('Row: '))
        user_column = int(input('Column: '))  #user inputs
        
        
        
        if user_row == 1 and is_x == True:
            if board1[user_column - 1] != 'X' and board1[user_column - 1] != 'O':
                board1[user_column - 1] = 'X'
                is_x = False
            else:
                print('SPOT UNAVAILABLE')
                print('')
                time.sleep(0.5)
            
        elif user_row == 2 and is_x == True:
            if board2[user_column - 1] != 'X' and board2[user_column - 1] != 'O':
                board2[user_column - 1] = 'X'
                is_x = False
            else:
                print('SPOT UNAVAILABLE')
                print('')
                time.sleep(0.5)
        
        elif user_row == 3 and is_x == True:
            if board3[user_column - 1] != 'X' and board3[user_column - 1] != 'O':
                board3[user_column - 1] = 'X'
                is_x = False
            else:
                print('SPOT UNAVAILABLE')
                print('')
                time.sleep(0.5)
            
        
    
        
            
            
        
        computer_row = random.randint(0, 2) 
        computer_column = random.randint(0, 2) 
       
        time.sleep(0.25)
       
        while is_x == False:
            if computer_row == 0 and is_x == False:
                
                if board1[computer_column] != 'X' and board1[computer_column] != 'O':
                    board1[computer_column] = 'O'
                    is_x = True
                else:
                    computer_column = random.randint(0, 2)
                    computer_row = random.randint(0, 2)
                    
            elif computer_row == 1 and is_x == False:
                
                if board2[computer_column] != 'X' and board1[computer_column] != 'O':
                    board2[computer_column] = 'O'      #makes computer's O appear
                    is_x = True
                else:
                    computer_column = random.randint(0, 2)
                    computer_row = random.randint(0, 2)
                
            elif computer_row == 2 and is_x == False:
                
                if board3[computer_column] != 'X' and board1[computer_column] != 'O':
                    board3[computer_column] = 'O'
                    is_x = True
                else:
                    computer_column = random.randint(0, 2)
                    computer_row = random.randint(0, 2)
                    
          
          
        print(board1)
        print(board2)
        print(board3)  
        
        
        #WIN CONDITIONS
                    
                    
        
        #horizontal
        if board1[0] == 'X' and board1[1] == 'X' and board1[2] == 'X':
            winner = 'X'
            
        elif board1[0] == 'O' and board1[1] == 'O' and board1[2] == 'O':
            winner = 'O'
            
            
        if board2[0] == 'X' and board2[1] == 'X' and board2[2] == 'X':
            winner = 'X'
            
        elif board2[0] == 'O' and board2[1] == 'O' and board2[2] == 'O':
            winner = 'O'
            
        
        if board3[0] == 'X' and board3[1] == 'X' and board3[2] == 'X':
            winner = 'X'
            
        elif board3[0] == 'O' and board3[1] == 'O' and board3[2] == 'O':
            winner = 'O'
            
        
        
        
        #vertical
        if board1[0] == 'X' and board2[0] == 'X' and board3[0] == 'X':
            winner = 'X'
            
        elif board1[0] == 'O' and board2[0] == 'O' and board3[0] == 'O':
            winner = 'O'
            
        
        if board1[1] == 'X' and board2[1] == 'X' and board3[1] == 'X':
            winner = 'X'
            
        elif board1[1] == 'O' and board2[1] == 'O' and board3[1] == 'O':
            winner = 'O'
            
        
        if board1[2] == 'X' and board2[2] == 'X' and board3[2] == 'X':
            winner = 'X'
            
        elif board1[2] == 'O' and board2[2] == 'O' and board3[2] == 'O':
            winner = 'O'
            
        
        
        #diagonal
        if board1[0] == 'X' and board2[1] == 'X' and board3[2] == 'X':
            winner = 'X'
            
        elif board1[0] == 'O' and board2[1] == 'O' and board3[2] == 'O':
            winner = 'O'
            
        
        if board1[2] == 'X' and board2[1] == 'X' and board3[0] == 'X':
            winner = 'X'
            
        elif board1[2] == 'O' and board2[1] == 'O' and board3[0] == 'O':
            winner = 'O'
            

        
        if winner == 'X':
            print('GAME OVER, X HAS WON THE GAME')
            game_over = True
        elif winner == 'O':
            print('GAME OVER, O HAS WON THE GAME')
            game_over = True
        
        
        
        
        

        
    
tictactoe()




   
time.sleep(5)  