# All functions and assets related to settings will be stored here.

from colorama import Fore, Style, init
import time
import configparser

# Initialize colorama
init(autoreset=True)

settings_art = r'''
                        [01] > Back             [02] > Token Count      [03] > View Tokens


'''

def counttokens():
    config = configparser.ConfigParser()
    config.read('assets/config/config.ini')

    if 'UserTokens' in config:
        tokens = config['UserTokens']
        
        token_count = len(tokens)

        time.sleep(0.3)

        if token_count == 0:
            print("[-] " + Fore.RED + "No tokens were found!" + Style.RESET_ALL)
            input("...")
        else:
            print("[?] " + Fore.MAGENTA + f"Found {token_count} tokens!" + Style.RESET_ALL)
            input("...")
    else:
        print("[-] " + Fore.RED + "The 'UserTokens' section was not found in the config.ini!" + Style.RESET_ALL)
        input("...")

def viewtokens():
    config = configparser.ConfigParser()

    # Read the config.ini file
    config.read('assets/config/config.ini')

    # Check if 'UserTokens' section exists
    if 'UserTokens' in config:
        tokens = config['UserTokens']

        time.sleep(0.3)

        if len(tokens) == 0:
            print("[-] " + Fore.RED + "No tokens were found!" + Style.RESET_ALL)
            input("...")
        else:
            print("[?] " + Fore.MAGENTA + "Here are your tokens!" + Style.RESET_ALL)
            # Display only the token values
            for token_value in tokens.values():
                print(Fore.GREEN + token_value + Style.RESET_ALL)
            input("...")
    else:
        print("[-] " + Fore.RED + "The 'UserTokens' section was not found in the config.ini!" + Style.RESET_ALL)
        input("...")