import sqlite3
from flask import Flask, request, jsonify, g
 
app = Flask(__name__)

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
 
@app.route('/register', methods=['POST'])
def register():
    print "registering shit" + request.method

    if request.method == 'POST':
        print "POST REQUEST"
        name = request.form['name']
        ident = request.form['ident']
        purl = request.form['purl']
        headline = request.form['headline']

        print name
        print ident
        print purl
        print headline

        print "INSERT INTO DB"
        g.db.execute('insert into entries (name, ident, purl, headline) values (?, ?, ?, ?)', [name, ident, purl, headline])
        g.db.commit()
    
        print "BOOBS"
        return "BOOBS"

    return "REGISTRATION"

@app.route('/getnearby', methods=['GET'])
def getnearby(): 
    print "GETTING NEARBY PEOPLE"
    
    cur = g.db.execute('select name, ident, purl, headline from entries')
    entries = [dict(name=row[0], ident=row[1], purl=row[2], headline=row[3]) for row in cur.fetchall()]
    print entries 
    return jsonify({ 'users' : entries })

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host='0.0.0.0')
