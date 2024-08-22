import requests
import sys
import time
import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# KeyAuth credentials
keyauthapp = api(
    name = "punchmadeloader", # Application Name
    ownerid = "3cwS1VOXCS", # Owner ID
    secret = "613343b7bab7772419b4d98ecea6c96bbffffd4e3d543ea3d46cfe11c86910e1", # Application Secret
    version = "1.0", # Application Version
    hash_to_check = getchecksum()
)


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

def loader_animation():
    animation = ['[■□□□□□□□□□□] 10%', '[■■□□□□□□□□□] 20%', '[■■■□□□□□□□□] 30%',
                  '[████□□□□□□□] 40%', '[█████□□□□□□] 50%', '[██████□□□□□] 60%',
                  '[███████□□□□] 70%', '[████████□□□] 80%', '[█████████□□] 90%',
                  '[██████████□] 100%']
    for frame in animation:
        sys.stdout.write(f'\r{frame}')
        sys.stdout.flush()
        time.sleep(0.5)

def main():
    keyauth = KeyAuth()
    if not keyauth.authenticate():
        print(Fore.RED + "Exiting...")
        input("Press Enter to exit...")
        sys.exit(1)

    # Simulate a loader process
    print(Fore.CYAN + "Loading, please wait...")
    loader_animation()

    # Clear the console and show that loading is complete
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "Loading complete!")

if __name__ == "__main__":
    main()
