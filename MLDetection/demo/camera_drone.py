import cv2
import socket
import time
import threading
import datetime
import os

def receiveData():
    global response
    while True:
        try:
            response, _ = clientSocket.recvfrom(1024)
        except:
            break

def readStates():
    global battery
    while True:
        try:
            response_state, _ = stateSocket.recvfrom(256)
            if response_state != 'ok':
                response_state = response_state.decode('ASCII')
                list = response_state.replace(';', ':').split(':')
                battery = int(list[21])
        except:
            break

def sendCommand(command):
    global response
    timestamp = int(time.time() * 1000)
    clientSocket.sendto(command.encode('utf-8'), address)

    while response is None:
        if (time.time() * 1000) - timestamp > 10 * 1000:
            return False

    return response


def sendReadCommand(command):
    response = sendCommand(command)
    try:
        response = str(response)
    except:
        pass
    return response

def sendControlCommand(command):
    response = None
    for i in range(0, 5):
        response = sendCommand(command)
        if response == 'OK' or response == 'ok':
            return True
    return False

def Snapshot(frame, name):
	filename = name#"{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
	p = os.path.sep.join(('img', filename))
	# save the file
	cv2.imwrite(p, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
	print("Photo saved {}".format(filename))

#
# Main program
#

# connection info
UDP_IP = '192.168.10.1'
UDP_PORT = 8889
last_received_command = time.time()
STATE_UDP_PORT = 8890

address = (UDP_IP, UDP_PORT)
response = None
response_state = None

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind(('', UDP_PORT))
stateSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stateSocket.bind(('', STATE_UDP_PORT))

# start threads
recThread = threading.Thread(target=receiveData)
recThread.daemon = True
recThread.start()

stateThread = threading.Thread(target=readStates)
stateThread.daemon = True
stateThread.start()

# connect to drone
response = sendControlCommand("command")
print(f'command response: {response}')
response = sendControlCommand("streamon")
print(f'streamon response: {response}')

# open UDP
print(f'opening UDP video feed, wait 2 seconds ')
videoUDP = 'udp://192.168.10.1:11111'
cap = cv2.VideoCapture(videoUDP)
time.sleep(2)

# open
drone_flying = False
i = 0
while True:
    i = i + 1
    start_time = time.time()

    try:
        _, frameOrig = cap.read()
        frame = cv2.resize(frameOrig, (480, 360))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if (time.time() - start_time ) > 0:
            fpsInfo = "FPS: " + str(1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, fpsInfo, (10, 20), font, 0.4, (255, 255, 255), 1)
        if i%400==1:
            Snapshot(frame, str(i)+".jpg")

    except Exception as e:
        print(f'exc: {e}')
        pass
    if i ==2:
    	msg = "takeoff"
    	sendCommand(msg)
    if i ==400:
    	msg = "up 40"
    	sendCommand(msg)
    if i ==800:
    	msg = "forward 100"
    	sendCommand(msg)
    if i ==1200:
    	msg = "cw 90"
    	sendCommand(msg)
    if i ==1600:
    	msg = "forward 100"
    	sendCommand(msg)
    if i ==2000:
    	msg = "cw 90"
    	sendCommand(msg)
    if i ==2400:
    	msg = "forward 100"
    	sendCommand(msg)
    if i ==2800:
    	msg = "cw 90"
    	sendCommand(msg)
    if i ==3200:
    	msg = "forward 100"
    	sendCommand(msg)
    if i ==3600:
    	msg = "cw 90"
    	sendCommand(msg)
    if i == 42000:
    	break
    if cv2.waitKey(1) & 0xFF == ord('t'):
        drone_flying = True
        detection_started = True
        msg = "takeoff"
        sendCommand(msg)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        drone_flying = False
        msg = "land"
        sendCommand(msg)
        time.sleep(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
msg = "land"
sendCommand(msg)
"""
msg = "land"
sendCommand(msg) # land
response = sendControlCommand("streamoff")
print(f'streamon response: {response}')
"""
