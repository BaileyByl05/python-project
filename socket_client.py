# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 3

Created on Mon Oct 28 15:08:17 2024

@author: Bailey
"""

import socket


def main():
    
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        # Enter server ip and port
        server_address = str(input('Enter the server IP address: '))
        server_port = int(input('Enter the server port: '))
        try:
            # Connect to the server
            client_socket.connect((server_address, server_port))
            break
        except:
            print('Connection failed')
        
    print(f"Connected to the server at {server_address}:{server_port}")
    
    # Message loop
    while True:
        # Send a message to the server
        message = input("Client (type 'exit' to end): ")
        client_socket.sendall(message.encode('utf-8'))
        
        # Exits the message loop if the client types 'exit'
        if message.lower() == 'exit':
            print("Client ended the connection.")
            break
        
        # Receive message from the server
        response = client_socket.recv(1024).decode('utf-8')
        
        # Exits the message loop if the server types 'exit'
        if response.lower() == 'exit':
            print("Server ended the connection.")
            break
        
        print(f"Server: {response}")
    
    # Closes the connection
    client_socket.close()
    print("Client closed the connection.")




if __name__ == "__main__":
    main()