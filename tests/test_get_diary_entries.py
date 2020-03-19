import json
import unittest

from entryBase import Base

class GetEntries(Base):

    def setUp(self):

        """ prepare testing environment """
        super().setUp()
        self.app.post('/api/v1/entries',
                      data=json.dumps(self.diary_entry),
                      content_type='application/json',
                      headers=self.headers)

    def tearDown(self):
        "Clear memory"
        super().tearDown()

    def test_get_all_entries(self):
        response = self.app.get('/api/v1/entries/',
                                content_type='application/json',
                                headers=self.headers)

        self.assertEqual(response.status_code, 404)


    def test_get_single_entry(self):
        response = self.app.get('/api/v1/entries/{}'.format(1),
                                content_type='application/json',
                                headers=self.headers)
        self.assertEqual(response.status_code, 200)   

    def test_get_entry_that_doesnot_exist(self):
        response = self.app.get('/api/v1/entries/23',
                                content_type='application/json',
                                headers=self.headers)
        self.assertEqual(response.status_code, 404)


if __name__=='__main__':
    unittest.main()























