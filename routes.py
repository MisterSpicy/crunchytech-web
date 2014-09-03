import sqlite3
from flask import Flask, request, jsonify, g
 
app = Flask(__name__)

users = {}

# configuration
DATABASE = '/tmp/breeze.db'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    print "BEFORE REQUEST"
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    print "TEARDOWN REQUEST"
    db = getattr(g, 'db', None)
    if db is not None:
        print "DB IS NOT NONE"
        db.close()
 
@app.route('/')
def show_entries():
    cur = g.db.execute('select name, ident from entries')
    entries = [dict(name=row[0], ident=row[1]) for row in cur.fetchall()]
    print entries
    return "FUNBAGS"

@app.route('/register', methods=['POST'])
def register():
    print "registering shit" + request.method

    if request.method == 'POST':
        print "POST REQUEST"
        name = request.form['name']
        ident = request.form['ident']
        print name
        print ident

        print "INSERT INTO DB"
        g.db.execute('insert into entries (name, ident) values (?, ?)', [name, ident])
        g.db.commit()
    
        users['ident'] = name
        print "BOOBS"
        return "BOOBS"

    print new_dict['someshit']
    return "REGISTRATION"

@app.route('/getnearby', methods=['GET'])
def getnearby(): 
    print "GETTING NEARBY PEOPLE"
    
    cur = g.db.execute('select name, ident from entries')
    entries = [dict(name=row[0], ident=row[1]) for row in cur.fetchall()]
    print entries 
    return jsonify({ 'users' : entries })

if __name__ == '__main__':
  app.run(debug=True)
