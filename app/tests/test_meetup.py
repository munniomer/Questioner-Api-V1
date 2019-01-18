"""Test user module"""
from app.tests.basetest import BaseTest


class TestMeetup(BaseTest):
    """Meetup tests class"""

    def test_if_no_data(self):
        """Tests if no data is provided in meetup creation"""
        respon = self.client.post(
            "/api/v1/meetups")
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a json data',
                      str(respon.data))

    def test_if_fields_missing(self):
        """Tests if some fields are missing in meetup creation"""
        respon = self.client.post(
            "/api/v1/meetups", json=self.meetup1, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Some fields are missing',
                      str(respon.data))

    def test_meetup_creation(self):
        """tests if new user can register"""
        respon = self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn('Meetup successfully created',
                      str(respon.data))

    def test_to_get_all_meetups(self):
        """Test when meetups are there to fetch"""
        respon = self.client.get('/api/v1/meetups')
        self.assertEqual(respon.status_code, 200)
        self.assertIn('All meetups orders',
                      str(respon.data))

    def test_get_specific_meetup(self):
        """Test to fetch a specific meetup details"""
        self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        respon = self.client.get('/api/v1/meetups/1')
        self.assertEqual(respon.status_code, 200)

    def test_empty_fields(self):
        """tests if there are empty fields in meetups"""
        respon = self.client.post(
            "/api/v1/meetups", json=self.meetup2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('please fill all the fields',
                      str(respon.data))

    def test_incorrect_data(self):
        """tests if meetup data are in correct form"""
        respon = self.client.post(
            "/api/v1/meetups", json=self.meetup3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Title and Venue should not be provided in numbers',
                      str(respon.data))

    def test_to_get_specific_meetup(self):
        """Test when a specific parcel does not exist"""
        self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        respon = self.client.get('/api/v1/meetups/11')
        self.assertEqual(respon.status_code, 404)
        self.assertIn("meetups details not found",
                      str(respon.data))

    def test_get_all_meetups(self):
        """Test when meetups are not found"""
        self.client.post(
            "/api/v1/meetups", json=self.meetup3, content_type='application/json')
        respon = self.client.get('/api/v1/meetups')
        self.assertEqual(respon.status_code, 404)
        self.assertIn('There are no meetups created',
                      str(respon.data))

    def test_bad_request_handler(self):
        """Tests the handler for bad request"""
        respon = self.client.get('/api/v1/buuuu')
        self.assertEqual(respon.status_code, 404)
        self.assertIn('Not Found!',
                      str(respon.data))

 



