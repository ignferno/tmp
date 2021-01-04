from flask import Flask, render_template
import sqlite3
import random

app = Flask(__name__)

conn = sqlite3.connect('test.db')

conn.close()

@app.route('/')
def hello():
	out = []
	with sqlite3.connect("test.db") as con:
		cursor = con.execute("SELECT text, author from quote")
		for row in cursor:
			out += [f"\"{row[0]}\"-{row[1]}"]
		con.commit()
	outstr = random.choice(out)
	return render_template("main.html", e=outstr)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
