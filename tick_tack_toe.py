
originalB = {1: '--', 2: '--', 3: '--',
         4: '--', 5: '--', 6: '--',
         7: '--', 8: '--', 9: '--'}

score = {'player1' : 0 , 'player2' : 0}

def print_board():

    print(f' 1) {originalB[1]} 2) {originalB[2]} 3) {originalB[3]}')
    print(f' 4) {originalB[4]} 5) {originalB[5]} 6) {originalB[6]} ')
    print(f' 7) {originalB[7]} 8) {originalB[8]} 9) {originalB[9]} ')

def reset_board():
    global originalB     #you use the 'global' work to acces a variable outside the function.
    originalB = {1: '--', 2: '--', 3: '--',
                4: '--', 5: '--', 6: '--',
                7: '--', 8: '--', 9: '--'}

def restart_game():
    conGame = input('would you like to restart the game? \nYES: [y] NO: [n]\n')
    if conGame == 'y':
       reset_board()
       print_board()
    else:
        print('Goodbye!')
        exit()

def check_for_win():
    if originalB[1] == originalB[2] == originalB[3] == 'O' or originalB[4] == originalB[5] == originalB[6] == 'O' or originalB[7] == originalB[8] == originalB[9] == 'O' or originalB[1] == originalB[4] == originalB[7] == 'O' or originalB[2] == originalB[5] == originalB[8] == 'O' or originalB[3] == originalB[6] == originalB[9] == 'O' or originalB[1] == originalB[5] == originalB[9] == 'O' or originalB[3] == originalB[5] == originalB[7] == 'O':
        print('player1 won!')
        global score
        score['player1'] += 1
        print_score()
        restart_game()
         
        
    if originalB[1] == originalB[2] == originalB[3] == 'X' or originalB[4] == originalB[5] == originalB[6] == 'X' or originalB[7] == originalB[8] == originalB[9] == 'X' or originalB[1] == originalB[4] == originalB[7] == 'X' or originalB[2] == originalB[5] == originalB[8] == 'X' or originalB[3] == originalB[6] == originalB[9] == 'X' or originalB[1] == originalB[5] == originalB[9] == 'X' or originalB[3] == originalB[5] == originalB[7] == 'X':
        print('player2 won!')
        score['player2'] += 1
        print_score()
        restart_game()
        
def check_for_draw():
    for x in originalB:
        if originalB[x] == '--':
            return 
    print('draw game!')
    print_score()
    restart_game()

def player_turn(player):
    while True:
        try:
            playerkind = int(input(f'player{player} please enter where you want to go\n'))
        except:
            print('please enter in a valid possition')
            print_board()
        else:
            if playerkind > 0 and playerkind < 10 and originalB[playerkind] == '--':
                if player == 1:
                    originalB[playerkind] = 'O'
                else:
                    originalB[playerkind] = 'X'
                print_board()
                check_for_win()
                check_for_draw()
                break
            else:
                print('please enter a valid possition')
                print_board()
        

def print_score():
    print(f'player1 has: {score["player1"]} points \nplayer2 has: {score["player2"]} points')


print('Welcome to the game of Tick Tack To')
print_board()


while True:
    player_turn(1)
    player_turn(2)


    
