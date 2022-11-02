# File: ControlGame.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 4/8/22
# Description of Program: two player board of strategy 
class ControlGame:
    def __init__(self, turnsToPlay):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].
        MAX_TURNS=64
        if turnsToPlay <= MAX_TURNS:
            MAX_TURNS=turnsToPlay
        self.__turnsToPlay=MAX_TURNS
        self.__EMPTY_BOARD = [ [ '.' for col in range(8) ] for row in range(8) ]
        self.__CurrentPlayer = 'Red'
 

    def __str__(self):

        # Permit displaying the header "Current board is:" following by the
        # board.
        xx = []
        board = "\nCurrent board is:\n"
        board += "  "
        for kk in range(0,8):
            xx.append(kk)
        board += " ".join(str(element) for element in xx)
        board += "\n"
        for ii in xx:
            zz=[]
            for jj in xx:
                zz.append(self.__EMPTY_BOARD[ii][jj])
            board+= "%s %s\n" %(ii," ".join(zz))
        return board

           

    def getCurrentPlayer(self):
        # Return the current player, 'Red' or 'Blue'
        return self.__CurrentPlayer

 

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and
        # vice versa
        if self.__CurrentPlayer == 'Red':
            self.__CurrentPlayer = 'Blue'
        else:
            self.__CurrentPlayer = 'Red'


    def getBoardState(self):
        # Return the current board.
        return self

 

    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value
        # indicating whether or not the turn occurred.
        if row<0 or row>7 or col<0 or col>7:
            print("Invalid turn. Location is out of bounds.")
            return False
        elif self.__EMPTY_BOARD[row][col] == ".":
           gtoken = ''
           player = self.getCurrentPlayer()
           if player == 'Red':
               gtoken = 'R'
           else:
               gtoken = 'B'
           self.__EMPTY_BOARD[row][col] = gtoken
           self.swapCurrentPlayer()
           return True
        else:
            print("Invalid turn. Cannot place piece on occupied cell.")
            return False

 

    def getRowColScore(self, stype):
        score = {}
        score_red = 0
        score_blue = 0
        for ii in range(0,8):
            count_red = 0
            count_blue = 0
            for jj in range(0,8):
                player = ''
                if stype == 'row':
                    # Search rows
                    player = self.__EMPTY_BOARD[ii][jj]
                else:
                    # Search cols
                    player = self.__EMPTY_BOARD[jj][ii]
                if player == 'R':
                    count_red += 1
                elif player == 'B':
                    count_blue += 1
            if count_red > 0 or count_blue > 0:
                if count_red > count_blue:
                    score_red += 1
                elif count_blue > count_red:
                    score_blue += 1
        return score_red, score_blue

 

 

    def checkCells(self, token, row, col):

        token_match = 0
        # Check up.
        if row >= 1 and self.__EMPTY_BOARD[row-1][col] == token:
            token_match += 1
        # Check down.
        if row <=6 and self.__EMPTY_BOARD[row+1][col] == token:
            token_match += 1
        # Check left.
        if col >= 1 and self.__EMPTY_BOARD[row][col-1] == token:
            token_match += 1
        # Check right.
        if col <=6 and self.__EMPTY_BOARD[row][col+1] == token:
            token_match += 1
        if token_match >= 2:
            return True
        return False

 

    def getCellScore(self):
        score_red = 0
        score_blue = 0
        for ii in range(0,8):
            for jj in range(0,8):
                player = self.__EMPTY_BOARD[ii][jj]
                row = ii
                col = jj
                if player == 'R':
                    if self.checkCells(player, row, col):
                        score_red += 1
                elif player == 'B':
                    if self.checkCells(player, row, col):
                        score_blue += 1
        return score_red, score_blue


    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea
        # to write subsidiary functions for this.
    
        row_score_red, row_score_blue = self.getRowColScore('row')
        col_score_red, col_score_blue = self.getRowColScore('col')
        cell_score_red, cell_score_blue = self.getCellScore()

        score_red = row_score_red + col_score_red + cell_score_red
        score_blue = row_score_blue + col_score_blue + cell_score_blue

        return score_red, score_blue
 
