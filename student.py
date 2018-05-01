class Student:
    
    def __init__(self,firstName,lastname,sid,password):
        self.__firstName = firstName
        self.__lastName = lastname
        self.__sid = sid
        self.__password = password

        
    def getPassword(self):
        return self.__password

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName
    
    def getSID(self):
        return self.__sid

    

