from flask import Flask,request,url_for,jsonify,make_response
from flask import abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

class UserAlreadyExists(Exception):
    def __init__(self,message):
        self.message = message

@app.errorhandler(UserAlreadyExists)
def handle_custom(error):
    return {
        "success":False,
        "message":error.message
    },409

@app.errorhandler(Exception)
def handle_exception(error):
    return {
        "success":False,
        "message":"Internal server error"
    },500
@app.errorhandler(HTTPException)
def handle_http_error(error):
    return {
        "success":False,
        "message":error.description
    },error.code



@app.errorhandler(404)
def handle_404(error):
    return {
       "success":False,
       "message":error.description 
    },404



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
    value = 5/0
    raise UserAlreadyExists("User alrady exists")

    data = request.get_json()

    if not data:
        return {
            "errors":"request data is required"
        },400

    response = make_response(
        {
           "name":data.get("name"),
                  "email":data.get("email"),
                  "age":data["age"]  
        },201
    )
    response.headers["x-app-version"] = "1.0"
    response.set_cookie("token","abc123",httponly=True,secure=False,samesite="Lax")
    return response



@app.route("/users/<int:id>")
def get_user(id):
     
    if id == 999:
        abort(400)

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
