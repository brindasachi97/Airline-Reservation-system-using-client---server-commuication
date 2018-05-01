class Seat:

    def __init__(self,seatID):
        self.__seatID = seatID
        self.__is_reserved = False
        self.__student = None


    def reserveTo(self,student):
        self.__student = student
        self.__is_reserved = True

    def cancelReservation(self):
        self.__student = None
        self.__is_reserved = False
        
    def getStudent(self):
        return  self.__student
    
    def isReserved(self):
        return self.__is_reserved
    
    def getSeatID(self):
        return self.__seatID

