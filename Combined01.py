import bluetooth

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height

def receive_data():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)

    print("Waiting for a Bluetooth connection...")
    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    try:
        while True:
            data = client_sock.recv(1024).decode('utf-8')
            if not data:
                break
            process_data(data)
    except KeyboardInterrupt:
        pass

    print("Disconnected.")
    client_sock.close()
    server_sock.close()

def process_data(data):
    # Implement your data categorization logic here
    # For example, you can check if the data is an integer or a string
    try:
        num = int(data)
        print(f"Received an integer: {num}")
        # Categorize based on the integer data      
        Count = data
        

        
    except ValueError:
        print(f"Received a string: {data}")
        # Categorize based on the string data       
        # word = data
        
        # word = 'hello'

	wordChild = 'Charindu'
	WordReseved = data

	if wordChild == WordReseved :
	    condition = 'Correct'
    
	else:
	    condition = 'Wrong'

	word = WordReseved

	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,width,height), outline=0, fill=0)


	# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
	#font = ImageFont.truetype('Minecraftia.ttf', 8)

	# Write two lines of text.

	draw.text((x, top),  condition, font=font, fill=255)
	draw.text((x, top+20), word, font=font, fill=255)

	disp.display()
        

if __name__ == "__main__":
    receive_data()
    
    
    


