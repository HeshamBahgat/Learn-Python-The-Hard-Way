"""
1- connection between browser and local host.
2- http request will be made to the ex50.py for the url.
3- ex.50 will send any url with / this is the default browser routes
4-
"""


from flask import Flask
from flask import render_template

app= Flask(__name__)


def second_url():
    return "Home Bage!"

@app.route("/")
@app.route("/home")
def hello_world():
    greeting = "Hello World"
    return render_template("~/PycharmProjects/Learn\ Python\ The\ Hard\ Way/home-page.html")

@app.route("/about")
def about_page():
    greeting = "Fans"
    return f"<h1>Hello, {greeting}!</h1>"




if __name__ == "__main__":
    app.run(debug=True)