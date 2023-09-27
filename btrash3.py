import bluetooth

# Define the Bluetooth server socket
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

# Get the Bluetooth address of the Raspberry Pi
print("Waiting for connection on RFCOMM channel", server_socket.getsockname()[1])

# Accept a Bluetooth connection
client_socket, client_info = server_socket.accept()
print("Accepted connection from", client_info)

try:
    while True:
        # Receive data from the Bluetooth client
        data = client_socket.recv(1024)
        
        if not data:
            break
        
        # Decode the received data
        received_data = data.decode("utf-8")
        
        # Process and display the received data
        print("Received:", received_data)
        
except KeyboardInterrupt:
    pass

print("Closing connection")
client_socket.close()
server_socket.close()
