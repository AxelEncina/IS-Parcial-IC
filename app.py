from flask import Flask
var = "Hola Mund";

app = Flask(__name__)

@app.route("/")

def index():
    return var

if __name__ == "__main__":
    app.run()

def index2():
    return