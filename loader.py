import http.client
import json
import sys
import time
import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# KeyAuth credentials
API_HOST = "keyauth.win"
API_ENDPOINT = "/api/1.2/"
API_PARAMS = {
    "type": "init",
    "ver": "1.0",
    "name": "loader",  # Replace with your application name
    "ownerid": "3cwS1VOXCS",  # Replace with your owner ID
    "hash": "null",
    "token": "null",
    "thash": "null"
}

def authenticate():
    conn = http.client.HTTPSConnection(API_HOST)
    payload = ''
    headers = {
        'User-Agent': 'Apidog/1.0.0 (https://apidog.com)'
    }
    
    # Construct the full URL with parameters
    url = f"{API_ENDPOINT}?{ '&'.join(f'{key}={value}' for key, value in API_PARAMS.items()) }"
    
    try:
        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        
        # Print the response data for debugging
        print(Fore.WHITE + "Response from KeyAuth server:")
        print(data)
        
        # Check if authentication was successful
        response_json = json.loads(data)
        if response_json.get("success"):
            print(Fore.GREEN + "Authentication successful!")
            return True
        else:
            print(Fore.RED + f"Authentication failed: {response_json.get('message', 'Unknown error')}")
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
    try:
        if not authenticate():
            print(Fore.RED + "Exiting...")
            input("Press Enter to exit...")
            sys.exit(1)

        # Simulate a loader process
        print(Fore.CYAN + "Loading, please wait...")
        loader_animation()

        # Clear the console and show that loading is complete
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + "Loading complete!")

    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {str(e)}")
    finally:
        # Pause to keep the window open after execution
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
