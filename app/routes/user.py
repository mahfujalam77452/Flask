from operator import and_, or_

from flask import Blueprint,request,make_response
from sqlalchemy import func
from app.models.user import User
from app.extensions import db 

user_bp = Blueprint("users",__name__,url_prefix = "/users")


@user_bp.route("",methods = ["POST"])
def create_user():
    users = [
    User(id=1, name="Rahim Ahmed", email="rahim.ahmed@example.com"),
    User(id=2, name="Karim Hasan", email="karim.hasan@example.com"),
    User(id=3, name="Sadia Rahman", email="sadia.rahman@example.com"),
    User(id=4, name="Nusrat Jahan", email="nusrat.jahan@example.com"),
    User(id=5, name="Tanvir Hossain", email="tanvir.hossain@example.com"),
    User(id=6, name="Fahim Ahmed", email="fahim.ahmed@example.com"),
    User(id=7, name="Mehedi Hasan", email="mehedi.hasan@example.com"),
    User(id=8, name="Jannatul Ferdous", email="jannatul.ferdous@example.com"),
    User(id=9, name="Sakib Khan", email="sakib.khan@example.com"),
    User(id=10, name="Sumaiya Akter", email="sumaiya.akter@example.com"),
    User(id=11, name="Arif Hossain", email="arif.hossain@example.com"),
    User(id=120, name="Mahfuj Rahman", email="mahfuj.rahman@example.com"),
    User(id=13, name="Rafiul Islam", email="rafiul.islam@example.com"),
    User(id=14, name="Tania Sultana", email="tania.sultana@example.com"),
    User(id=15, name="Shakil Ahmed", email="shakil.ahmed@example.com"),
    User(id=16, name="Mim Akter", email="mim.akter@example.com"),
    User(id=17, name="Imran Kabir", email="imran.kabir@example.com"),
    User(id=18, name="Farzana Yasmin", email="farzana.yasmin@example.com"),
    User(id=19, name="Nayeem Hasan", email="nayeem.hasan@example.com"),
    User(id=20, name="Anika Rahman", email="anika.rahman@example.com"),
    ]

    db.session.add_all(users)
    db.session.commit()


    stmp = db.select(User)

    result = db.session.execute(stmp)

    data = result.scalars().all()
    
    # value = 5/0
    # raise UserAlreadyExists("User alrady exists")

    # data = request.get_json()

    if not data:
        return {
            "errors":"request data is required"
        },400

    response = make_response(
        {
           "data":[{"id":user.id,"name":user.name,"email":user.email} for user in data]  
        },201
    )
    response.headers["x-app-version"] = "1.0"
    response.set_cookie("token","abc123",httponly=True,secure=False,samesite="Lax")
    return response



@user_bp.route("")
def get_user():

    # stmp = db.select(User).where(User.id == 2)

    # user = db.session.execute(stmp).scalar_one_or_none()
     
    stmp = db.select(User).where(
        or_(
            User.id > 5,
            User.name == "Rafiul Islam"

        )
    ).order_by(User.email.desc()).offset(2).limit(2)

    users = db.session.execute(stmp).scalars().all()
    count = db.session.execute(
       db.select(func.count()).select_from(User).where(User.id % 2 == 0)
    ).scalar()
    response = make_response(
            {
               "count":count,
               "data":[{"id":user.id,"name":user.name,"email":user.email} for user in users ]  
            },200
        )

    return response



@user_bp.route("",methods=["PUT"])
def get_post():
    user = db.session.execute(
        db.select(User).where(User.id == 1)
    ).scalar_one_or_none()

    if user :
        db.session.delete(user)
        db.session.commit()
    response = make_response(
        {
         "user":{"id":user.id,"name":user.name,"email":user.email}
        },203
    )

    return response

