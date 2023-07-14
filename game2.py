import time
import serial,keyboard

# Specify the port for your Arduino board
port = 'COM6'  # Update with your Arduino port

# Define the baud rate
baud_rate = 9600

# Initialize the serial connection
ser = serial.Serial(port, baud_rate, timeout=1)

def get_distance():
    # Send a command to trigger the ultrasonic sensor
    ser.write(b'T')  # Send 'T' command

    # Read the distance measurement from the Arduino
    response = ser.readline().decode().strip()

    try:
        distance = float(response)
        return distance
    except ValueError:
        return None

while True:
    dist = get_distance()
    print(dist)
    if dist is not None:
        if 20<dist<30:
            if keyboard.is_pressed('a'):
                keyboard.release('a')
            if keyboard.is_pressed('z'):
                keyboard.release('z')
        if 0<=dist<=20:
            '''if keyboard.is_pressed('z'):
                keyboard.release('z')'''
            keyboard.press('a')
            time.sleep(0.1)
            keyboard.release('a')
        
        if dist>=30:
            '''if keyboard.is_pressed('a'):
                keyboard.release('a')'''
            keyboard.press('z')
            time.sleep(0.1)
            keyboard.release('z')
    '''if dist is not None:
        print( dist)
    else:
        print("Failed to read distance")'''
    #time.sleep(0.001)
zz