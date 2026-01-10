from flask import Flask
from database import config


# instance from Flask
app=Flask(__name__)

# config SQLAlchemy 
app.config('SQLALCHEMY_DATABASE_URI') = config.DATABASE_CONNECTION_URI

#mysql://username:password@server/db

@app.route('/')
def home():
    return "welcome to flask"


# to run locally
if __name__=="__main__":
    app.run()

