# from shuffleCards import *

class readInput:
    global blank_dict, row1_dict, row2_dict, row3_dict, row4_dict
    def __init__(self):
        pass

    def readinputfile(self):
        global blank_dict, row1, row2, row3, row4
        blank_dict = {}
        input_file = open("input.txt", "r")
        mylist = []
        for line in input_file.readlines():
            # print(line)
            mylist.append(line.rstrip("\n"))
        # print(mylist)
        row1 = {k: v for k,v in enumerate(mylist[0:13])}
        row2 = {k: v for k,v in enumerate(mylist[13:26])}
        row3 = {k: v for k,v in enumerate(mylist[26:39])}
        row4 = {k: v for k,v in enumerate(mylist[39:52])}
        global board
        board = [row1,row2,row3,row4]
        print(board)
        for row in range(len(board)):
            for k,v in board[row].items():
                # key: location of blank, value: card to the left of blank
                if v == "blank":
                    blank_dict[(row, k)] = board[row][k-1]  

        print(blank_dict)
read = readInput()
read.readinputfile()

