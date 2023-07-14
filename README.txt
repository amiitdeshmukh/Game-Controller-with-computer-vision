Step 1: Connect Arduino board to the serial port and upload firmata into the board

Step 2: pip install the following libraries using terminal:
	1.	pyfirmata (takes input from proximity sensor using serial port)
	2.	mediapipe (used to read hand gesture using computer vision)
	3.	keyboary (used to control keyboard keys using python)

Description: 
	1.	Here we control a car in the game called “Need for Speed” where the controls are as follows:
	i.	‘a’ acceleration
	ii.	‘z’ breaks
	iii.	‘m’ right turn
	iv.	‘n’ left turn

2.	 The file ‘game1.py’ controls the left and right turn of the car as follows:
	•	We take thumb_tip(point 4 in mediapipe) and index_finger_tip(point 8 in mediapipe) to control the turn:
	•	If the distance between the point 4 and point 8 in the frame is x than for the range -45<=x<=45 the car will not take any turn
	•	For x<-45 keyboard will press ‘n’ key and car will take left turn
	•	For x>45 key board will press ‘m’ key and car will take right turn

3.	The file ‘game2.py’ controls acceleration and breaks of the car:
	•	If the serial port reads the distance between 0-20 cm from the proximity sensor then the keyboard will press ‘a’ thereby accelerating the car
	•	If it reads the distance greater then 30cm then it will apply breaks.
	•	If the distance read is in the range 20-30cm the car will run freely without any applied acceleration or breaks.
