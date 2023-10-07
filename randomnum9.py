import tkinter as tk
from PIL import Image, ImageTk
import random

def show_apple():
    # Generate a random number (replace 10 with the maximum value you want)
    random_number = random.randint(1, 10)
    
    if random_number==1:
        apple_label1.place(x=50, y=100)
    
    elif random_number==2:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
    
    elif random_number==3:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)

    elif random_number==4:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
            
    elif random_number==5:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
        apple_label5.place(x=450, y=100)    

    elif random_number==6:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
        apple_label5.place(x=450, y=100) 
        apple_label6.place(x=50, y=200)
        
        
    elif random_number==7:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
        apple_label5.place(x=450, y=100) 
        apple_label6.place(x=50, y=200)
        apple_label7.place(x=150, y=200)

    elif random_number==8:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
        apple_label5.place(x=450, y=100) 
        apple_label6.place(x=50, y=200)
        apple_label7.place(x=150, y=200)
        apple_label8.place(x=250, y=200)
        
    elif random_number==9:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
        apple_label5.place(x=450, y=100) 
        apple_label6.place(x=50, y=200)
        apple_label7.place(x=150, y=200)
        apple_label8.place(x=250, y=200)
        apple_label9.place(x=350, y=200)
        
    elif random_number==10:
        apple_label1.place(x=50, y=100)
        apple_label2.place(x=150, y=100)
        apple_label3.place(x=250, y=100)
        apple_label4.place(x=350, y=100)
        apple_label5.place(x=450, y=100) 
        apple_label6.place(x=50, y=200)
        apple_label7.place(x=150, y=200)
        apple_label8.place(x=250, y=200)
        apple_label9.place(x=350, y=200)
        apple_label10.place(x=450, y=200)

def clear_all():
    apple_label1.place_forget()
    apple_label2.place_forget()
    apple_label3.place_forget()
    apple_label4.place_forget()
    apple_label5.place_forget()
    apple_label6.place_forget()
    apple_label7.place_forget()
    apple_label8.place_forget()
    apple_label9.place_forget()
    apple_label10.place_forget()

# Set up the main window
root = tk.Tk()
root.title("EN20412852")

# Set the window size (adjust as needed)
window_width = 800
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Load image of an apple and resize it (replace with the path to your apple image)
original_image = Image.open("apple.png")
resized_image = original_image.resize((window_width // 7, window_height // 5), Image.LANCZOS)
apple_image1 = ImageTk.PhotoImage(resized_image)

# Create a second apple image
apple_image2 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image3 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image4 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image5 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image6 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image7 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image8 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image9 = ImageTk.PhotoImage(resized_image)

# Create a third apple image
apple_image10 = ImageTk.PhotoImage(resized_image)



# Create a label to display the apple image
apple_label1 = tk.Label(root, image=apple_image1)

apple_label2 = tk.Label(root, image=apple_image2)

apple_label3 = tk.Label(root, image=apple_image3)

apple_label4 = tk.Label(root, image=apple_image4)

apple_label5 = tk.Label(root, image=apple_image5)

apple_label6 = tk.Label(root, image=apple_image6)

apple_label7 = tk.Label(root, image=apple_image7)

apple_label8 = tk.Label(root, image=apple_image8)

apple_label9 = tk.Label(root, image=apple_image9)

apple_label10 = tk.Label(root, image=apple_image10)

# Button to show the apple image
show_button = tk.Button(root, text="Show Apple", command=show_apple)
show_button.place(x=250, y=350)

# Button to clear all
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.place(x=400, y=350)

# Start the GUI event loop
root.mainloop()

