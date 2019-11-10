#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'


import time
import sys


class GameOperator:
    def __init__(self):
        self.time_player1 = 0
        self.time_player2 = 0
        self.win_player1 = -1
        self.win_player2 = -1

    def startplay(self, gamestate, player1, player2):
        """ start a game between two players
        win 1 lose 0 draw 2"""
        curr_player = player1
        wait_player = player2
        # check if game over
        print('GAME START')
        print('PLAYER 1: {}\tPLAYER 2: {}'.format(curr_player.player_dict[curr_player.type],
                                                 wait_player.player_dict[wait_player.type]))
        time.sleep(1)
        sys.stderr.write(gamestate.board() + '\n')
        sys.stderr.flush()
        time.sleep(1)
        time_store = {1: [], 2: []}
        while not gamestate.terminal():
            turn = 0
            # 0 represents that game not over
            time_list = time_store.get(curr_player.player_num)
            while turn == 0 and not gamestate.terminal():
                print('PLAYER {}\'S TURN'.format(curr_player.player_num))
                start = time.time()
                move = curr_player.choose_move(gamestate)
                while move not in gamestate.possible_actions(curr_player):
                    print('{} is not valid'.format(move))
                    move = curr_player.choose_move(gamestate)
                end = time.time()
                time_used = end - start
                time_list.append(time_used)
                print('PLAYER {} {} made a move:'.format(curr_player.player_num,
                                                            curr_player.player_dict[curr_player.type]))
                sys.stdout.write(str(move) + '\n')
                sys.stderr.flush()
                time.sleep(1)
                print('TIME USED: {} seconds'.format(time_used))
                # TODO
                turn = gamestate.make_move(curr_player, move)[-1]
                time.sleep(1)
                sys.stderr.write(gamestate.board() + '\n')
                sys.stderr.flush()
                time.sleep(1)
            temp = curr_player
            curr_player = wait_player
            wait_player = temp
        self.time_player1 = sum(time_store.get(1)) / len(time_store.get(1))
        self.time_player2 = sum(time_store.get(2)) / len(time_store.get(2))
        if gamestate.result(player1.player_num):
            self.win_player1 = 1
            self.win_player2 = 0
            print('GAME OVER')
            time.sleep(1)
            sys.stderr.write(gamestate.board() + '\n')
            sys.stderr.flush()
            time.sleep(1)
            print('PLAYER 1 WINS !')
            print('PLAYER 1\'s time per move is {} seconds'.format(self.time_player1))
            print('PLAYER 2\'s time per move is {} seconds'.format(self.time_player2))
        elif gamestate.result(player2.player_num):
            self.win_player1 = 0
            self.win_player2 = 1
            print('GAME OVER')
            time.sleep(1)
            sys.stderr.write(gamestate.board() + '\n')
            sys.stderr.flush()
            time.sleep(1)
            print('PLAYER 2 WINS !')
            print('PLAYER 1\'s time per move is {}'.format(self.time_player1))
            print('PLAYER 2\'s time per move is {}'.format(self.time_player2))
        else:
            self.win_player1 = 2
            self.win_player2 = 2
            print('GAME OVER')
            time.sleep(1)
            sys.stderr.write(gamestate.board() + '\n')
            sys.stderr.flush()
            time.sleep(1)
            print('DRAW')
            print('PLAYER 1\'s time per move is {}'.format(self.time_player1))
            print('PLAYER 2\'s time per move is {}'.format(self.time_player2))
        return self.time_player1, self.time_player2, self.win_player1, self.win_player2

    def blindplay(self, gamestate, player1, player2):
        """ start a game between two players """
        curr_player = player1
        wait_player = player2
        time_store = {1: [], 2: []}
        while not gamestate.terminal():
            turn = 0
            # 0 represents that game not over
            time_list = time_store.get(curr_player.player_num)
            while turn == 0 and not gamestate.terminal():
                start = time.time()
                move = curr_player.choose_move(gamestate)
                while move not in gamestate.possible_actions(curr_player):
                    move = curr_player.choose_move(gamestate)
                end = time.time()
                time_used = end - start
                time_list.append(time_used)
                turn = gamestate.make_move(curr_player, move)[-1]
            temp = curr_player
            curr_player = wait_player
            wait_player = temp
        self.time_player1 = sum(time_store.get(1)) / len(time_store.get(1))
        self.time_player2 = sum(time_store.get(2)) / len(time_store.get(2))
        if gamestate.result(player1.player_num):
            self.win_player1 = 1
            self.win_player2 = 0
        elif gamestate.result(player2.player_num):
            self.win_player1 = 0
            self.win_player2 = 1
        else:
            self.win_player1 = 2
            self.win_player2 = 2
        return self.time_player1, self.time_player2, self.win_player1, self.win_player2
