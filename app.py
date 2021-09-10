# import flask web server
from flask import Flask, render_template

# import tic-tac-toe
from tictactoe import TicTacToe

# create flask app
app = Flask(__name__)

games = []


@app.route('/')
@app.route('/play')
@app.route('/home')
def index():
    game = TicTacToe()
    games.append(game)
    return render_template("home.html", game_number=game.get_n())

@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


if __name__ == '__main__':
    app.run(debug=True)



