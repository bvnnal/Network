from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 

student_id = input("Input student ID: ")
section = input("Input section: ")
first_name = input("Input first name: ")
last_name = input("Input last name: ")

request = f"REQUEST {student_id} {section} {first_name} {last_name}"
print(f"Client: Sending -> {request}")
clientSocket.send(request.encode()) 
response = clientSocket.recv(1024).decode()
print(f"Client: Received -> {response}")

if response.startswith("RESPONSE 200 OK"):
    print("Status Code: 200, Status Phrase: OK")
    response = clientSocket.recv(1024).decode()
    print(f"Client: Received -> {response}")

status_code = response.split()[1]
status_phrase = response.split()[2]
modified_data = response.split(" ", 3)[3]
print(f"Status Code: {status_code}, Status Phrase: {status_phrase}")
print(f"From Server: {modified_data}") 
clientSocket.close()
print("Client: Connection closed")