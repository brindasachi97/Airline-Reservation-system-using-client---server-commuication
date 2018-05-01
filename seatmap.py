from seat import Seat
from student import Student

class SeatMap:
    
    def __init__(self,n):
        self.seats = []

        for seatid in range(1,n+1):
            self.seats.append(Seat(seatid))


    def searchForStudent(self,student):
        for seat in self.seats:
            st = seat.getStudent()
            if st == None:
                continue
            if st.getSID() == student.getSID():
                return seat.getSeatID()
        return None

    def isReserved(self,seatid):
        return self.seats[seatid-1].isReserved() #seat id starts from 1 

    def reserveSeat(self, seatid, student):
        self.seats[seatid-1].reserveTo(student)

    def cancelReservation(self, seatid):
        self.seats[seatid-1].cancelReservation()

    def getStudent(self,seatno):
        return self.seats[seatno-1].getStudent()

