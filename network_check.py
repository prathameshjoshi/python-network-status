import socket
import time
from datetime import datetime

# Check internet connection with ping
def is_connected():
    try:
        countdown_start = int(time.time() * 1000)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        countdown_end = int(time.time() * 1000)
        countdown = countdown_end - countdown_start
        return True, countdown

    except OSError:
        pass
    return False, False

# Get current time
def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

while True:
    time.sleep(2)
    check, countdown = is_connected()
    if check != True:
        print('{} : Disconnected'.format(current_time()))
    else:
        print('{} : Connected {} ms'.format(current_time(), countdown))
