# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 3

Created on Mon Oct 28 15:07:51 2024

@author: Bailey Byl 20135558
"""

import socket


def main():
    
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Assign the IP address and port
    server_socket.bind(('localhost', 1234))
    
    # Open the socket and listen for connections
    server_socket.listen(1)
    print("Server has started and is listening on port 1234...")
    
    connection, client_address = server_socket.accept()
    print("Client connected")
    
    # Message loop
    while True:
        # Receive message from the client
        message = connection.recv(1024).decode('utf-8')
        
        # Exits the message loop if the client types 'exit'
        if message.lower() == 'exit':
            print("Client disconnected")
            break
        
        # Prints the clients message
        print(f"Client: {message}")
        
        # Send a message back to the client
        response = input("Server (type 'exit' to end): ")
        connection.sendall(response.encode('utf-8'))
        
        # Exits the message loop if the server types 'exit'
        if response.lower() == 'exit':
            print("Server ended the connection.")
            break
    
    # Closes the connection
    connection.close()
    server_socket.close()
    print("Server closed the connection.")



if __name__ == "__main__":
    main()
