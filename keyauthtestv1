import requests
import subprocess
import sys
import random
import time
import colorama
from colorama import Fore

# KeyAuth credentials
API_URL = "https://keyauth.com/api"
NAME = "punchmadeloader"
OWNER_ID = "3cwS1VOXCS"
SECRET = "613343b7bab7772419b4d98ecea6c96bbffffd4e3d543ea3d46cfe11c86910e1"
VERSION = "1.0"

class KeyAuth:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = f"{API_URL}/"

    def authenticate(self):
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

# Initialize colorama
colorama.init()

# Authenticate
keyauth = KeyAuth()
if not keyauth.authenticate():
    print("Exiting...")
    sys.exit(1)

# Initialize colorama
colorama.init()

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
    
    # Check if Python is installed
    try:
        subprocess.run(["where", "python"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Python not found. Please install Python from the Microsoft Store or check your PATH settings.")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print(Fore.GREEN + "Python is installed.")

    # Ensure pip is up-to-date
    print(Fore.CYAN + "Updating pip...")
    run_command("py -m pip install --upgrade pip")
    
    # Install required Python packages
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
    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648', '649'] or self.cardNumber[0:2] in ['65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if isinstance(number, bool) or isinstance(number, float): return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            self.cardNumber = number
            self.__findBrand()
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN + f'[!] {self.cardNumber} Is valid')
                with open("cards.txt", "w") as file:
                    file.write(repr(number))
            else:
                print(Fore.WHITE + f'{self.cardNumber} Is not valid')
        else:
            return 'Not a valid Credit Card Number'

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
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(Validator().validate(int(cc)))

if whatcard == 4:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "6045781123"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)
        print(Validator().validate(int(cc)))

input("Press Enter to exit...")
