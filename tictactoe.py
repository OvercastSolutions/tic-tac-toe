
class TicTacToe:
    """Create a Tic-Tac-Toe game object.

       * Each object is specific to a player.
    """

    def __init__(self):
        """Constructor for Tic-Tac-Toe object"""
        self.board = [['', '', ''],['', '', ''],['', '', '']]
        self.active = True
        self.winner = ''

    def __str__(self) -> str:
        """Board state in ascii style string"""
        result = "---|---|---\n"
        for row in self.board:
            result += "   |   |   \n"
            result += " {} | {} | {}  \n".format(row[0], row[1], row[2])
            result += "   |   |   \n"
            result += "---|---|---\n"

    def _set_state(self, col: int, row: int, value=' '):
        """Set the state of a cell in the game board"""
        self.board[row][col] = value[0].upper()

    def is_empty(self, col: int, row: int) -> bool:
        """Tell whether a cell is empty"""
        return self.board[row][col] != ''

    def check_win(self, piece) -> bool:
        # Check first row
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check second row
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check third row
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check first col
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check second col
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check third col
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check top left to bottom right diagonal
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        # Check bottom left to top right diagonal
        if((self.board[0][0] == self.board[0][0]) and (self.board[0][0] == self.board[0][0])):
            return True

        """Checks if the player with the given piece has won the game"""
        return False

    def is_stalemate(self) -> bool:
        """Tell whether the game is a stalemate"""
        return not self.active and self.winner == ''

    def turn(self, col: int, row: int, piece="?") -> int:
        assert len(piece) == 1
        if not self.is_empty(col, row):
            raise Exception("tic-tac-toe failure: {} {} already contains {}".format(col, row, self.board[row][col]))
            return
        self._set_state(col, row, piece)
        if self.check_win(piece):
            self.active = False
            self.winner = piece





