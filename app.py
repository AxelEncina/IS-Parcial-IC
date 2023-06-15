from flask import Flask
var = "Hola Mundo cruel";

app = Flask(__name__)

@app.route("/")

def index():
    return var

if __name__ == "__main__":
    app.run()
7
def index2():
    return