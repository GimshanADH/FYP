import serial

# Define the serial port (adjust this based on your setup)
serial_port = '/dev/serial0'  # For Raspberry Pi 3B

# Open the serial port
try:
    ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

# Main loop to send and receive data
while True:
    data_to_send = input("Enter data to send: ")
    ser.write(data_to_send.encode('utf-8'))

    received_data = ser.readline().decode('utf-8').strip()
    print("Received data:", received_data)

# Close the serial port
ser.close()

