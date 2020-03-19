import json 
import unittest 
from entryBase import Base

class Entries(Base):

    def setUp(self):
        """ prepare testing environment """

        """ get setUp method from Base """
        super().setUp()

    def tearDown(self):
        """ Clear memory."""
        super().tearDown()

    def test_create_diary_entry(self):
        """ self.headers contains our auth token """
       
        response = self.app.post('/api/v1/entries',
                                data=json.dumps(self.diary_entry),
                                content_type='application/json',
                                headers=self.headers)

        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['message'], \
                                    'diary entry added successfully.')

    def test_create_empty_entry(self):

        response = self.app.post('/api/v1/entries',
                                data=json.dumps(self.empty_diary_entry),
                                content_type='application/json',
                                headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Missing title or body fields.')

    def test_entry_without_title(self):

        response = self.app.post('/api/v1/entries',
                                data=json.dumps(self.diary_entry_without_title),
                                content_type='application/json',
                                headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Missing title or body fields.')

    def test_entry_without_body(self):

        response = self.app.post('/api/v1/entries',
                                data=json.dumps(self.diary_entry_without_body),
                                content_type='application/json',
                                headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Missing title or body fields.')
    '''
    def test_entry_is_alphanumeric(self):
        response = self.app.post('/api/v1/entries',
                                data=json.dumps(self.diary_entry_not_alphanumeric),
                                content_type='application/json',
                                headers=self.headers)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'title can only be letters or numbers.')
    '''
    
    def test_entry_is_missing_keys(self):
        response = self.app.post('/api/v1/entries',
                                data=json.dumps(self.diary_entry_missing_keys),
                                content_type='application/json',
                                headers=self.headers)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'missing title or body keys')

    






if __name__ == '__main__':
    unittest.main()