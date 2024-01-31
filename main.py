from board import Board
from player import Player
# Ask user for gameplay details


def main():
    # Create board
    game_board = Board(3, "dashed")
    print("Welcome to Tik Tak Toe!\n\n")
    first_name = input("Player 1 enter your name...\n")
    print(first_name+" is X\n")
    second_name = input("Player 2 enter your name...\n")
    print(second_name+" is O\n")
    
    game_count = 1
    
    first_player = Player(first_name, "X")
    second_player = Player(second_name, "O")
    player_won = False
    game_over = False
    first_player_turn = True # First player starts
    second_player_turn = False # Will be true when its second players turn
    replay_game = False
    game_board.display_board() 
    
    if game_board.created_with == "list":
        while (not game_over and not player_won) or replay_game:
            if replay_game:
                print("Game "+str(game_count))
                game_board.clear_board_list()
                game_board.display_board()
                # Reset flags
                replay_game= False
                player_won = False
                game_over = False
                first_player_turn = True # First player starts
                second_player_turn = False # Will be true when its second players turn
                
                 
            if first_player_turn:
                playing_now = first_player
                not_playing_now = second_player
                first_player_turn = False
                second_player_turn = True
            elif second_player_turn:
                playing_now = second_player
                not_playing_now = first_player
                second_player_turn = False
                first_player_turn = True
                
            print("\n"+playing_now.name+"'s Turn\n")
            valid_row = False
            valid_col = False
            while not valid_row:
                try:
                    row = input("Pick 1, 2 or 3\n1. Top\n2. Middle\n3. Bottom\n")
                    row_int = int(row)
                    if row_int > 3 or row_int < 1 :
                        raise Exception()
                    else:
                        row_index = int(row)-1 # For correct index 
                        valid_row = True   
                except Exception:
                    print("Invalid selection. Please select 1, 2 or 3")
                    valid_row = False
            
            
            while not valid_col:   
                try:
                    col = input("Pick 1, 2 or 3\n1. Left\n2. Middle\n3. Right\n")
                    col_int = int(col)
                    if col_int > 3 or col_int < 1:
                        raise Exception()
                    else:
                        col_index = int(col)-1 # For correct index
                        valid_col = True
                except Exception:
                    print("Invalid selection. Please select 1, 2 or 3")
                    valid_col = False
                    
            
            game_board.play_list(where=(row_index,col_index), who=playing_now.char, name = playing_now.name)
            if(game_board.check_status_list(spot=(row_index,col_index), who=playing_now.char)):
                player_won = True
                print(playing_now.name+" WON!\n")
                playing_now.add_score() # Add this players score
                print("Scores:\n"+first_player.name+": "+str(first_player.score)+" | "+second_player.name+": "+str(second_player.score)+"\n")
                replay = input("Play again?\nType Yes to play again...\n")
                if replay == "Yes":
                    game_count = game_count + 1
                    replay_game = True
                else:
                    print("GAME OVER!\n")
                    print("FINAL SCORES:\n"+first_player.name+": "+str(first_player.score)+" | "+second_player.name+": "+str(second_player.score))
                    if first_player.score > second_player.score:
                        print(first_player.name+" WON!")
                    elif second_player.score < first_player.score:
                        print(second_player.name+" WON!")
                    else:
                        print("TIE!")


            elif(game_board.spots_left==0):
                # If there are no spots left, the game is over
                game_over = True
                print("GAME OVER!")
                print("Scores:\n"+first_player.name+": "+str(first_player.score)+" | "+second_player.name+": "+str(second_player.score))
                replay = input("Play again?\nType Yes to play again...n")
                if replay == "Yes":
                    game_count = game_count+1
                    replay_game = True
                else:
                    print("GAME OVER!\n")
                    print("FINAL SCORES:\n"+first_player.name+": "+str(first_player.score)+" | "+second_player.name+": "+str(second_player.score))
                    if first_player.score > second_player.score:
                        print(first_player.name+" WON!")
                    elif second_player.score < first_player.score:
                        print(second_player.name+" WON!")
                    else:
                        print("TIE!")
        
              
# Call to main
if __name__ == "__main__":
    main()