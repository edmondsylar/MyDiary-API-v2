import json
import unittest 

from entryBase import Base

class EditEntries(Base):

    def setUp(self):
        super().setUp()
        self.app.post('/api/v1/entries',
                      data=json.dumps(self.diary_entry),
                      content_type='application/json',
                      headers=self.headers)

        self.diary_entry = {
            "title": "Lord of the rings",
            "body": "trilogy"
        }
        

    def tearDown(self):
        super().tearDown()

    def test_can_edit_diary_entry(self):
        response = self.app.put('/api/v1/entries/1',
                                data=json.dumps(self.diary_entry),
                                content_type='application/json',
                                headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'diary entry updated succesfully')


    def test_update_non_existing_diary_entry(self):
        response = self.app.put('/api/v1/entries/-1',
                            data=json.dumps(self.diary_entry),
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_update_diary_entry_without_title(self):
        response = self.app.put('/api/v1/entries/1',
                            data=json.dumps(self.diary_entry_without_title),
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Missing title or body fields.')

    def test_update_diary_entry_without_body(self):
        response = self.app.put('/api/v1/entries/1',
                            data=json.dumps(self.diary_entry_without_body),
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Missing title or body fields.')

    def test_update_empty_diary_entry(self):
        response = self.app.put('/api/v1/entries/1',
                            data=json.dumps(self.empty_diary_entry),
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Missing title or body fields.')
    

    def test_update_entry_missing_key(self):
        response = self.app.put('/api/v1/entries/1',
                            data=json.dumps(self.diary_entry_missing_keys),
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 403)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'missing title or body keys')
    

if __name__=='__main__':
    unittest.main()
























