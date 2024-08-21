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

def main():
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
    print(Fore.WHITE + "How to use the cards: Make sure to have an aged account on amazon.com. If you do not, this may not work. Go to your payment methods and add the card as a Credit card/Debit card. Put your name on the card or someone else's, put a random expiration date, the CVV is going to be 000, and press add. After adding the card, wait 2-4 weeks before buying anything.")

    print(" ")
    print("1. 1k")
    print("2. 2k")
    print("3. 5k")
    print("4. 10k")
    print(" ")
    
    try:
        whatcard = int(input("What Card Do You Want? (1, 2, 3 or 4) "))
        if whatcard not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice. Please enter 1, 2, 3, or 4.")
        
        print(" ")
        randomnums = "0123456789"
        card_bins = {
            1: "60457811425",
            2: "604578114",
            3: "604578118",
            4: "6045781123"
        }
        
        bin_prefix = card_bins[whatcard]
        howmany = int(input("How Many Cards Do You Want? "))
        
        time.sleep(1.0)
        print("Starting")
        time.sleep(1.0)
        
        for _ in range(howmany):
            length = 6 if whatcard == 1 else 7
            random_suffix = ''.join(random.choice(randomnums) for _ in range(length))
            card_number = bin_prefix + random_suffix
            validator = Validator()
            print(validator.validate(card_number))
        
    except ValueError as ve:
        print(Fore.RED + str(ve))
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

    input("Press Enter to exit...")  # Wait for the user to press Enter

if __name__ == '__main__':
    main()
