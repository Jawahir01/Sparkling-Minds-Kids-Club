import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home Page route
@app.route("/")
def index():
    # username = mongo.db.users.find_one(
    #     {"username": session["user"]})["username"]
    # if session["user"]:
    #     return render_template("index.html", username=username)
    # else:
    return render_template("index.html")


# Courses route
@app.route("/courses")
def courses():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    courses = list(mongo.db.courses.find())
    return render_template("courses.html", courses=courses, username=username)


# User registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("This username has been already taken")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "first-name": request.form.get("first-name").lower(),
            "last-name": request.form.get("last-name").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "security-question": request.form.get("security-question").lower(),
            "security-answer": request.form.get("security-answer").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have been Successful! Registered")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# User signin route
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


# forgot_password
@app.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html")


# User Profile route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # List the courses for the child to choose from
    courses = list(mongo.db.courses.find())

    if session["user"]:
        children = list(mongo.db.kids.find({'username': username}))
        return render_template("profile.html", username=username,
                               children=children, courses=courses)


# Add Child route
@app.route("/add_child", methods=["GET", "POST"])
def add_child():
    # insert a child to DB based on user's session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    courses = list(mongo.db.courses.find())

    # Add new child to the user's list
    if request.method == "POST":
        child = {
            "username": session["user"],
            "childfname": request.form.get("childfname"),
            "childlname": request.form.get("childlname"),
            "date_of_birth": request.form.get("date_of_birth"),
            "school_name": request.form.get("school_name"),
            "school_year": request.form.get("school_year"),
            "child_choice": list(request.form.get("choice")),
            "child_med_conditions": request.form.get("child_med_conditions")
        }
        mongo.db.kids.insert_one(child)
        flash("Your Child hass been added successfully!")

    children = list(mongo.db.kids.find({'username': username}))
    return render_template("profile.html", children=children, courses=courses)


# Edit Child route
@app.route("/edit_child/<kids_id>", methods=["GET", "POST"])
def edit_child(kids_id):

    # update child details
    if request.method == "POST":
        update = {
            "username": session["user"],
            "childfname": request.form.get("childfname"),
            "childlname": request.form.get("childlname"),
            "date_of_birth": request.form.get("date_of_birth"),
            "school_name": request.form.get("school_name"),
            "school_year": request.form.get("school_year"),
            "child_choice": list(request.form.get("child_choice")),
            "child_med_conditions": request.form.get("child_med_conditions")
        }

        mongo.db.kids.update({"_id": ObjectId(kids_id)}, update)
        flash("Your Child's Details have been Successfully Updated")

    child = mongo.db.kids.find_one({"_id": ObjectId(kids_id)})
    children = list(mongo.db.kids.find({'username': username}))
    return render_template("profile.html", child=child, children=children)


# Signout route
@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
