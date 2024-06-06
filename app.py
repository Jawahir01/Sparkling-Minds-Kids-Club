import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import (date, datetime, timedelta)
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
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("index.html", username=username)
    else:
        return render_template("index.html")


# Courses route
@app.route("/courses")
def courses():
    courses = list(mongo.db.courses.find())
    if session["user"]:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template(
            "courses.html", courses=courses, username=username)
    else:
        return render_template("courses.html", courses=courses)


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
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # Check if Security Question and answer match the user input
            if (existing_user.get("security-question") == request.form.get
                ("security-question")) and (existing_user.get(
                    "security-answer") == request.form.get("security-answer")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(
                    request.form.get("username")))
                return render_template("update_password.html")
            else:
                # invalid answer
                flash("Incorrect Username and/or Answer")
                return redirect(url_for("forgot_password"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Answer")
            return redirect(url_for("signin"))

    return render_template("forgot_password.html")


# Update Password
@app.route("/update_password/<username>", methods=["GET", "POST"])
def update_password(username):

    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if request.method == "POST":
        update = {
            "username": user["username"],
            "password": generate_password_hash(
                request.form.get("password")),
            "first-name": user["first-name"],
            "last-name": user["last-name"],
            "email": user["email"],
            "security-question": user["security-question"],
            "security-answer": user["security-answer"]

        }

        mongo.db.users.replace_one({"_id": ObjectId(user["_id"])}, update)
    courses = list(mongo.db.courses.find())
    children = list(mongo.db.kids.find({'username': username}))
    flash("Your New password has been Successfully Updated")
    return render_template(
        "profile.html", username=username, children=children, courses=courses)


# User Profile route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    courses = list(mongo.db.courses.find())
    children = list(mongo.db.kids.find({'username': username}))

    # Initialize child variable
    child = None

    # Attempt to find the kids_id from the request parameters
    kids_id = request.args.get("kids_id")
    if kids_id:
        try:
            child = mongo.db.kids.find_one({"_id": ObjectId(kids_id)})
        except InvalidId:
            flash("Invalid child ID")
    return render_template(
        "profile.html", username=username, children=children,
        child=child, courses=courses)


# Age Function
def calculate_age(born):
    today = datetime.now()
    age = today.year - born.year - (
        (today.month, today.day) < (born.month, born.day))
    return age


# Add Child route
@app.route("/add_child", methods=["GET", "POST"])
def add_child():
    # insert a child to DB based on user's session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    courses = list(mongo.db.courses.find())

    # Add new child to the user's list
    if request.method == "POST":
        username = session["user"]
        childfname = request.form.get("childfname")
        childlname = request.form.get("childlname")
        date_of_birth = datetime.strptime(
            request.form["date_of_birth"], '%Y-%m-%d'
        )
        age = calculate_age(date_of_birth)
        school_name = request.form.get("school_name")
        school_year = request.form.get("school_year")
        child_choice = request.form.getlist("child_choice")
        child_med_conditions = request.form.get("child_med_conditions")

        if 6 <= age <= 15:
            child = {
                "username": username,
                "childfname": childfname,
                "childlname": childlname,
                "date_of_birth": date_of_birth.strftime('%Y-%m-%d'),
                "school_name": school_name,
                "school_year": school_year,
                "child_choice": child_choice,
                "child_med_conditions": child_med_conditions
            }
            mongo.db.kids.insert_one(child)
            flash("Your Child has been added successfully!")

        else:
            flash("Unfortunately, you\'re age is not qualified for our club")

    children = list(mongo.db.kids.find({'username': username}))
    return redirect(url_for("profile", username=session["user"]))


# Edit Child route
@app.route("/edit_child/<kids_id>", methods=["GET", "POST"])
def edit_child(kids_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    courses = list(mongo.db.courses.find())
    children = list(mongo.db.kids.find({'username': username}))
    child = mongo.db.kids.find_one({"_id": ObjectId(kids_id)})

    if request.method == "POST":
        update_child = {
            "username": session["user"],
            "childfname": request.form.get("childfname"),
            "childlname": request.form.get("childlname"),
            "date_of_birth": request.form.get("date_of_birth"),
            "school_name": request.form.get("school_name"),
            "school_year": request.form.get("school_year"),
            "child_choice": request.form.getlist("child_choice"),
            "child_med_conditions": request.form.get("child_med_conditions")
        }
        mongo.db.kids.replace_one({"_id": ObjectId(kids_id)}, update_child)
        flash("Your Child's Details have been Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    return redirect(url_for("profile", username=session["user"]))


# Delete Child route
@app.route("/delete_child/<kids_id>")
def delete_child(kids_id):
    mongo.db.kids.delete_one({"_id": ObjectId(kids_id)})
    flash("Your Child's Informationaly Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


# Contact Us route
@app.route("/contact_us")
def contact_us():
    if session["user"]:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template("contact_us.html", username=username)
    else:
        return render_template("contact_us.html")


# Thank you route
@app.route("/thank_you", methods=["GET", "POST"])
def thank_you():
    if request.method == "POST":
        return render_template("thank_you.html")


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
