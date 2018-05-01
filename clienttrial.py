# Python TCP Client A
import socket 
import getpass
import os
import json
import psycopg2
#from db import insert
#from db import print_all

global price
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

def map(socket):
    print "****The Seat Map****"
    print "****A means available and R means reserved****\n"
    for i in range(6):
        for l in range(6):
            print recieveLine(socket) + "\t",
        print ""

    print "\n"

def book(socket,seatid):
    global price
    socket.send(seatid + "\n")
    print "\n"
    print "**** Enter First Name ****"
    fname=raw_input()
    #print(fname)
    socket.send(fname + "\n")
    print "**** Enter Last Name ****"
    lname=raw_input()
    #print(lname)
    socket.send(lname + "\n")
    print "**** Enter Source ****"
    source=raw_input()
    socket.send(source + "\n")
    print "**** Enter Destination ****"
    destn=raw_input()
    socket.send(destn + "\n")
    print "**** Enter User ID ****"
    userID=raw_input()
    #print(userID)
    socket.send(userID + "\n")
    print "**** Enter Password ****"
    socket.send(getpass.getpass() + "\n")
    print "**** Enter the Class - Economy/Business ****"
    myclass=raw_input()
    socket.send(myclass + "\n")
    if myclass=="Economy":
	price=6000
        print("THE PRICE is",price)
    else:
	price=10000
        print("THE PRICE is",price)
    print "**** Enter Food Preference - Veg/NonVeg ****"
    food=raw_input()
    socket.send(food + "\n")
    print "*** Are you a frequent flyer? - Yes/No ***"
    choice=raw_input()
    socket.send(choice + "\n")
    ######################TICKET DISPLAY##################################
    print "****************************************************************"
    print "NAME:",fname+" "+lname
    print "SOURCE:",source
    print"DESTINATION:",destn
    print"CLASS:",myclass
    print"SEAT ID:",seatid
    print"PRICE:",price
    print "****************************************************************"
    conn = None
    try:
        	conn = psycopg2.connect(host="localhost",database="airlines",user="brinda2",password="passw")
        	cur = conn.cursor()
       		#print('Database Connection Open')
       		cur.execute("""insert into passenger(seatid,fname,lname,source,destn,userID,myclass,price,food,choice) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                            (seatid,fname,lname,source,destn,userID,myclass,price,food,choice))
 		#print("INSERTED INTO THE DATABASE")
        	cur.close()
        	conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
    finally:
        	if conn is not None:
            		conn.close()
            	#print('Database connection closed.')

def cancel(socket,seatid):
    global price
    socket.send(seatid + "\n")
    print "\n"
    print "**** Enter User ID ****"
    socket.send(raw_input() + "\n")
    print "**** Enter Password ****"
    socket.send(getpass.getpass() + "\n")
    #print "Your money" + price + "has been refunded"
    conn = None
    try:
        	conn = psycopg2.connect(host="localhost",database="airlines",user="brinda2",password="passw")
        	cur = conn.cursor()
       		#print('Database Connection Open')
		#cur.execute("""select price from passenger where price=%s""",(price))
		print ("Your money",price,"has been refunded")
		cur.execute("""delete from passenger where seatid = %s""", (seatid,))
 		#print("DELETED FROM THE DATABASE")
		
              
        	cur.close()
        	conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
    finally:
        	if conn is not None:
            		conn.close()
            	#print('Database connection closed.')


host = raw_input("Host: ")
port = input("Port: ")
print("Enter help for details or exit to exit it")
message = ""
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.connect((host, port))

while message != 'exit':

    if(message == "map"):
        server.send(message + "\n")
        map(server)

    elif(message == "help"):
	print " ************************** WELCOME TO INDIGO AIRLINES ************************* "
        print " ************ HELP SCREEN ************"
        print " ****You can use the following commands****"
        print "   @book : to reserve a seat"
        print "   @map: to print the seat map"
        print "   @cancel: to cancel reservation\n"
        
    elif(message == "book"):
        
        server.send(message + "\n")
	seatno = raw_input("Enter Seat No: ")
        book(server,seatno)
        print recieveLine(server)
    
    elif(message == "cancel"):
        server.send(message + "\n")
	seatno = raw_input("Enter Seat No: ")
        cancel(server,seatno)
        print recieveLine(server)
    
    
    message = raw_input("client> ")
    os.system('clear')



server.close()

