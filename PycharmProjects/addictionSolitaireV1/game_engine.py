# ---------------------------------------------------------
# ---------------------------------------------------------
# This file implements the brute force approach to the backend of the game
# ---------------------------------------------------------
# ---------------------------------------------------------


import read_input

read_input.readinputfile()


# ------------------------
# ------------------------
# def get_left_of_blank(blank_loc)
# parameter: blank_loc
# description: gets the card to the left of the blank location from blank_dict
# returns a string which is the card to the left of blank
# ------------------------
# ------------------------


def get_left_of_blank(blank_loc):
    return read_input.blank_dict[blank_loc]

# ------------------------
# ------------------------
# def is_left_smaller(left, candidate_card)
# parameter: left - card to the left of blank_location
#            candidate_card - card that can go on the blank location
# description: Checks if the candidate_card is greater than the card to the left of blank by 1
# returns True if the card to the left is smaller than candidate card, else returns False
# ------------------------
# ------------------------


def is_left_smaller(left, candidate_card):
    if len(candidate_card) == 3:
        if int(candidate_card[:2])-1 == int(left[0]):
            return True
    if len(candidate_card) == 2 and candidate_card.isalpha():
        if candidate_card[0] == 'J' and int(left[0]) == 10:
            return True
        elif candidate_card[0] == 'Q' and left[0] == 'J':
            return True
        elif candidate_card[0] == 'K' and left[0] == 'Q':
            return True
    if len(candidate_card) == 2 and candidate_card.isalnum():
        if int(candidate_card[0])-1 == int(left[0]):
            return True
    return False


# ------------------------
# ------------------------
# def is_same_suit(left, candidate_card)
# parameter: left - card to the left of blank_location
#            candidate_card - card that can go on the blank location
# description: Checks if the candidate_card is of the same suit as that of the card to the left of blank
# returns True if the card to the left card belongs to the same suit, else returns False
# ------------------------
# ------------------------


def is_same_suit(left, candidate_card):
    if left[-1] == candidate_card[-1]:
        return True
    return False


# ------------------------
# ------------------------
# def is_valid_move(blank_loc, candidate_card)
# parameters: blank_loc - tuple of row and col representing the location of blank on the board
#             candidate_card - string type, card to be moved to the blank location on board
# description: Checks if the move is valid
# returns True if all conditions are True, else returns False
# ------------------------
# ------------------------


def is_valid_move(blank_loc, candidate_card):
    left = get_left_of_blank(blank_loc)

    if candidate_card[0] != '2' and read_input.blank_dict[blank_loc] is not None:
        return False
    if not is_left_smaller(left, candidate_card):
        return False
    if not is_same_suit(left, candidate_card):
        return False
    return True

# ------------------------
# ------------------------
# def is_game_over()
# description: Checks if all the blank spaces are after the King card on board
# if yes, returns True, meaning that reshuffling is required
# if not, returns False, meaning that the game can be continued and moves can be made
# ------------------------
# ------------------------


def is_game_over():
    blank_dict_val = list(read_input.blank_dict.values())
    if len(blank_dict_val) == 1 and blank_dict_val[0][0] == 'K':
        return True

# ------------------------
# ------------------------
# def get_card_loc(card)
# parameter: card - string whose location is to be found
# description: get the location of any card from the board
# returns a tuple of row and column where the card is located on the board
# ------------------------
# ------------------------


def get_card_loc(card):
    for i in range(len(read_input.board)):
        for k, v in read_input.board[i].items():
            if v == card:
                return i, k

# ------------------------
# ------------------------
# def update_board(blank_loc, candidate_card)
# parameter: blank_loc - tuple of row and column where there is blank
#            candidate_card - string type, card to be moved to blank location
# Description: Delete the old blank_loc from blank_dict
#              Move the candidate card to the blank location on board
#              Add new blank_loc as the location of Candidate_card on the board
#              update the blank_dict dictionary
# ------------------------
# ------------------------


def update_board(blank_loc, candidate_card):
    # getting the location of candidate card from the board
    candidate_card_loc = get_card_loc(candidate_card)

    # row and col number of candidate card form board
    candidate_card_row = candidate_card_loc[0]
    candidate_card_col = candidate_card_loc[1]

    # row and col number for blank location
    blank_row = blank_loc[0]
    blank_col = blank_loc[1]

    # Deleting the old blank_location from blank_dict
    del read_input.blank_dict[blank_loc]

    # updating the board
    read_input.board[blank_row][blank_col] = candidate_card
    read_input.board[candidate_card_row][candidate_card_col] = "blank"

    # updating the blank_dict
    read_input.blank_dict[candidate_card_loc] = read_input.board[candidate_card_row][candidate_card_col-1]
