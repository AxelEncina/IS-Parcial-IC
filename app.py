from flask import Flask
var = "Hola Mundo";
var2 = "Hola Mundo";
var3 = "Hola Mundo";
var4 = "Hola Mundo";
var5 = "Hola Mundo"
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