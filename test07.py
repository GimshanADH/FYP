import tkinter as tk
import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for physical buttons
button_dictation_pin = 17  # Replace with the actual GPIO pin number for dictation button
button_car_pin = 18  # Replace with the actual GPIO pin number for car button
button_status_pin = 19  # Replace with the actual GPIO pin number for status button

# Set up button press event detection
GPIO.setup(button_dictation_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_car_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_status_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create the main window
root = tk.Tk()
root.title("EN20412852")

# Set the initial size of the main window
root.geometry("400x300")  # Adjust the dimensions as needed

# Your array or string data (replace this with your actual data)
data_to_display = "Educational play set"

# Create a label to display the text
text_label = tk.Label(root, text=data_to_display, font=("Helvetica", 16))
text_label.pack()

# Function to update the displayed text
def dictation_activity():
    new_data3 = "Write the words on paper"
    text_label.config(text=new_data3)

# Function to update the displayed text to "Hello"
def car_activity():
    hello_text = "Car"
    text_label.config(text=hello_text)

# Function to update the display status
def dictation_status():
    global word_child, WordReseved, condition, word_app
    if word_child == WordReseved:
        status_text = condition
    else:
        status_text = f"<<<You are {condition}>>>\n >>Correct Word is {word_app}<<"
    text_label.config(text=status_text)

# Callback function for dictation button press event
def button_dictation_pressed(channel):
    dictation_activity()

# Callback function for car button press event
def button_car_pressed(channel):
    car_activity()

# Callback function for status button press event
def button_status_pressed(channel):
    dictation_status()

# Set up button press event detection
GPIO.add_event_detect(button_dictation_pin, GPIO.FALLING, callback=button_dictation_pressed, bouncetime=300)
GPIO.add_event_detect(button_car_pin, GPIO.FALLING, callback=button_car_pressed, bouncetime=300)
GPIO.add_event_detect(button_status_pin, GPIO.FALLING, callback=button_status_pressed, bouncetime=300)

# Button to update the text (just for demonstration purposes)
update_button = tk.Button(root, text="Dictation", command=dictation_activity)
update_button.pack(side="left", padx=10, pady=10)

# Button to trigger the "Say Hello" action
mic_button = tk.Button(root, text="Car", command=car_activity)
mic_button.place(x=70, y=200)

# Button to trigger the "Say Hello" action
status_button = tk.Button(root, text="Status", command=dictation_status)
status_button.place(x=70, y=200)

# Start the GUI event loop
root.mainloop()

# Clean up GPIO on script exit
GPIO.cleanup()

