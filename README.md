# Kalah-AI-Agent
## Introduction
The project is to design, implement and evaluate an AI bot to play a game named Mancala. Mancala is a two-player turn-based game. The AI agent is required to decide its move by using adversarial algorithms including minimax algorithm and  alpha-beta algorithm as well as by a random strategy. It is can also involve a human player. The report has three parts: program design, experiment and discussion. In program design part, it will mention architecture of the program, state/action representation, turn taking and handling equivalent moves. In experiment part, it will mention how to investigate skill of minimax, computational effectiveness of alpha-beta pruning, and first-choice bias and pie rule. In discussion part, it will mention what I learned and the challenges I met.

### 1. Program Design
#### 1.1 Architecture
In this game, we have three entities: players, gameboard and an operator. Players will have strategies to make the move. Here, we use an operator to help players to make move so that players are only thinking about what actions they should take. Gameboard will reflect the players’ moves based on the game rules (for example, moving counterclockwise, place the stones one by into the other cups on the board, one stone at a time and so on). We also need methods to calculate win/lose/draw rate and timing. According to the idea above, the program architecture will be:
![image](https://github.com/ChloeZPan/Kalah-AI-Agent/blob/master/image/figure1.PNG)
Figure 1: Architecture of the program
 
The program has 5 class: player, gameboard, experiment, play and testing. 

**Player.** It has 4 strategies and it needs to choose which strategy to use. Therefore, the choose move method is to take actions according to what strategy the player is using. 

**Operator.** It takes the actions as a representative of player. It has two methods. Start play method will show the state after each player makes a move. Blind play method will not show the board visually. This method aims to get a result in testing more quickly. 

**Gameboard.** Board display method visually displays a gameboard. Reset method can initialized the board. Possible actions contain the pits which are not empty. Make move method help the board to decide the number of stones in each pit, number of stones in each player’s Mancala store and whose next term it is. Evaluate method is actually only serve players using minimax and alpha-beta algorithms (it might be better in player class). Here, I used difference between stones in each player’s Mancala store as the utility of each move. Terminal method decides whether game over or not. Result method will return the number of stones in each player’s Mancala store and who will play in next turn after each move. 

**Experiment.** This class contains methods to do the tests. Rate calculation can calculate the win/lose/draw rate after 30 games. I set the default value to 30 in order to decrease bias. As it uses blind play method in Opetator, it will show the rounds instead of showing game boards. Compare timing method will calculate each player’s average time to sow the stones per game, and then calculate the time gap.

**Play.** This is the main method to play the game. 

**Testing.** This is the main method to do the tests.
Notice: In my actual code, the names may be slightly different. More details in my README.txt.

#### 1.2 state/action Representation and Turn Taking
The representation of state/action is mainly achieved by make move method in gameboard class. Consider the following situation: (1) Which pit to choose? (2) How will the state change when we choose a pit? (3) What will result from our last stone’s position?
#### (1) Which pit to choose? 
The possible actions method gives us and answer: we can only choose non-empty pits in our side. I used “if” statement to get the pits on the current player’s side and then check if the value is 0 or not.

####  (2) How will the state change when we choose a pit?
The pits we choose will become empty and the stones will be sowed into the pits following one by one. When the next is the current player’s store, put one stone into the store and then keep putting stone into the opponent’s pits. When the next is the opponent’s store, skip the store and keep sowing until the stones run out.
What is interesting here is how I decide whose side the player current on. We copy our pits right after we chose a pit. When we finish putting stones along our own side, we change to the opponent’s side. We can always check the side by comparing our current side by the copied one.

####  (3) What will result from our last stone’s position?
Except the normal situation, there are three special results according where our last stone be put. 
•	When the stone is put into our own store, the next turn will be our turn. 
•	When the stone is put into an empty pit but your opponent pit on the other side is not empty, the stone in the pit your last stone be placed and the stones in your opponent pit will all be placed into your store. 
•	When the last stone is put into your store and all your pits are empty, the game will be over.

#### 1.3 Handling equivalent moves
For player using minimax and alpha-beta pruning, we use the difference of score as the utility. What if several options have the same utility? My minimax and alpha-beta pruning will randomly choose one. The process will be if the current option has the same utility as the selected option, randomly choose one of them. The mechanism is to always compare the selected option with new option.

This also dramatically change the result. When using a “fixed ” strategy, it shows first-choice bias. When I used “random” strategy, the first-choice bias seems to disappear. In the experiment part, I will mention first-choice bias in more details.

### 2. Experiment and Evaluation
#### 2.1 Skill of Minimax
To investigate the skill of minimax, I used minimax strategy against random strategy. I also exchange the position of these strategy to avoid the possible first-choice bias. 

To get the win/lose/draw rate, I run the program to play for 30 times. 30 is a size which can be considered as large sample in statistics. Then, I get the average of 10 results (considering the time it will take I only get the average of 10). The results are as below.

#### Minimax vs Random
Table 1: Win/lose/draw rate of Minimax when against Random
![image](https://github.com/ChloeZPan/Kalah-AI-Agent/blob/master/image/Table1.png)

From the table, we can see Minimax beats Random in most games no matter it is the first player or second player. However, the win rate of minimax decreases when it become the second player. It could be a first-choice bias.

#### Minimax vs Alpha-Beta
Table 2: Win/lose/draw rate of Minimax when against Alpha-Beta
![image](https://github.com/ChloeZPan/Kalah-AI-Agent/blob/master/image/table2.png)

From the table, we can see Minimax and Alpha-beta pruning have almost the same perform when minimax is the first player. However, the win rate of minimax decreases when it becomes the second player. It could be a first-choice bias.

#### 2.2 Computational Effectiveness of Alpha-beta Pruning
To investigate the computational effectiveness of alpha-beta pruning, I played minimax against alpha-beta pruning for time times and get the time.
Table 3: How much Alpha-Beta is faster than Minimax
![image](https://github.com/ChloeZPan/Kalah-AI-Agent/blob/master/image/table3.png)

From the table, we can see Alpha-beta pruning is much faster than Minimax. This means pruning can effectively increase the speed of Alpha-Beta.

#### 2.3 First-Choice Bias and Pie Rule
To check if the first player has an advantage over the second player, I let these strategies implementation to against themselves. The results are as below.
Table 4: Win/lose/draw rate when against itself
![image](https://github.com/ChloeZPan/Kalah-AI-Agent/blob/master/image/table4.png)

From the table, we can see when Random vs Random, it is no advantage over the second player. When Minimax vs Minimax, the first player only has a slightly advantage. When alpha-beta vs alpha-beta, the win rate of first player is higher than the second player, but the gap is not huge. As the sample size is only run 30 times to get rates and repeat 10 times to get average, we cannot conclude we don’t have the first-choice bias. It requires further investigation.

### 3 Discussion
#### 3.1 What Learned
(1) Deep and comprehensive understanding of mechanism of minimax and alpha-beta pruning
The process of transferring pseudo code to actual code is not easy. There are a lot of details you need to consider. I need to understand what the algorithms exactly do so that when I run into an error, I know how to figure a way out. For example, with a good understanding of these algorithms, when my program takes a long time to execute, I knew at once I needed to cut off at a certain depth.

(2) Basic coding skill using python
This one is the longest project I wrote using python. From the project, I know what __init__and__repr__ are used for. I know the concept of standard out and standard error. Also, I know some cool methods from outsourcing modules such as sys and time.

(3)Program design and experiment design
In this project, I gain experience of design program and use experiment to do some test. I notice to get a structure is quite important. I get to figure out the architecture before I get start and keep adjusting the structure while coding.
Unfortunately, but also fortunately, I don’t have a partner in this project. I spent a LOT of time on it, however, I get a comprehensive understanding of this project and improve my ability to deal with a problem from the beginning to the end.

(4) Patience to learn new things and calm to handle difficulties
The last but not the least, I learn the importance of patience and calm when you are facing a challenge. I spent a long time learning python’s basic knowledge in order to doing this project in python. I also spent time on reading the text book and search online to get a better understanding of the algorithms. I think my effort worth it.

#### 3.2 Challenges
How to choose a proper evaluation function?
In the program, I choose the difference of the scores as the utility. However, there are other options. For example, the best move could be the one that will let you keep playing (always choose to put your last stone into your own store). The best move can also be the one that can get a “capture” (put the last stone into an empty pit and get your opponent’s stones). Also, the best move can be the one that let you put as many as possible stones on your side, and then let your opponent finishes the game first so that all stones on your side will be put into your store.
The current minimax and alpha-beta pruning will only consider one of these best move options which is let the gap of the scores larger. In the last situation I mentioned above, it may not be an efficient way to beat your opponent. This is why the adversarial algorithms implementation here cannot always beat random player with an overwhelming score.

How to decide where to cut-off?
In the program, I set the depth to 5 as default in order to shorten the time for adversarial algorithms to make a decision. However, this will decrease the skill of both minimax and alpha-beta pruning. The problem is also related to the evaluation function one because you cannot directly compare the final results. Instead, you need to rely on your evaluation function.
