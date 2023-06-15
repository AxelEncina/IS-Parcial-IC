from flask import Flask
var = "Hola Minoli";
var2 = "Hola Minoli";
var3 = "Hola Minoli";
var4 = "Hola Minoli";
var5 = "Hola Minoli"
var2= var
var3= var2
var3= var4
var4= var5

app = Flask(__name__)

@app.route("/")

def index():
    return var

if __name__ == "__main__":
    app.run()