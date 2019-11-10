# Kalah-AI-Agent
## Introduction
The project is to design, implement and evaluate an AI bot to play a game named Mancala. Mancala is a two-player turn-based game. The AI agent is required to decide its move by using adversarial algorithms including minimax algorithm and  alpha-beta algorithm as well as by a random strategy. It is can also involve a human player. The report has three parts: program design, experiment and discussion. In program design part, it will mention architecture of the program, state/action representation, turn taking and handling equivalent moves. In experiment part, it will mention how to investigate skill of minimax, computational effectiveness of alpha-beta pruning, and first-choice bias and pie rule. In discussion part, it will mention what I learned and the challenges I met.

### 1. Program Design
#### 1.1 Architecture
In this game, we have three entities: players, gameboard and an operator. Players will have strategies to make the move. Here, we use an operator to help players to make move so that players are only thinking about what actions they should take. Gameboard will reflect the players’ moves based on the game rules (for example, moving counterclockwise, place the stones one by into the other cups on the board, one stone at a time and so on). We also need methods to calculate win/lose/draw rate and timing. According to the idea above, the program architecture will be:
![image](http://github.com/ChloeZPan/Kalah-AI-Agent/edit/master/image/figure1.png)
