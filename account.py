class Account:
    def __init__(self, user_name, tier=0):
        # Setting to string in-case bad input is introduced
        self.__user_name = str(user_name)
        # Physician = 3, Medical Personnel = 2, Office Staff 1, and Volunteers = 0
        # Setting tier to lowest default if unexpected input introduced
        if tier not in [0, 1, 2, 3]:
            tier = 0
        self.__tier = tier

    def get_user(self):
        return self.__user_name

    def get_tier(self):
        return self.__tier