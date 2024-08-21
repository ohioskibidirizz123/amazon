import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()







class validator():

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
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
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
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
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
                print(Fore.GREEN)
                return f'[!] {self.cardNumber} Is not valid'
                file = open("cards.txt", "w")
                number = repr(number)
                file.write(number)
                file.close()
            else:
                print(Fore.RED)
                return f' {self.cardNumber} Is not valid'
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
print("How to use the cards: Make sure to have a aged account on amazon.com if you do not this may not work. Go to your payment methods and add the card as a Credit card/Debit card put your name on the card or someone elses put a random experation date the cvv is gonna be 000 and press add. After adding the card wait 2-4 weeks before buying anything")





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
        print(validator().validate(int(cc)))

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
        print(validator().validate(int(cc)))

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
        print(validator().validate(int(cc)))

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
        print(validator().validate(int(cc)))
