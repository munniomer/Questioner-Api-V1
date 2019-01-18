from datetime import datetime
from werkzeug.exceptions import BadRequest
questions = [] 


class QuestionsModel(object):
    """Class question models."""

    def __init__(self):
        self.db = questions


    def add_question(self,user_Id,meetup_Id,title,body):
        """ Method for saving questions to the dictionary """
        payload = {
            "question_Id": len(self.db) + 1,  
            "user_Id":  user_Id, 
            "meetup_Id": meetup_Id,  
            "created_on": str(datetime.now()),
            "title": title,
            "body": body,
            "votes" : 0

        }
        
        self.db.append(payload)
        return self.db


    def upvote_question(self,question_Id):
        """ Method for upvoting a question """
        question = [question for question in questions if question['question_Id'] == question_Id]
        if question:
            for ques in question:
                vote = ques["votes"]
                userid = ques["user_Id"]
                if userid:
                    if vote > 0:
                        raise BadRequest("you can't upvote again")
                ques["votes"] += 1
            return question
    
    def downvote_question(self,question_Id):
        """ Method for downvoting a question """
        question = [question for question in questions if question['question_Id'] == question_Id]
        if question:
            for ques in question:
                vote = ques["votes"]
                userid = ques["user_Id"]
                if userid:
                    if vote < 0:
                        raise BadRequest("you can't downvote again")
                ques["votes"] -= 1
            return question



