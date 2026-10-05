from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello I am Flask"
@app.route("/about")
def about():
    return "This is about page"
@app.route("/health")
def health():
    return "Helth is weilth"

