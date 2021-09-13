# ---------------------------------------------------------
# ---------------------------------------------------------
# This file implements the brute force approach to the front end of the game solver
# ---------------------------------------------------------
# ---------------------------------------------------------


import read_input as ri
import game_engine as ge

ri.readinputfile()


# --------------------------------------
# --------------------------------------
# def solve()
# description: calls appropriate functions to make valid moves
# --------------------------------------
# --------------------------------------


def solve():
    for k, v in ri.blank_dict:
        if k[1] == 0:
            # pick a 2
            candidate_card = ri.board[ri.twos[0][0]][ri.twos[0][1]]

        if len(v) == 2:
            candidate_card = str(int(v[0])+1)+v[1]
        elif len(v) == 3:
            candidate_card = str(int(v[:2]) + 1) + v[2]

        if ge.is_valid_move(k, candidate_card):
            ge.update_board(k, candidate_card)
        if ge.is_game_over():
            print("Game Over!")
            exit()


