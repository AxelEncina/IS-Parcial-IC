from flask import Flask
var = "Hola Minoli"
app = Flask(__name__)

@app.route("/")

def index():
    return var

if __name__ == "__main__":
    app.run()