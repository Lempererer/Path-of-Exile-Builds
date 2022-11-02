from unittest import result
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

    #selects build names
    build_name_sql = '''
    SELECT build_name
    FROM builds
    '''
    cursor.execute(build_name_sql)
    build_name_results = cursor.fetchall()

    #retrieves the 'item_name' and 'item_id' from the database where 'item_type' = ?
    amulet_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(amulet_sql, ("amulet", ))
    amulet_results = cursor.fetchall()

    belt_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(belt_sql, ("belt", ))
    belt_results = cursor.fetchall()

    body_armour_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(body_armour_sql, ("body_armour", ))
    body_armour_results = cursor.fetchall()

    boots_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(boots_sql, ("boots", ))
    boots_results = cursor.fetchall()

    gloves_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(gloves_sql, ("gloves", ))
    gloves_results = cursor.fetchall()

    hand_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(hand_sql, ("hand", ))
    hand_results = cursor.fetchall()

    helmet_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(helmet_sql, ("helmet", ))
    helmet_results = cursor.fetchall()

    ring_sql = '''
    SELECT item_name, item_id
    FROM items
    WHERE item_type = ?
    '''
    cursor.execute(ring_sql, ("ring", ))
    ring_results = cursor.fetchall()

    #prints results of sql queries in the console. useful for debugging
    print(build_name_results)
    print(amulet_results)

    #makes the route use 'builds.html'. passes on all results from sql queries. 
    return render_template("builds.html", build_name_results = build_name_results, amulet_results = amulet_results, belt_results = belt_results, body_armour_results = body_armour_results, boots_results = boots_results, gloves_results = gloves_results, hand_results = hand_results, helmet_results = helmet_results, ring_results = ring_results)

#build page. dynamic route so that a created build can automatically have its own route. 
@app.route("/builds/<string:build_name>")
def build(build_name):
    cursor = get_db().cursor()

    #selects build names
    build_name_sql = '''
    SELECT build_name
    FROM builds
    WHERE build_name=?
    '''
    cursor.execute(build_name_sql, (build_name, ))
    build_name_results = cursor.fetchall()
    print(build_name_results)

    #retrieves the 'item_name' and 'item_id' from the database where 'item_type' = ?
    amulet_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.amulet_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(amulet_sql, (build_name, ))
    amulet_results = cursor.fetchall()
    print(amulet_results)

    belt_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.belt_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(belt_sql, (build_name, ))
    belt_results = cursor.fetchall()

    body_armour_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.body_armour_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(body_armour_sql, (build_name, ))
    body_armour_results = cursor.fetchall()

    boots_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.boots_id = items.item_id
    WHERE build_name= ?
    '''
    cursor.execute(boots_sql, (build_name, ))
    boots_results = cursor.fetchall()

    gloves_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.gloves_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(gloves_sql, (build_name, ))
    gloves_results = cursor.fetchall()

    main_hand_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.main_hand_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(main_hand_sql, (build_name, ))
    main_hand_results = cursor.fetchall()

    off_hand_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.off_hand_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(off_hand_sql, (build_name, ))
    off_hand_results = cursor.fetchall()

    helmet_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.helmet_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(helmet_sql, (build_name, ))
    helmet_results = cursor.fetchall()

    ring_1_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.ring_1_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(ring_1_sql, (build_name, ))
    ring_1_results = cursor.fetchall()

    ring_2_sql = '''
    SELECT items.item_img, items.item_id
    FROM builds
    JOIN items ON builds.ring_2_id = items.item_id
    WHERE build_name= ? 
    '''
    cursor.execute(ring_2_sql, (build_name, ))
    ring_2_results = cursor.fetchall()
    
    #makes the route use 'build.html' as a template. passes on all results from sql queries. 
    return render_template("build.html", build_name_results = build_name_results, amulet_results = amulet_results, belt_results = belt_results, body_armour_results = body_armour_results, boots_results = boots_results, gloves_results = gloves_results, main_hand_results = main_hand_results, off_hand_results = off_hand_results, helmet_results = helmet_results, ring_1_results = ring_1_results, ring_2_results = ring_2_results)

#add route to create new builds
@app.route("/add", methods=["GET", "POST"])
def add():
    print ("adding data")
    if request.method == "POST":
        cursor = get_db().cursor()

        #takes the input from the form and puts it into a new variable to be inserted into the database as a new build
        new_build_name = request.form["builds_build_name_id"]
        new_body_armour_id = request.form["select_body_armour"]
        new_helmet_id = request.form["select_helmet"]
        new_amulet_id = request.form["select_amulet"]
        new_gloves_id = request.form["select_gloves"]
        new_boots_id = request.form["select_boots"]
        new_ring_1_id = request.form["select_ring_1"]
        new_ring_2_id = request.form["select_ring_2"]
        new_main_hand_id = request.form["select_main_hand"]
        new_off_hand_id = request.form["select_off_hand"]
        new_belt_id = request.form["select_belt"]
        add_sql = '''
        INSERT INTO builds(build_name, body_armour_id, helmet_id, amulet_id, gloves_id, boots_id, ring_1_id, ring_2_id, main_hand_id, off_hand_id, belt_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(add_sql,(new_build_name, new_body_armour_id, new_helmet_id, new_amulet_id, new_gloves_id, new_boots_id, new_ring_1_id, new_ring_2_id, new_main_hand_id, new_off_hand_id, new_belt_id))
        get_db().commit()
    
    #after adding the build this takes user back to '/builds'
    return redirect("/builds")

#delete route to delete builds
@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        cursor = get_db().cursor()

        #takes the build name user enters into the delete form and sets it as 'build_name'
        build_name= str(request.form["delete_builds_build_name_id"])

        #deletes the build the user specifies
        sql = '''
        DELETE FROM builds 
        WHERE build_name = ?
        '''
        cursor.execute(sql,(build_name, ))
        get_db().commit()

    #after adding the build this takes user back to '/builds'
    return redirect("/builds")

#displays the item data images when user clicks on item in the grid. dynamic so that the same route can be used for all items in the database.
@app.route("/item/<int:item_id>")
def item_description(item_id):
    cursor = get_db().cursor()

    #retrieves the item data image corresponding with the id of the item the user clicks on
    sql = '''
    SELECT item_data_img
    FROM items
    WHERE item_id = ?
    '''
    cursor.execute(sql, (item_id, ))
    results = cursor.fetchall()

    #prints results of sql queries in the console. useful for debugging
    print(results)

    #makes the route use 'item_description.html' as a template
    return render_template("item_description.html", results = results)

#runs flask in terminal
if __name__ == "__main__":
    app.run(debug=True)