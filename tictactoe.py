



class TicTacToe:
    """Create a Tic-Tac-Toe game object.

       * Each object is specific to a player.
    """

    def __init__(self):
        self.board = [['', '', ''],['', '', ''],['', '', '']]

    def __str__(self):
        result = "---|---|---\n"
        for row in self.board:
            result += "   |   |   \n"
            result += " {} | {} | {}  \n".format(row[0], row[1], row[2])
            result += "   |   |   \n"
            result += "---|---|---\n"

    def _set_state(self, col, row, value=' '):
        self.board[row][col] = value[0].upper()






