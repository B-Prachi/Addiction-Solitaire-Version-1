# from shuffleCards import *
"""
- Reads the input file line by line and stores in 4 dictionaries, one for each row with 13 columns.
  row = { <col_num>: <card_on_that_location> }
- 4 dictionaries stored in a list named 'board'
  board = [ {<row1>}, {<row2>}, {<row3>}, {<row4>} ]
- A ditionary named 'blank_dict' that stores the blank location in a tuple (<row_num>, <col_num>) as key and
  value as the card to the left of the blank location.
  blank_dict = { (<row_num>, <col_num>): <card_to_left_of_blank> }
"""

class readInput:
    def __init__(self):
        pass

    def readinputfile(self):
        global blank_dict, row1, row2, row3, row4
        blank_dict = {}
        input_file = open("input.txt", "r")
        mylist = []
        for line in input_file.readlines():
            mylist.append(line.rstrip("\n"))
        row1 = {k: v for k,v in enumerate(mylist[0:13])}
        row2 = {k: v for k,v in enumerate(mylist[13:26])}
        row3 = {k: v for k,v in enumerate(mylist[26:39])}
        row4 = {k: v for k,v in enumerate(mylist[39:52])}
        global board
        board = [row1, row2, row3, row4]
        print(board)
        for row in range(len(board)):
            for k, v in board[row].items():
                # key: location of blank, value: card to the left of blank
                if v == "blank":
                    blank_dict[(row, k)] = board[row][k-1]


read = readInput()
read.readinputfile()

