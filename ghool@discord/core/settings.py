# All functions and assets related to settings will be stored here.

from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

settings_art = r'''
                        [01] > Back             [02] > Token Count      [03] > View Tokens


'''

def counttokens():
    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()
    
    time.sleep(0.3)

    if len(tokens) == 0:
        print("[-] " + Fore.RED + "No tokens were found!" + Style.RESET_ALL)
        input("...")
    else:
        print("[?] " + Fore.MAGENTA + "Found " + str(len(tokens)) + " tokens!" + Style.RESET_ALL)
        input("...")

def viewtokens():
    with open('assets/config/tokens.txt') as f:
        tokens = f.read()

    time.sleep(0.3)

    if tokens == "":
        print("[-] " + Fore.RED + "No tokens were found!" + Style.RESET_ALL)
        input("...")
    else:
        print("[?] " + Fore.MAGENTA + "Here are your tokens!" + Style.RESET_ALL)
        print(Fore.GREEN + tokens + Style.RESET_ALL)
        input("...")