from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Homepage():
    return "API do Pc Gamer"

@app.route("/gpu")
def gamer():
    return render_template("placavídeo.html")

@app.route("/mobo")
def mobogamer():
    return render_template("placamae.html")

if __name__ == "__main__":
    app.run(debug=True)

