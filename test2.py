from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><body><h1>ようこそ</h1></body></html>'

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run("0.0.0.0")
