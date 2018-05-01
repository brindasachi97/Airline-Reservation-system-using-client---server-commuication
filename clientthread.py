import threading
from threading import Thread
from seatmap import SeatMap
from student import Student
import socket


def recieveLine(socket):
    """
    This function recieve a line from the requested socket till it reach an enter (\n)
    @return a string recieve line
    """
    data = ""
    line = ""
    while(data != '\n'):
        line  += data
        data = socket.recv(1)
        if not data:
            print "Connection is closed from the server\n"
            exit(0)
    return line


BUFFER_SIZE = 1024
NUMBEROFSEATS = 36
seats = SeatMap(NUMBEROFSEATS)

    
# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,conn,addr): 
        Thread.__init__(self) 
        self.conn = conn 
        self.addr = addr
        self.lock = threading.Lock()
        
        print "[+] New server socket thread started for " + addr[0] + ":" + str(addr[1]) 

    def sendMap(self): # send the whole seats to the client
         
        for i in range(1,NUMBEROFSEATS+1):
            seat = ""
            if seats.isReserved(i):
                seat += "R"
            else:
                seat += "A"
            seat += str(i)
            self.conn.send(seat + "\n")

    def readStudent(self): # Get student details from the client
        
        firstname = recieveLine(self.conn)
        lastname = recieveLine(self.conn)
        sid = recieveLine(self.conn)
        password = recieveLine(self.conn)
        return Student(firstname,lastname,sid,password)

    
    def book(self,seatnumber):

        st = self.readStudent()
        
        self.lock.acquire()

        if seats.searchForStudent(st) == None:
            if(not seats.isReserved(seatnumber)):
                seats.reserveSeat(seatnumber,st)
                self.conn.send("Success\n")
            else:
                self.conn.send("The Seat is already Reserved\n")
        else:
            self.conn.send("You've already reserved a seat \n")

        self.lock.release()

    def cancel(self,seatno):

        sid = recieveLine(self.conn)
        password = recieveLine(self.conn)
        st = Student("","",sid,password)

        self.lock.acquire()
        
        seatid = seats.searchForStudent(st)
        
        if seatid == None:
            self.conn.send("You didn't reserve any\n")
        else:
            if seatid == seatno:
                if seats.getStudent(seatno).getPassword() == st.getPassword():
                    seats.cancelReservation(seatid)
                    self.conn.send("Canceled successfully\n")
                else:
                    self.conn.send("Wrong Password\n")
            else:
                self.conn.send("Failed, Not your seat\n")
        self.lock.release()
        
    def run(self): 
        while True : 
            data = recieveLine(self.conn)
            if(data == "map"):
                self.lock.acquire()
                self.sendMap()
                self.lock.release()
            elif(data == "book"):
                seatno = recieveLine(self.conn)
                self.book(int(seatno))
            elif(data == "cancel"):
                seatno = recieveLine(self.conn)
                self.cancel(int(seatno))

