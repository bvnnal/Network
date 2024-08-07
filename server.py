from socket import *

def student_data(student_id, section, first_name, last_name):
    first_name = first_name.upper()
    last_name = last_name[0].upper() + "."
    return f"{student_id} {section} {first_name} {last_name}"

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
print("Server: Ready!")
serverSocket.listen(1)
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Server: Connection established with {addr}")
    request = connectionSocket.recv(1024).decode()
    print(f"Server: Received -> {request}")
    if request.startswith("REQUEST"):
        parts = request.split(" ", 4)
        if len(parts) == 5:
            student_id = parts[1]
            section = parts[2]
            first_name = parts[3]
            last_name = parts[4]
            response = "RESPONSE 200 OK"
            print(f"Server: Sending -> {response}")
            connectionSocket.send(response.encode())
            processed_data = student_data(student_id, section, first_name, last_name)
            response = f"RESPONSE 250 OK {processed_data}"
        else:
            response = "RESPONSE 400 BAD REQUEST"
    else:
        response = "RESPONSE 400 BAD REQUEST"
    print(f"Server: Sending -> {response}")
    connectionSocket.send(response.encode())
    connectionSocket.close()
    print("Server: Connection closed")