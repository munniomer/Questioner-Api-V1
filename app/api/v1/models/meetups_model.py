from datetime import datetime
meetups = [] 


class MeetupModel(object):
    """Class user models."""

    def __init__(self):
        self.db = meetups

    def add_meetup(self,venue, title, happening_on):
        """ Method for saving user to the dictionary """
        payload = {
            "meetup_Id": len(self.db) + 1,  
            "created_on": str(datetime.now()),
            "venue": venue,
            "title": title,
            "happening_on": happening_on

        }
        self.db.append(payload)
        return self.db
