import requests
import subprocess
import sys
import random
import time
import colorama
from colorama import Fore

# KeyAuth credentials
API_URL = "https://keyauth.com/api"  # Replace with the correct URL
NAME = "punchmadeloader"
OWNER_ID = "3cwS1VOXCS"
SECRET = "613343b7bab7772419b4d98ecea6c96bbffffd4e3d543ea3d46cfe11c86910e1"
VERSION = "1.0"

class KeyAuth:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = f"{API_URL}/"

    def authenticate(self):
        try:
            response = self.session.post(f"{self.base_url}login", json={
                "name": NAME,
                "ownerid": OWNER_ID,
                "secret": SECRET,
                "version": VERSION
            })

            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    print(Fore.GREEN + "Authentication successful!")
                    return True
                else:
                    print(Fore.RED + f"Authentication failed: {data.get('message', 'Unknown error')}")
                    return False
            else:
                print(Fore.RED + f"Failed to reach KeyAuth server. Status code: {response.status_code}")
                return False
        except Exception as e:
            print(Fore.RED + f"An error occurred: {str(e)}")
            return False

# Initialize colorama
colorama.init()

# Authenticate
keyauth = KeyAuth()
if not keyauth.authenticate():
    print("Exiting...")
    input("Press Enter to exit...")
    sys.exit(1)

# Function to run shell commands
def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(Fore.RED + f"Error: {process.stderr}")
        sys.exit(process.returncode)
    print(Fore.GREEN + process.stdout)

# Function to check and install required Python packages
def check_and_install_packages():
    print(Fore.CYAN + "Checking Python installation...")
    try:
        subprocess.run(["where", "python"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Python not found. Please install Python from the Microsoft Store or check your PATH settings.")
        input("Press Enter to exit...")
        sys.exit(1)
    print(Fore.GREEN + "Python is installed.")
    print(Fore.CYAN + "Updating pip...")
    run_command("py -m pip install --upgrade pip")
    print(Fore.CYAN + "Installing Python packages...")
    run_command("py -m pip install times")
    run_command("py -m pip install colorama")
    run_command("py -m pip install random-number")
    print(Fore.GREEN + "Installation complete.")

# Call the function to check and install packages
check_and_install_packages()

# Rest of your existing code
import os
os.system('cls')

class Validator:
    # Your existing Validator class code
    # ...

# Print welcome message
print(Fore.GREEN + "  ██████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗███╗░░░███╗░█████╗░██████╗░███████╗ ")
print(Fore.GREEN + "  ██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║████╗░████║██╔══██╗██╔══██╗██╔════╝ ")
print(Fore.GREEN + "  ██████╔╝██║░░░██║██╔██╗██║██║░░╚═╝███████║██╔████╔██║███████║██║░░██║█████╗░░ ")
print(Fore.GREEN + "  ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║██████╔╝███████╗ ")
print(Fore.GREEN + "  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝ ")
print(" ")
print(Fore.GREEN + "                 ██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░")
print(Fore.GREEN + "                 ██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print(Fore.GREEN + "                 ██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗")
print(Fore.GREEN + "                 ██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝")
print(Fore.GREEN + "                 ███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║")
print(Fore.GREEN + "                 ╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")
print(" ")
print(" ")
print(Fore.WHITE + "                       made by kencarsonlover775 on discord")
print(" ")
print(" ")
print(Fore.WHITE + "How to use the cards: Make sure to have an aged account on amazon.com. Go to your payment methods and add the card as a Credit card/Debit card. Put your name on the card or someone else's, set a random expiration date, and the CVV should be 000. After adding the card, wait 2-4 weeks before buying anything.")

print(" ")
print("1. 1k")
print("2. 2k")
print("3. 5k")
print("4. 10k")
print(" ")
whatcard = input("What Card Do You Want? (1, 2, 3 or 4) ")
print(" ")
whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    howmany = input("How Many Cards Do You Want? ")
    time.sleep(1.0)
    print("Starting")
    time.sleep(1.0)
    howmany = int(howmany)

    for x in range(howmany):
        bin = "60457811425"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(Validator().validate(int(cc)))

if whatcard == 2:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578114"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(Validator().validate(int(cc)))

if whatcard == 3:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578118"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)+str(ff8)
        print(Validator().validate(int(cc)))

if whatcard == 4:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)+str(ff8)+str(ff9)+str(ff10)
        print(Validator().validate(int(cc)))

input("Press Enter to exit...")
