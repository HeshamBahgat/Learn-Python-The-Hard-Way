
from flask import Flask
from flask import render_template

app= Flask(__name__)


def second_url():
    return "Home Bage!"

@app.route("/")
@app.route("/home")
def hello_world():
    greeting = "Hello World"
    return render_template("ex50-home.html")


if __name__ == "__main__":
    app.run(port= "4998", debug=True)
