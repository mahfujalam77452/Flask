from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    print("DATABASE:", db.engine.url)
    print("TABLES BEFORE:", db.metadata.tables.keys())

    db.create_all()

    print("TABLES AFTER:", db.metadata.tables.keys())

if __name__ == "__main__":
    app.run(debug=True)