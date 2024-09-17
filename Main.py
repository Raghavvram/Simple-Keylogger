import keyboard
import time

while True:
    # Start recording keystrokes
    keyboard.start_recording()

    # Wait for 5 seconds while recording keystrokes
    time.sleep(5)

    # Retrieve recorded keystrokes
    outputs = keyboard.stop_recording()

    # If output is empty skip
    if len(outputs) == 0:continue
    
    # The output return a class 
    for i in outputs:
        i = str(i) # converting it to string
        elements = i.split('(')[1].split(')')[0].split()
        
        # Access the first element
        first_element = elements[0]
        
        # if it is a keypress down, then we print it (up is ignored)
        if elements[1] == "down":print(first_element)
        else: continue

    # Sleep to avoid triggering the next recording immediately
    time.sleep(0.5)

