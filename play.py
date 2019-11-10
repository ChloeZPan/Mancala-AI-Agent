#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'


import sys


def start(player1_type, player2_type):
    """human = 0, random = 1, minimax = 2,alphabeta = 3"""
    import gamestate as g
    import player as p
    import gameoperator as game
    state = g.GameState()
    player1 = p.Player(1, player1_type)
    player2 = p.Player(2, player2_type)
    begin = game.GameOperator()
    begin.startplay(state, player1, player2)


if __name__ == "__main__":
    player1_type = int(sys.argv[1])
    player2_type = int(sys.argv[2])
    start(player1_type, player2_type)

