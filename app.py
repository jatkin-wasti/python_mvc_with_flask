# Flask looks for files called app so this is what we have named our file
from flask import Flask, jsonify, redirect, url_for, render_template


# Create an instance of our app
app = Flask(__name__)

# Creating a dictionary in a list to easily transfer it into JSON format
students = [
    {"id": 0, "title": "Mr.", "first_name": "Jamie", "last_name": "Atkin-Wasti", "course": "DevOps"}
]


# using a decorator to create our api/url for the user to access our data in the browser
@app.route("/")  # localhost:5000 is default port for Flask
# This function runs when the URL/API is accessed
def home():
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!</h1>"


@app.route("/welcome/")  # The extra forward slash allows the page to work both with and without it
def greet_user():
    return "Welcome to the DevOps team!"


# Creating our own API to display data on the specific route/URL/end point/API
@app.route("/api/v1/student/data", methods=["GET"])  # This will add this API/URL/end point to the
# http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)  # Use ETL Extract Transform Load. Transforms the students data into Json format


# This redirects the user to the greeting page when trying to access the login page
@app.route("/login/")
def login():
    return render_template("index.html")


# This handles all errors, so if a user tries to access a non existent page it will redirect them to the home page
@app.errorhandler(Exception)
def error_redirect(error):
    return redirect((url_for("home")))


# The <> show that this is an input field
@app.route("/<username>/")
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps, {username}</h1>"


@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/base/")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
