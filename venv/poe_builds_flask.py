from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)

DATABASE = "poe_builds_database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    return render_template("contents.html")

if __name__ == "__main__":
    app.run(debug=True)