#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'


import math
import copy
import random
import sys


class Player:
    player_dict = {0: 'human', 1: 'random', 2: 'minimax', 3: 'alphabeta'}

    def __init__(self, player_num, player_type):
        """initialize a Player
        (1) player_num: player1 or player2
            (2) player_type: numbers (human = 0, random = 1, minimax = 2,alphabeta = 3)
        """
        self.player_num = player_num
        self.opp_num = 3 - player_num
        self.type = player_type

    def __repr__(self):
        """show who is playing"""
        return 'PLAYER {} {} is playing'.format(self.player_num, self.player_dict[self.type])

    def choose_move(self, gamestate):
        """ get the move for the player, move is actually npits """
        if self.player_dict[self.type] == 'human':
            move = self.human_decision(gamestate)
            return move
        elif self.player_dict[self.type] == 'random':
            move = self.random_decision(gamestate)
            return move
        elif self.player_dict[self.type] == 'minimax':
            move = self.minimax_decision(gamestate)
            return move
        elif self.player_dict[self.type] == 'alphabeta':
            move = self.alphabeta_decision(gamestate)
            return move
        else:
            print('invalid player')
            return -1

    def human_decision(self, gamestate):
        move = int(input('Please enter your move:\n'))
        while move not in gamestate.possible_actions(self):
            sys.stderr.write('illegal move\n')
            move = int(input('Please enter your move:\n'))
        return move

    def random_decision(self, gamestate):
        d = gamestate.possible_actions(self)
        move = random.choice(list(d.keys()))
        return move

    def minimax_decision(self, gamestate, depth=5):
        """ Choose the best minimax move
        return
        move: the move to get the best utility
        """
        move = -1
        score = -math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            # pick stone in pit a
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            # opp's next move
            s = opp.minvalue(state_temp, depth - 1)
            # if the result is better than our best score, save the move
            if s > score:
                move = npits
                score = s
            if s == score:
                move = random.choice([move, npits])
                score = s
        return move

    def maxvalue(self, gamestate, depth):
        """ get minimax value for the maximer's next move"""
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = -math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            # pick stone in pit a
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            s = opp.minvalue(state_temp, depth - 1)
            if s > score:
                score = s
        return score

    def minvalue(self, gamestate, depth):
        """ get minimax value for the minimer's next move"""
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            # pick stone in pit
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            s = opp.maxvalue(state_temp, depth - 1)
            if s < score:
                score = s
        return score

    def alphabeta_decision(self, gamestate, depth=5):
        """ Choose the best alphabeta move
        return
        move: the move to get the best utility
        """
        move = -1
        alpha = -math.inf
        beta = math.inf
        score = -math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            # pick stone in pit a
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            s = opp.minab(state_temp, alpha, beta, depth - 1)
            # if the result is better than our best score, save the move and score
            if s > score:
                move = npits
                score = s
            if s == score:
                move = random.choice([move, npits])
                score = s
            alpha = max(score, alpha)
        return move

    def maxab(self, gamestate, alpha, beta, depth):
        """ get alpha-beta value for the maximer's next move"""
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = - math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            # pick stone in pit a
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            # opp chooses the larger score
            s = max(score, opp.minab(state_temp, alpha, beta, depth - 1))
            # if new score is larger than pruning
            if s >= beta:
                alpha = s
                return alpha
            alpha = max(alpha, s)
        return alpha

    def minab(self, gamestate, alpha, beta, depth):
        """ get alpha-beta value for the minimer's next move"""
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            # pick stone in pit a
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            # opp chooses the smaller score
            s = min(score, opp.maxab(state_temp, alpha, beta, depth - 1))
            # if new score is smaller than pruning
            if s <= alpha:
                beta = s
                return beta
            beta = min(beta, s)
        return beta
