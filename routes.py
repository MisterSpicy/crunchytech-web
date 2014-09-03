rom flask import Flask
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')
 
if __name__ == '__main__':
  app.run(host='0.0.0.0')

@app.route('/add', methods=['GET'])

def add_entry():
    return "HELLO WORLD"
