from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgress:kanyemba93@localhost/python-api'
db = SQLAlchemy(app)

class Event(db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__( self):
        return f"Event:{self.description}"

    def __init__(self, descripton, share,likes,views):
        self.description = description

        

@app.route('/')
def hello():
    return 'hey'

if __name__ == "__main__":
    app.run()