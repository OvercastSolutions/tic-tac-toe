# import flask web server
from flask import Flask, render_template

# import tic-tac-toe
from tictactoe import TicTacToe

# create flask app
app = Flask(__name__)

games = []

def game_by_n(n: int) -> TicTacToe:
    """
    Checks if there is a loaded game of a given ID number.
    """
    global games
    for game in games:
        print("** comparing {} with {}".format(game.get_n(), n))
        if game.get_n() == n:
            print("** found game with id {}".format(n))
            return game
    print("** could not find game with id {}".format(n))
    return None

def print_current_games():
    """
    Prints the currently loaded games of tic-tac-toe.

    """
    global games
    result = "** current games: "
    for game in games:
        result += " {}".format(game.get_n())
    print(result)

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/new')
def new_game(): #TODO Make this not a route
    global games
    game = TicTacToe()
    games.append(game)
    print_current_games()
    return render_template("game.html", game_n=game.get_n())


# FUTURE ROUTES:
#@app.route('/n/<number>')   #See current board state
#@app.route('/n/<number>/x') #Play as X
#@app.route('/n/<number>/o') #Play as O

@app.route('/n/<number>')
def game(number: int): #TODO handle nonexistant games
    game = game_by_n(int(number))
    print_current_games()
    return render_template("home.html", game_n=game.get_n())

@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")

if __name__ == '__main__':
    app.run(debug=True)



