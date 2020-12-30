from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():

    conn = sqlite3.connect('dates.sqlite')
    cur = conn.cursor()
    dates = list()
    important = False
    for row in cur.execute('SELECT * FROM dates ORDER BY date desc'):
        dates.append({'date': row[1], 'event': row[2]})

    return render_template('index.html', dates=dates, important=important)


@app.route('/abridged')
def short():

    conn = sqlite3.connect('dates.sqlite')
    cur = conn.cursor()
    dates = list()

    for row in cur.execute('SELECT * FROM dates ORDER BY date desc'):
        if row[2][0] == "*":
            dates.append({'date': row[1], 'event': row[2]})

    return render_template('index.html', dates=dates)


@app.route('/about')
def about():

    return render_template('about.html')


if __name__ == '__main__':
    app.run()
