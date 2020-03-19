from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required, get_raw_jwt, create_access_token, get_jwt_identity
from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from datetime import datetime
import re

from . import blacklist

from application.models.user_model import User
from application import db


api = Namespace('Users', Description='User operations')


def validate_email(email):
    match = re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email)
    if match is not None:
        return True
    return False


class UserSignUp(Resource):
    """ Enable user to sign up """

    def post(self):
        try:

            user_data = request.get_json()
            firstname = user_data['firstname']
            secondname = user_data['secondname']
            confirmPassword = user_data['confirm_password']
            phone = user_data['phone']
            email = user_data['email']
            password = user_data["password"]

            """ check for empty fields """
            if email == "" or phone.strip() == ""\
                    or confirmPassword.strip() == "" or password.strip() == ""\
                    or firstname.strip() == "" or secondname.strip() == "":
                return {"message": "Please ensure all fields are non-empty."}, 400

            if len(firstname) < 3 or len(secondname) < 3:
                return {'message': 'names cannot be less than 3 characters'}, 400 

            """ check if password id less than 6 characters """
            if len(password) < 6:
                return {'message': 'password should be 6 characters or more.'}, 400

            """ match email against regular expression """
            if not validate_email(email):
                return {"message": "Email is invalid"}, 400

            """ if passwords dont match """
            if not password == confirmPassword:
                return {'message': 'Passwords do not match'}, 400

            query = "select email from users where email='%s'\
             or phone='%s'" % (email, phone)
            result = db.execute(query)
            user = result.fetchone()
            """ if no user, save user data """
            if user is None:
                userObject = User(user_data)
                userObject.save()
                return {'message': 'Account created.'}, 201
            return {'message': 'User exists.'}, 403
        except(KeyError):
            return {'message': 'please ensure you have entered all required fields'}


class UserLogin(Resource):
    """ Enable user to login / generate jwt token """

    def post(self):

        try:

            user_data = request.get_json()
            email = user_data['email']
            password = user_data['password']

            """ check for empty fields """
            if email.strip() == "" or password.strip() == "":
                return {"message": "Password or email cannot be empty."}, 401

            query = "select password from users where email='{}'"\
                    . format(email)
            result = db.execute(query)
            user = result.fetchone()

            if user is None:
                return {'message': 'User not found.'}, 404

            """ check if password given is equal to hashed password to db """

            if check_password_hash(user[0], password):
                token = create_access_token(identity=email)
                return {'message': 'You have succesfully logged in.', 'token': token}, 201
            else:
                return {'message': 'Invalid password.'}, 401
        except(KeyError):

            return {'message': 'Please ensure you have provided both email and password'}, 401

class Profile(Resource):
    @jwt_required 
    def get(self):
        """ get user details """
        email = get_jwt_identity()
        query = "select firstname,secondname,phone \
            from users where email='{}'".format(email)
        result = db.execute(query)
        users = result.fetchone()
        return {'firstname': users[0],'secondname':users[1],\
        'phone number': users[2], 'email': email},200


class Logout(Resource):
    """ log out user """
    @jwt_required
    def post(self):
        """ Add user's token to blacklist """
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return ({'message': 'You have successfully logged out'}), 200


api.add_resource(UserSignUp, '/auth/signup')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(Profile, '/auth/profile')
api.add_resource(Logout, '/auth/logout')
