import socket
import time

from rich.console import Console
console = Console()


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

if __name__ == '__main__':
    while True:
        time.sleep(2)
        check, countdown = is_connected()
        if check != True:
            console.log(f'Disconnected', style="bold red")
        else:
            console.log(f'Connected {countdown} ms', style='bold green')
