from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
"""Aca se deben setear los datos de la base de datos luego de ://<userDB>:<passDB>@url """
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/MyBandAppDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.app_context().push()

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(250), unique=True)
    userName = db.Column(db.String(50), unique=True)
    userPassword = db.Column(db.String(250))
    userSubcriptionId = db.Column(db.Integer)
    userSubExpiration = db.Column(db.String(8))
    userLibraryId = db.Column(db.Integer)

    def __init__(self, mail, userName, userPassword, userSubcriptionId, userSubExpiration, userLibraryId):
        self.mail = mail
        self.userName = userName
        self.userPassword = userPassword
        self.userSubcriptionId = userSubcriptionId
        self.userSubExpiration = userSubExpiration
        self.userLibraryId = userLibraryId


db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','mail','userName','userPassword','userSubcriptionId','userSubExpiration','userLibraryId')

user_schema = UserSchema()
allUser_schema = UserSchema(many=True)

@app.route('/users',methods=['POST'])
def create_user():
    print(request.json)
    return 'recibido'

if __name__ == "__main__":
    app.run(debug=True)
