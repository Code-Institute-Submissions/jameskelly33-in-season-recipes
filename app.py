import os


from flask import (Flask, flash, render_template, 
                  redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import calendar

if os.path.exists('env.py'):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] =os.environ.get("MONGO_URI")
app.secret_key =os.environ.get("SECRET_KEY")


mongo=PyMongo(app)


@app.route("/")
@app.route("/index.html")


def homepage():
    return render_template("index.html")


@app.route("/ingredients.html")


def ingredients():
    ingredients = mongo.db.ingredients.find()
    now = datetime.now()
    current_month = now.strftime("%m")
    this_month = "calendar.month_name[int(current_month)]"
    if this_month == "December":
        next_month = "January"
    else:
        next_month = calendar.month_name[(int(current_month))+ 1]
    
    return render_template('ingredients.html', ingredients = ingredients, this_month = this_month, next_month = next_month )

@app.route("/recipes.html")


def recipes():
    recipes = mongo.db.recipes.find()
    return render_template('recipes.html', recipes = recipes)

@app.route("/fullrecipe.html")


def getfullrecipe():
    return render_template("fullrecipe.html")

@app.route("/myrecipes.html")


def myrecipes():
    recipes = mongo.db.recipes.find()
    return render_template("myrecipes.html", recipes = recipes)

@app.route("/uploadrecipe.html")

def uploadrecipe():
    return render_template('uploadrecipe.html')





if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
