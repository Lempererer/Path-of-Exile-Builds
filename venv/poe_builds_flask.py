from flask import Flask, g, render_template, redirect, request, url_for
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
    cursor = get_db().cursor()
    sql = "SELECT build_name FROM builds"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("builds.html", results = results)

#impale cyclone page
@app.route("/impale_cyclone")
def impale_cyclone():
    cursor = get_db().cursor()
    sql = '''
    SELECT build_name, amulet.amulet_img, belt.belt_img, body_armour.body_armour_img, boots.boots_img, gloves.gloves_img, helmet.helmet_img, main_hand.main_hand_img, off_hand.off_hand_img, ring_1.ring_img, ring_2.ring_img
    FROM builds
    JOIN amulet ON builds.amulet_id = amulet.amulet_id
    JOIN belt ON builds.belt_id = belt.belt_id
    JOIN body_armour ON builds.body_armour_id = body_armour.body_armour_id
    JOIN boots ON builds.boots_id = boots.boots_id
    JOIN gloves ON builds.gloves_id = gloves.gloves_id
    JOIN helmet ON builds.helmet_id = helmet.helmet_id
    JOIN main_hand ON builds.main_hand_id = main_hand.main_hand_id 
    JOIN off_hand ON builds.off_hand_id = off_hand.off_hand_id
    JOIN ring_1 ON builds.ring_1_id = ring_1.ring_id
    JOIN ring_2 ON builds.ring_2_id = ring_2.ring_id
    WHERE build_name='Impale Cyclone';
    '''
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("impale_cyclone.html", results = results)

#righteous fire/fire trap page
@app.route("/righteous_fire")
def righteous_fire():
    cursor = get_db().cursor()
    sql = '''
    SELECT build_name, amulet.amulet_img, belt.belt_img, body_armour.body_armour_img, boots.boots_img, gloves.gloves_img, helmet.helmet_img, main_hand.main_hand_img, off_hand.off_hand_img, ring_1.ring_img, ring_2.ring_img FROM builds 
    JOIN amulet ON builds.amulet_id = amulet.amulet_id
    JOIN belt ON builds.belt_id = belt.belt_id
    JOIN body_armour ON builds.body_armour_id = body_armour.body_armour_id
    JOIN boots ON builds.boots_id = boots.boots_id
    JOIN gloves ON builds.gloves_id = gloves.gloves_id
    JOIN helmet ON builds.helmet_id = helmet.helmet_id
    JOIN main_hand ON builds.main_hand_id = main_hand.main_hand_id 
    JOIN off_hand ON builds.off_hand_id = off_hand.off_hand_id
    JOIN ring_1 ON builds.ring_1_id = ring_1.ring_id
    JOIN ring_2 ON builds.ring_2_id = ring_2.ring_id
    '''
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("righteous_fire.html", results = results)

#runs flask in terminal
if __name__ == "__main__":
    app.run(debug=True)