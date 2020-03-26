from HakAkses import HakAkses

class Login():
    
    def __init__(self, username, password, hakAkses):
        self.__username = username
        self.__password = password

        if hakAkses in HakAkses:
            self.__hakAkses = hakAkses.name
        else :
            print("something wrong")
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def hakAkses(self):
        return self.__hakAkses

    @hakAkses.setter
    def hakAkses(self, hakAkses):
        self.__hakAkses = hakAkses