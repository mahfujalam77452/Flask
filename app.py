from flask import Flask,request,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return url_for("get_user",id = 10)
@app.route("/about")
def about():
    return "This is about page"
@app.route("/health")
def health():
    return "Helth is weilth"

@app.route("/users",methods = ["POST"])
def create_user():
    return "User created"

@app.route("/users/<id>")
def get_user(id):
    return f"Get user : {id}"

@app.route("/users/<id>/posts/<int:post_id>")
def get_post(id,post_id):
    return f"User id : {id} , Post id : {post_id} type {type(post_id)}"


@app.route("/products")
def get_products():
    limit = request.args.get("limit",default=10,type = int)
    mn_price = request.args.get("min_price",default=20,type = int)
    mx_price = request.args.get("max_price",default=100,type = int)

    return {
      "limit": limit,
       "max-price":mx_price,
      "min-price" :mn_price
    }

