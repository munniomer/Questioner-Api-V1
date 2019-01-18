"""Test question module"""
from app.tests.basetest import BaseTest


class TestUSeQuestion(BaseTest):
    """User tests class"""  
    
    def test_if_no_data(self):
        """Tests if no data is provided in question creation"""
        respon = self.client.post(
            "/api/v1/questions")
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a json data',
                      str(respon.data))

    def test_if_fields_missing(self):
        """Tests if some fields are missing in question creation"""
        respon = self.client.post(
            "/api/v1/questions", json=self.question, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Some fields are missing',
                      str(respon.data))

    def test_question_creation(self):
        """tests if question can be posted"""
        self.client.post("/api/v1/user/register", json=self.new_user18, content_type='application/json')
        self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        respon = self.client.post(
            "/api/v1/questions", json=self.question1, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn('Meetup successfully created',
                      str(respon.data))
      
    def test_empty_fields_question(self):
        """tests if empty fields in question"""
        respon = self.client.post(
            "/api/v1/questions", json=self.question2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('title and body cant be empty or less than 5 words',
                      str(respon.data))

    def test_data_type_question(self):
        """tests if some fields in questions are in numbers"""
        respon = self.client.post(
            "/api/v1/questions", json=self.question3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('title and body should not be provided in numbers',
                      str(respon.data))
    
    def test_data_format_question(self):
        """tests the data format in questions"""
        respon = self.client.post(
            "/api/v1/questions", json=self.question4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn("title and body cant contain only numbers",
                      str(respon.data))


    def test_if_user_exists(self):
        """tests if user exists in question creation"""
        self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        respon = self.client.post(
            "/api/v1/questions", json=self.question5, content_type='application/json')
        self.assertEqual(respon.status_code, 404)
        self.assertIn('That user doesnt exist, plz create a user',
                      str(respon.data))
    
    def test_question_exists(self):
        """tests if question is already posted"""
        self.client.post("/api/v1/user/register", json=self.new_user19, content_type='application/json')
        self.client.post(
            "/api/v1/meetups", json=self.meetup, content_type='application/json')
        self.client.post(
            "/api/v1/questions", json=self.question6, content_type='application/json')
        respon = self.client.post(
            "/api/v1/questions", json=self.question6, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('There is a question title similar that exists',
                      str(respon.data))


    
    