#from validate_email import validate_email
from werkzeug.security import generate_password_hash

from application import db


class User():

    def __init__(self, user_data):
        self.firstname = user_data['firstname']
        self.secondname = user_data['secondname']
        self.email = user_data['email']
        self.password = generate_password_hash(
            user_data['password'], method='sha256')
        self.phone = user_data['phone']

    def save(self):
        # insert new record
        query = "INSERT INTO users (firstname,secondname,email,password,phone)\
        VALUES ('{}' , '{}', '{}', '{}', '{}')"\
                . format(self.firstname, self.secondname, self.email, self.password, self.phone)

        return db.execute(query)
