from flask import Flask
<<<<<<< HEAD
var = "Hola Minoli"

=======
var = "Hola Mundo";
var = "Hola Mundo";
var = "Hola Mundo";
var2 = var
var3 = var2
var4 = var3
>>>>>>> d8b63294e1676e509ccad26478e22bd019837560
app = Flask(__name__)

@app.route("/")

def index():
    return var4

if __name__ == "__main__":
    app.run()

def index2():
    return