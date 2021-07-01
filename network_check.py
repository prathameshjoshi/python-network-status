import socket
import time
from datetime import datetime

# Check internet connection with ping
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True

    except OSError:
        pass
    return False

# Get current time
def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

while True:
    time.sleep(2)
    check = is_connected()
    if check != True:
        print('{} : Disconnected'.format(current_time()))
    else:
        print('{} : Connected'.format(current_time()))
