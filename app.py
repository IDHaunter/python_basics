from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/second")
def second_route():
    return "<p>Это второй endpoint!</p>"

if __name__ == '__main__':
    app.run(debug=True)