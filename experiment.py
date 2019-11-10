#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'


class TestMethod:
    def __init__(self):
        self.win_rate = 0
        self.loss_rate = 0
        self.draw_rate = 0
        self.oppwin_rate = self.loss_rate
        self.opploss_rate = self.win_rate
        self.oppdraw_rate = self.draw_rate
        self.time_gap = 0

    def rate_calculate(self, gamestate, gameop, player1, player2, n=30):
        '''Rate are player 1's rate
        The opponent's rate are easy to calculate'''
        win = 0
        loss = 0
        draw = 0
        r = 1
        while r <= n:
            gamestate.reset()
            gameop.blindplay(gamestate, player1, player2)
            print('Round {}'.format(r))
            if gameop.win_player1 == 1:
                win += 1
            elif gameop.win_player1 == 0:
                loss += 1
            elif gameop.win_player1 == 2:
                draw += 1
            else:
                return -1, -1, -1
            r += 1
        self.win_rate = win/n
        self.loss_rate = loss/n
        self.draw_rate = draw/n
        print('WIN rate: {} / {}'.format(win, n))
        print('LOSE rate: {} / {}'.format(loss, n))
        print('DRAW rate: {} / {}'.format(draw, n))
        return self.win_rate, self.loss_rate, self.draw_rate

    def compare_timing(self, gamestate, gameop, player1, player2):
        gameop.blindplay(gamestate, player1, player2)
        t1 = gameop.time_player1
        t2 = gameop.time_player2
        self.time_gap = t1 - t2
        print('PLAYER 1 is {} seconds [SLOWER] than PLAYER 2'.format(self.time_gap))
        return self.time_gap
