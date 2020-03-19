import json
		
import unittest
		
		
from application import create_app
		
		
		
class Base(unittest.TestCase):
		
		
    def setUp(self):
		
		
        """Prepare testing environment."""
		
        self.app = create_app('testing')
		
        self.app = self.app.test_client()
		
        from application import db
		
        self.db = db
		
        self.db.drop_all()
		
        self.db.create_all()
		
		
        self.diary_entry = {
		
		
            "title":"Harry Porter",
		
            "body": "Thebestmovieever"
		
        }
		
        self.diary_entry_without_title = {
		
            "title": "",
		
            "body": "The best movie ever"
		
            
		
        }
		
        self.diary_entry_without_body = {
		
            "title":"Great Wizards",
		
            "body": ""
		
		
        }
		
		
        self.empty_diary_entry = {
		
            "title": "",
		
            "body": ""
		
        }
		
		
        self.diary_entry_not_alphanumeric = {
		
            "title": "12#$",
		
            "body": "The best movie ever"
		
            
		
        }
		
        self.diary_entry_missing_keys = {
		
            "title":"Harry"
		
        }
		
        
		
        """ user 1 """
		
        
		
        self.user_data = {
		
            "firstname":"muh",
		
            "secondname":"bri",
		
            "email": "muh@gmail.com",
		
            "password": "annet123",
		
            "phone": "0719800509",
		
            "confirm_password": "annet123"
		
        }
		
		
        self.app.post('/api/v1/auth/signup',
		
                        data=json.dumps(self.user_data),
		
                        content_type='application/json')
		
		
        """ login to acquire token """
		
        
		
		
        user_login_data = {
		
            "email": "muh@gmail.com",
		
            "password": "annet123"
		
        }
		
		
        response = self.app.post('/api/v1/auth/login',
		
                                 data=json.dumps(user_login_data),
		
                                 content_type='application/json')
		
        response_data = json.loads(response.get_data())
		
        
		
        token = response_data['token']
		
        # add the token to the authorization header
		
        self.headers = {'Authorization': 'Bearer {}'.format(token)}
		
		
        """ user 2 """
		
        self.user_data_2 = {
		
            "firstname":"ken",
		
            "secondname":"lane",
		
            "email": "kane@gmail.com",
		
            "password": "kane123",
		
            "phone": "078XXXXX",
		
            "confirm_password": "kane123"
		
        }
		
		
        
		
		
    
		
    
		
    def tearDown(self):
		
        """Clean memory."""
		
        self.db.drop_all()
		
        self.app = None