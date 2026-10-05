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
    data = request.get_json()

    if not data:
        return {
            "errors":"request data is required"
        },400
    return {
        "name":data.get("name"),
        "email":data.get("email"),
        "age":data["age"]
    },201

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

@app.route("/admin",methods=["POST"])
def create_admin():
    name = request.form.get("name")
    email = request.form.get("email")
    file = request.files.get("file")
    file.save("uploads/"+file.filename)
    return {
        "email":email,
        "name":name,
        "file":file.filename,
        "method":request.method,
        "url":request.url,
        "path":request.path,
        "base_url":request.base_url
    }
