# from flask import Flask,request,url_for,jsonify,make_response
# from flask import abort
# from werkzeug.exceptions import HTTPException
# from routes.user import user_bp


# app = Flask(__name__)

# app.register_blueprint(user_bp)

# class UserAlreadyExists(Exception):
#     def __init__(self,message):
#         self.message = message

# @app.errorhandler(UserAlreadyExists)
# def handle_custom(error):
#     return {
#         "success":False,
#         "message":error.message
#     },409

# @app.errorhandler(Exception)
# def handle_exception(error):
#     return {
#         "success":False,
#         "message":"Internal server error"
#     },500
# @app.errorhandler(HTTPException)
# def handle_http_error(error):
#     return {
#         "success":False,
#         "message":error.description
#     },error.code



# @app.errorhandler(404)
# def handle_404(error):
#     return {
#        "success":False,
#        "message":error.description 
#     },404



# @app.route("/")
# def home():
#     return url_for("get_user",id = 10)
# @app.route("/about")
# def about():
#     return "This is about page"
# @app.route("/health")
# def health():
#     return "Helth is weilth"



# @app.route("/products")
# def get_products():
#     limit = request.args.get("limit",default=10,type = int)
#     mn_price = request.args.get("min_price",default=20,type = int)
#     mx_price = request.args.get("max_price",default=100,type = int)

#     return {
#       "limit": limit,
#        "max-price":mx_price,
#       "min-price" :mn_price
#     }



# @app.route("/admin",methods=["POST"])
# def create_admin():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     file = request.files.get("file")
#     file.save("uploads/"+file.filename)
#     return {
#         "email":email,
#         "name":name,
#         "file":file.filename,
#         "method":request.method,
#         "url":request.url,
#         "path":request.path,
#         "base_url":request.base_url
#     }
