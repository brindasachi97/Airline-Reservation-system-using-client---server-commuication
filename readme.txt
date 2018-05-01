README file for CN ASSIGNMENT 
TOPIC : Client Server communication for AIRLINE RESERVATION
 
We are implementing airline reservation using client server communication. 

We have the following files:

On Server Side:

1. server.py
	We connect to the TCP_IP = "127.0.0.1" and an arbitrary port number using TCP_PORT = input("Port: ")
We make a socket connection between the client and server. The server here listens to 4 clients as we have specified the parameter as 4 in tcpServer.listen(4).
Also a new thread is created for each client.

server.py imports the file clientthread.py

2. clientthread.py
	Checks whether the connection between the client and the server is appropriate. If not, closes the connection.
Initializes buffer size to 1024 and the number of seats available to 36.  
Now we get passenger details from the client (i.e., the passenger details are sent from the client to server)
We have 3 functions : book, cancel and map.
In book, we see if the seat is already reserved. If not, we reserve a new seat.
In cancel, we do password validation i.e., if the password of the passenger matches, we cancel the seat and refund the amount (else, wrong password). Also, we don't cancel the seat if not booked.
In map, if a seat is reserved, the seat number is prefixed with "R", otherwise prefixed with "A" implying available. These details are sent from server side to the client side.

clientthread.py imports seatmap.py and student.py


3. seat.py
	Whenever a seat is booked/cancelled, we initialize values of few variables to True or False depending on the respective case.

4. seatmap.py
	If a passenger doesn't exist (not yet booked), we skip that particular iteration. Else, we return the seat id of the particular passenger.
seatmap.py imports seat.py and student.py


5. student.py
	The details entered by the client are sent to the server side.

On Client Side:

1. clienttrial.py
	The seat details (Available/Reserved) are received from server side. The client enters the required details, sends to the server, and also gets stored in the database. We have multiple clients, all running on the same port number. (It is First Come First Serve)
We ask the client for 3 options:
Book, Map and cancel. Depending on the option entered, the client either books/cancels/views the available number of seats.



We have the following features implemented in airline reservation system:

1.BOOKING A TICKET
2.DETAILS/OPTIONS ENTERED BY THE CLIENT
3.TICKET RESERVED ON THE BASIS OF FIRST COME FIRST SERVE
4.INSERTION OF CLIENT DETAILS INTO THE DATABASE
5.SEAT MAP DISPLAY
6.MULTIPLE CLIENTS ON SAME PORT ADDRESS AND PORT NUMBER
7.CANCELLATION OF A TICKET
8.PASSWORD VALIDATION
9.REFUND
10.DELETION FROM THE DATABASE
