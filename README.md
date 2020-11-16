# MVC with Flask in Python
## MVC (Model View Controller)


### Display data on the browser using HTML, CSS, JS, and Bootstrap
- HTML (Hyper Text Markup Language)
- CSS (Cascading Style Sheet)
- JS (Javascript)
- Bootstrap

### Building our API
**Displaying data from python flask to specific API call/URL/end point**

**Why flask?**
- Flask is a web app framework
- Very powerful to interact with DB and user interface/browsers
- Can be used to make an API
- Allows us to integrate with HTML, CSS, and JS
- Allows us to map HTTP requests to python functions - URL, HTTP GET
- Allows us to set the API path as a URL to view in the browser

**Installing Flask**
- Using pip to install Flask in the terminal ```pip install flask```
- Ensure that Flask is installed correctly and import it to the file along with other useful parts of Flask
```python
from flask import Flask, jsonify, redirect, url_for
```
- If this line is underlined in red and it tells you that Flask is not found, run the pip install again and it should
 work
- Create an instance of the app so that we can run it
```python
# Create an instance of our app
app = Flask(__name__)
```
- Assigning a dictionary in a list that we will display on the browser in a JSON format (which is why we imported
 jsonify)
```python
# Creating a dictionary in a list to easily transfer it into JSON format
students = [
    {"id": 0, "title": "Mr.", "first_name": "Jamie", "last_name": "Atkin-Wasti", "course": "DevOps"}
]
```
- Creating our first decorator as the home page
```python
# using a decorator to create our api/url for the user to access our data in the browser
@app.route("/")  # localhost:5000 is default port for Flask
# This function runs when the URL/API is accessed
def home():
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!</h1>"
```
- Creating another decorator that displays a welcome message, using a / at the end of the url to account for a user
 typing the url with or without a trailing /
```python
@app.route("/welcome/")  # The extra forward slash allows the page to work both with and without it
def greet_user():
    return "Welcome to the DevOps team!"
```
- Converting our list into Json format with jsonify() and getting that data when a user goes to the specified URL
```python
# Creating our own API to display data on the specific route/URL/end point/API
@app.route("/api/v1/student/data", methods=["GET"])  # This will add this API/URL/end point to the
# http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)  # Use ETL Extract Transform Load. Transforms the students data into Json format
```
- Here we'll take a users input and personalise the message displayed to them!
```python
# The <> show that this is an input field
@app.route("/<username>/")
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps, {username}</h1>"
```
- Redirecting users is an important tool to use. We'll create a specific and a non specific way to handle this
- The first method redirects the user to the greetings page if they try to access the still in construction login page
- The second catches all other errors e.g. when they try to access a page that doesn't exist, and redirects them to
 the home page
```python
# This redirects the user to the greeting page when trying to access the login page
@app.route("/login/")
def login():
    return redirect(url_for("greet_user"))


# This handles all errors, so if a user tries to access a non existent page it will redirect them to the home page
@app.errorhandler(Exception)
def error_redirect(error):
    return redirect((url_for("home")))
```
- This turns the debugging option on and runs the app only if ran from this file
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- How to run the Flask app
```commandline
flask run
```
- We then click on the url provided in our terminal which should look like this ```http://127.0.0.1:5000/ ``` to
 access our site
- We can also go to the other specified routes to access the student data or the login page by appending the path to
 the existing url, i.e. ```http://127.0.0.1:5000/login```
**Integrating HTML**
- Naming conventions are essential
- We need to create a template folder in our dir
- Flask looks for templates folder and anything inside the folder
- We will create index.html inside our templates folder

**Bootstrap to design our page with HTML, CSS, and JS**
- CSS goes in the <head></head> section
- 

## 
