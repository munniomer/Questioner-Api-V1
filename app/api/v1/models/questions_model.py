from datetime import datetime
questions = [] 


class QuestionsModel(object):
    """Class question models."""

    def __init__(self):
        self.db = questions


    def add_question(self,user_Id,meetup_Id,title,body):
        """ Method for saving questions to the dictionary """
        payload = {
            "question_Id": len(self.db) + 1,  
            "userId":  user_Id, 
            "meetup_Id": meetup_Id,  
            "created_on": str(datetime.now()),
            "title": title,
            "body": body,
            "votes" : 0

        }
        
        self.db.append(payload)
        return self.db


