# import flask web server
from flask import Flask, render_template

# create flask app
app = Flask(__name__)

@app.route('/')
@app.route('/play')
@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


if __name__ == '__main__':
    app.run(debug=True)



