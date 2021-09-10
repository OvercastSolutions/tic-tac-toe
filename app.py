# import flask web server
from flask import Flask, render_template

# import tic-tac-toe
from tictactoe import TicTacToe

# create flask app
app = Flask(__name__)

games = []

def game_by_n(n: int) -> TicTacToe:
    global games
    for game in games:
        print("** comparing {} with {}".format(game.get_n(), n))
        if game.get_n() == n:
            print("** found game with id {}".format(n))
            return game
    print("** could not find game with id {}".format(n))
    return None

def print_current_games():
    global games
    result = "** current games: "
    for game in games:
        result += " {}".format(game.get_n())
    print(result)


@app.route('/')
@app.route('/home')
def index():
    global games
    game = TicTacToe()
    games.append(game)
    print_current_games()
    return render_template("home.html", game_n=game.get_n())

@app.route('/<number>')
def game(number: int): #TODO handle nonexistant games
    game = game_by_n(int(number))
    print_current_games()
    return render_template("home.html", game_n=game.get_n())

@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


if __name__ == '__main__':
    app.run(debug=True)



