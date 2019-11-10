Project 1: Game Playing
----------------------
Commend Line Arguments
----------------------

----Play the game-----
-for LINUX
(1)rename file: mv play.py play
(2)make it executable: chmod +x play
(3)execute: 
./play player1 player2
(enter number at player1 and player2 positions, human = 0, random = 1, minimax = 2,alphabeta = 3)
e.g ./play 2 3
let minimax against alphbeta

-for Windows
execute:
python play.py player1 player2
(player1 and player2 also be numbers)

-----Testing-----
-for LINUX
(1)rename file: mv testing.py testing
(2)make it executable: chmod +x testing
(3)execute: 
./testing test_type player1_type player2_type
(enter number at player1_type and player2_type positions, 0 human, 1 human, 2 minimax, 3 alphabeta)
(enter number at test_type position, 0 win/lose/draw rate, 1 time gap)
e.g ./testing 0 2 3
get the win/lose/draw rate when minimax against alphbeta

-----------------
Introductory Info
-----------------
The src directory has a README.txt and 6 python files.

(1) gamestate.py
GameState: a class about state of the game. 
boad(): display the gameboard
reset(): initialize the board (six pits per player and four stones per pit)
possible_actions(): provide the valid move. the non-empty pits on the current player's side
make_move(player, npits): change the state according to the move and decide who is to play next and if game is over
terminal(): check is game over
result(): check who is the winner
evaluate(player): for minimax and alphabeta only. the utility the player will get for a certain move

(2) player.py
Player: a class about information of a player
player_num: player 1 or player 2
opp_num: opponent is player 1 or player 2
type: (human = 0, random = 1, minimax = 2,alphabeta = 3)
choose_move(gamestate): use what strategy to make move
human_decision(gamestate): when involve a human player, prompt the player to input
random_decision(gamestate): make move randomly
minimax_decision(gamestate, depth=5): implement minimax algorithms
maxvalue(gamestate, depth): act as maximer in minimax algorithms
minvalue(gamestate, depth): act as minimer in minimax algorithms
alphabeta_decision(gamestate, depth=5): implement alphbeta pruning
maxab(gamestate, depth): decide value of alpha
minab(gamestate, depth): decide value of beta

(3) gameoperator.py
GameOperator: play the game
startplay(gamestate, player1, player2): play the game by displaying the board after each move
blindplay(gamestate, player1, player2): for testing use. play the game without displaying the board.

(4) experiment.py
rate_calculate(gamestate, gameop, player1, player2, n=30): calculate the win/lose/draw rate by repeatedly playing the game for 30 time(default).
compare_timing(gamestate, gameop, player1, player2): calculate the time gap between two players

(5) play.py
door to play the game
start(player1_type, player2_type): start the game by entering two players

(6) testing.py
door to do tests
testing(test_type, player1_type, player2_type): test_type(0 or 1, 0 is to calculate rate, 1 is to calculate time gap)

-----------
Author Info
-----------
Name: Zeyi Pan
UR ID: 31633987
 

