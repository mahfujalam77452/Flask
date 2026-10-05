from flask import Blueprint,request,make_response

user_bp = Blueprint("users",__name__,url_prefix = "/users")


@user_bp.route("",methods = ["POST"])
def create_user():
    
    # value = 5/0
    # raise UserAlreadyExists("User alrady exists")

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



@user_bp.route("/<int:id>")
def get_user(id):
     
    if id == 999:
        abort(400)

    return f"Get user : {id}"



@user_bp.route("/<id>/posts/<int:post_id>")
def get_post(id,post_id):
    return f"User id : {id} , Post id : {post_id} type {type(post_id)}"

