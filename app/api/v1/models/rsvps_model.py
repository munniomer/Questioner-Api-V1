rsvps = []


class RsvpsModel(object):
    """Class question models."""

    def __init__(self):
        self.db = rsvps

    def add_rsvps(self, user_Id, meetup_Id, response):
        """ Method for saving questions to the dictionary """
        payload = {
            "rsvps_Id": len(rsvps) + 1,
            "user_Id":  user_Id,
            "meetup_Id": meetup_Id,
            "response": response
        }
        # print("before",payload)
        self.db.append(payload)
        # print("after",rsvps)

        return self.db

 
