from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)

#the database
DATABASE = "poe_builds_database.db"

#connecting to database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#disconnecting to database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#home page
@app.route("/")
def home():
    return render_template("contents.html")

#runs flask in terminal
if __name__ == "__main__":
    app.run(debug=True)