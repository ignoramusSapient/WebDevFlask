from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_wordl():
  return '<p>Hello, World!. This is the first code in Python for flask</p>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)