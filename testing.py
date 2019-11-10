#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'


import sys


def testing(test_type, player1_type, player2_type):
    '''test_type:get the rate 0, compare time 1
    '''
    import gamestate as g
    import player as p
    import gameoperator as game
    import experiment as e
    state = g.GameState()
    player1 = p.Player(1, player1_type)
    player2 = p.Player(2, player2_type)
    begin = game.GameOperator()
    m = e.TestMethod()
    if test_type == 0:
        # calculate win loss rate
        m.rate_calculate(state, begin, player1, player2)
    if test_type == 1:
        # calculate time gap
        m.compare_timing(state, begin, player1, player2)


if __name__ == "__main__":
    test_type = int(sys.argv[1])
    player1_type = int(sys.argv[2])
    player2_type = int(sys.argv[3])
    testing(test_type, player1_type, player2_type)
