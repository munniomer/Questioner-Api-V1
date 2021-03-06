users = []  # list for storing our users


class UserModel(object):
    """Class user models."""

    def __init__(self):
        self.db = users

    def add_user(self, username, email, password,role):
        """ Method for saving user to the dictionary """
        payload = {
            "userId": len(self.db) + 1,  
            "username": username,
            "email": email,
            "password": password,
            "role": role

        }
        self.db.append(payload)
        return self.db