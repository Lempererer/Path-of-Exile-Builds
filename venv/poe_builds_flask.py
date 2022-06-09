from flask import Flask, g, render_template, redirect, request
import sqlite3

app = Flask(__name__)

#establishing database route
DATABASE = "venv\poe_builds_database.db"

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
    return render_template("index.html")

#builds page
@app.route("/builds")
def builds():
    return render_template("builds.html")

#page for build
@app.route("/build__impale-crit_cyclone_slayer")
def build():
    cursor = get_db().cursor()
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("build__impale-crit_cyclone_slayer.html", results = results)

#runs flask in terminal
if __name__ == "__main__":
    app.run(debug=True)