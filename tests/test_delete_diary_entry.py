import json
import unittest

from entryBase import Base

class DeleteEntries(Base):

    def setUp(self):
        super().setUp()
        self.app.post('/api/v1/entries',
                                 data=json.dumps(self.diary_entry),
                                 content_type='application/json',
                                 headers=self.headers)
        
    def tearDown(self):
        super().tearDown()

    def test_user_can_delete_ride_offer(self):
        
        response = self.app.delete('/api/v1/entries/1',
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'], 'Diary entry deleted successfully')

    def test_user_cannot_delete_non_existing_ride_offer(self):
        
        response = self.app.delete('/api/v1/entries/-1',
                            content_type='application/json',
                            headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],'Diary entry not found')

if __name__ == '__main__':
    unittest.main()
