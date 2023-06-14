from flask import Flask
var = "Hola Minoli";
var2 ="Hola Minoli"
var2 = var
app = Flask(__name__)

@app.route("/")

def index():
    return var

if __name__ == "__main__":
    app.run()

def index2():
    return