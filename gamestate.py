#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'


class GameState:
    def __init__(self, a=6, b=4):
        """ initialize game state, a is the number of pits, b is the number of stones in a pit
        set default a = 6, b = 4"""
        self.init_num_pits = a
        self.init_stone = b
        self.pits_num = self.init_num_pits
        self.store_score = [0, 0]
        self.pits_player1 = {k: self.init_stone for k in range(1, self.pits_num + 1)}
        self.pits_player2 = {k: self.init_stone for k in range(1, self.pits_num + 1)}

    def board(self):
        """ display game board which can update automatically"""
        board_set = "\t    "
        for i in range(self.pits_num, 0, -1):
            board_set += "   " + str(i) + "   "
        board_set += "\n"
        # board_set = "\t\t\t\t6\t\t5\t 4\t 3\t 2\t 1\n"
        board_set += "\t   -------------------------------------------\n"
        board_set += "   " + str(self.store_score[1]).zfill(2) + "      |  "
        for i in range(len(self.pits_player2) - 1, -1, -1):
            board_set += str(self.pits_player2[i + 1]).zfill(2) + "  |  "
        board_set += "(PLAYER 2)\n"
        board_set += "--------------------------------------------------------------------\n"
        board_set += "(PLAYER 1) |  "
        for i in range(0, len(self.pits_player1)):
            board_set += str(self.pits_player1[i + 1]).zfill(2) + "  |  "
        board_set += "   " + str(self.store_score[0]).zfill(2)
        board_set += "\n"
        board_set += "\t   -------------------------------------------\n"
        board_set += "\t    "
        for i in range(self.pits_num):
            board_set += "   " + str(i + 1) + "   "
        return board_set

    def reset(self, a=6, b=4):
        self.init_num_pits = a
        self.init_stone = b
        self.pits_num = self.init_num_pits
        self.store_score = [0, 0]
        self.pits_player1 = {k: self.init_stone for k in range(1, self.pits_num + 1)}
        self.pits_player2 = {k: self.init_stone for k in range(1, self.pits_num + 1)}

    def possible_actions(self, player):
        """ find all possible actions which are the pits with stones
        return
        actions: a dictionary of legal moves of a state whose key is the #pit \
        and value is number of stones in that pit
        """
        if player.player_num == 1:
            pits = self.pits_player1
        else:
            pits = self.pits_player2
        actions = {}
        for (npits, stones) in pits.items():
            # Check if key is even then add pair to new dictionary
            if stones != 0:
                actions[npits] = stones
        return actions

    def make_move(self, player, npits):
            """ make a move for the given player; sow stones along the player's pits, \
            if there are stones left, change to the opponent's side
            input
            (1) player: one of human/ random/ Minimax/ AlphaBeta
            (2) npits: the number of pits that the player choose, it is the key of possible actions
            return
            (1) turn: If turn is 0, this player can play again
            (2) pits: the state after the player's turn
            (3) opp_pits: the opponent's pits after the player's turn
            """
            if player.player_num == 1:
                pits = self.pits_player1
                opp_pits = self.pits_player2
            else:
                pits = self.pits_player2
                opp_pits = self.pits_player1
            stones = pits[npits]
            score = self.store_score
            # get all stones from the pit and the pit is empty
            pits[npits] = 0
            # move on to next pit
            npits += 1
            temp = pits
            turn = 1
            # if the player still have stones, keep going
            while stones > 0:
                turn = 1
                while npits <= len(pits) and stones > 0:
                    pits[npits] += 1
                    npits += 1
                    stones -= 1
                if stones == 0:  # when stone is used up, game over
                    # check if capture (the last stone falls into an empty pit)
                    if pits[npits - 1] == 1:
                        if opp_pits[7 - (npits - 1)] != 0:
                            score[player.player_num - 1] += 1 + opp_pits[7 - (npits - 1)]
                            pits[npits - 1] = 0
                            opp_pits[7 - (npits - 1)] = 0
                    break
                # if stones are not used up, then there must be a stone
                # been sowed into the player's store
                if pits == temp:
                    # check if change side, avoid add score repeatedly
                    score[player.player_num - 1] += 1
                    stones -= 1
                    turn = 0
                    # if not the last stone, keep looping, turn becomes 1 again
                # to change side
                other_temp = pits
                pits = opp_pits
                opp_pits = other_temp
                npits = 1
            return self.pits_player1, self.pits_player2, self.store_score, turn

    def terminal(self):
        """ check if game over"""
        over1 = False
        over2 = False
        if all(value == 0 for value in self.pits_player1.values()):
            self.store_score[1] += sum(self.pits_player2.values())
            self.pits_player2 = self.pits_player1
            over1 = True
        if all(value == 0 for value in self.pits_player2.values()):
            self.store_score[0] += sum(self.pits_player1.values())
            self.pits_player1 = self.pits_player2
            over2 = True
        if over1 or over2:
            return True
        else:
            return False

    def result(self, player_num):
        """ check if the player is a winner """
        opp_num = 3 - player_num
        if self.terminal():
            return self.store_score[player_num - 1] > self.store_score[opp_num - 1]
        else:
            return False

    def evaluate(self, player):
        """ get utility for this player given a state
        because it will take too long to explore to the bottom
        cannot set utility according to the final result
        just use the difference between player's scores"""
        if player.player_num == 1:
            return self.store_score[0] - self.store_score[1]
        elif player.player_num == 2:
            return self.store_score[1] - self.store_score[0]
