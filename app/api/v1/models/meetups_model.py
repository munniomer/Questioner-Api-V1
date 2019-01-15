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

    def get_all_meetups(self):
        """ Method for getting all Meetup records """
        return self.db
    
    def get_specific_meetup(self, meetup_Id):
        """ Method for getting a specific meetup details """
        meetup = [meetup for meetup in meetups if meetup['meetup_Id'] == meetup_Id]
        return meetup

