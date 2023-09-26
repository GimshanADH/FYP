import serial

uart_channel = serial.Serial("/dev/ttyAMMO",baudrate=9600, timeout=2)

BT_DEVICE = '/dev/ttyS0'
BT_BAUDRATE = 9600


BTSerial = serial.Serial(BT_DEVICE, BT_BAUDRATE)

try:
	while True:
		data= uart_channel.read()
		
    		try:
        		num = int(data)
        		print(f"Received an integer: {num}")
        		# Perform actions for integer data
        		
        		count_app = data
        		
        		print("Recieved count: ",data)
        		# print count_app number of objects 
        		
        		
        		
    		except ValueError:
        		print(f"Received a word: {data}")
        		# Perform actions for string data
        		
      			print("Recieved word: " ,data)
      			word_app = data
      			word_child = 'charindu'
      			
      			if wordChild == WordReseved :
    				condition = 'Correct'
    				
    				print(" child " ,condition)
    				# need to display victory
    				
    				
			else:
    				condition = 'Wrong'
    				
    				print(" child " ,condition)
    				# need to display try again and word_app
    				
						
except KeyboardInterrupt:
    print("\nProgram stopped by the user.")
    sys.exit(0)
