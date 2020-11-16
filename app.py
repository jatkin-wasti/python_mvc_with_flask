# Flask looks for files called app so this is what we have named our file
from flask import Flask


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
    return "This is a dream team of DevOps consultants celebrating a WOW moment!"


if __name__ == "__main__":
    app.run(debug=True)
