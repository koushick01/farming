from logging import error
from flask import Flask, render_template, redirect, request
from flask.helpers import flash
app = Flask(__name__)
MEMBERS = {}
name = ""


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/home")
def home():
     return render_template("home.html") 


@app.route("/fertilizer")
def fertiliser():
    return render_template("fertilizers.html")


@app.route("/weather")
def weather():
    return render_template("weather.html")


@app.route("/market")
def market():
    return render_template("market.html")


@app.route("/news")
def news():
    return render_template("news.html")  


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/team")
def team():
    return render_template("ourteam.html")



@app.route("/apple")
def apple():
    return render_template("apple.html")




@app.route("/banana")
def banana():
    return render_template("banana.html")


@app.route("/maize")
def maize():
    return render_template("maize.html")



@app.route("/mango")
def mango():
    return render_template("mango.html")


@app.route("/onion")
def onion():
    return render_template("onion.html")


@app.route("/potato")
def potato():
    return render_template("potato.html")



@app.route("/rice")
def rice():
    return render_template("rice.html")


@app.route("/tomato")
def tomato():
    return render_template("tomato.html")



@app.route("/wheat")
def wheat():
    return render_template("wheat.html")


@app.route("/next" , methods=["GET", "POST"])
def details():
    global name
    if request.method == "POST":    
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        if email in MEMBERS:
            message = "You are already registered"
            return render_template("login.html", message = message)
        else:
            MEMBERS[email] = password
            message = "Successfully registered"
            return render_template("login.html", message = message)


@app.route("/register", methods = ["GET", "POST"])
def entry():
    if request.method == "POST":
        lemail = request.form.get("email")
        lpassword = request.form.get("password")
        for lemail in MEMBERS:
            if MEMBERS[lemail] == lpassword:
                return render_template("home.html", name = name)
            else:
               message = "Invalid password or username"
               return render_template("login.html", message = message)              