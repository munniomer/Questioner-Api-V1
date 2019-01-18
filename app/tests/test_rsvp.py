"""Test rsvp module"""
from app.tests.basetest import BaseTest


class RsvpMeetup(BaseTest):
    """Rsvps tests class"""

    def test_if_no_data(self):
        """Tests if no data is provided in rsvps creation"""
        respon = self.client.post(
            "/api/v1/meetups/1/rsvps")
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a json data',
                      str(respon.data))

    def test_if_fields_missing(self):
        """Tests if some fields are missing in rsvps creation"""
        respon = self.client.post(
            "/api/v1/meetups/1/rsvps", json=self.rsvp, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Some fields are missing',
                      str(respon.data))
    
    def test_rsvps_creation(self):
        """tests if rsvps can be posted"""
        self.client.post("/api/v1/user/register", json=self.new_user19, content_type='application/json')
        self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        respon = self.client.post(
            "/api/v1/meetups/1/rsvps", json=self.rsvp1, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn('Rsvps successfully created',
                      str(respon.data))
    
    def test_if_user_exists(self):
        """tests if user exists in rsvps creation"""
        respon = self.client.post(
            "/api/v1/meetups/3/rsvps", json=self.rsvp2, content_type='application/json')
        self.assertEqual(respon.status_code, 404)
        self.assertIn('That user doesnt exist, plz create a user',
                      str(respon.data))
    
    def test_if_meetup_exists(self):
        """tests if meetup exists in rsvps creation"""
        self.client.post("/api/v1/user/register", json=self.new_user19, content_type='application/json')
        respon = self.client.post(
            "/api/v1/meetups/10/rsvps", json=self.rsvp3, content_type='application/json')
        self.assertEqual(respon.status_code, 404)
        self.assertIn('That meetup doesnt exist',
                      str(respon.data))
    
    def test_data_format_validate_rsvps(self):
        """tests the data format in rsvps"""
        respon = self.client.post(
            "/api/v1/meetups/1/rsvps", json=self.rsvp4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn("response should not be provided in numbers",
                      str(respon.data))

    def test_empty_space_rsvps(self):
        """tests empty space in rsvps"""
        respon = self.client.post(
            "/api/v1/meetups/1/rsvps", json=self.rsvp5, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn("response should not be empty",
                      str(respon.data))