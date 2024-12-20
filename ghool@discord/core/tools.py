# All functions and assets related to tools will be stored here.

from colorama import Fore, Style, init
import time
import threading
import requests
import random
import string

tools_art = r'''
                        [01] > Back             [02] > Token Checker    [03] > Nitro Generator


'''

def checker():
    print(Fore.YELLOW + "[>] You are about to check that all of your tokens are active." + Style.RESET_ALL)

    # Read tokens from the input file
    with open('assets/input/checker/tokens.txt') as f:
        tokens = f.read().splitlines()

    print(Fore.YELLOW + "[>] Checking " + str(len(tokens)) + " tokens." + Style.RESET_ALL)

    # List to store valid tokens
    valid_tokens = []

    # Function to send a request and check token validity
    def send(token):
        url = 'https://discord.com/assets/d11b723fa5510fa3c0bd.js'
        headers = {'Authorization': token}

        response = requests.get(url, headers=headers)

        # If the response is successful (status code 200 or 204), add the token to the valid_tokens list
        if response.status_code in [200, 204]:
            print(Fore.GREEN + f'Token Active! | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            valid_tokens.append(token)
        else:
            print(Fore.RED + f'Token Inactive! | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
    
    threads = []

    # Start a thread for each token
    for token in tokens:
        thread = threading.Thread(target=send, args=(token,))
        thread.start()
        threads.append(thread)
        time.sleep(1)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Write the valid tokens to the output file
    with open('assets/output/checker/valid.txt', 'w') as output_file:
        for token in valid_tokens:
            output_file.write(f"{token}\n")

    print(Fore.YELLOW + "[>] Process complete. Valid tokens saved to 'output/checker/tokens.txt'" + Style.RESET_ALL)
    input(Fore.YELLOW + "[>] Press Any Key To Continue! " + Style.RESET_ALL)

def nitrogen():
    nitlnk = input(Fore.MAGENTA + "[?] How many nitro links do you want to generate? (or 'b' to go back): " + Style.RESET_ALL)
    if nitlnk.lower() == 'b':
        return  # Go back to main menu

    if not nitlnk.isdigit():
        print(Fore.RED + "[-] Invalid. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return
    
    characters = string.ascii_letters + string.digits

    for i in range(int(nitlnk)):
        random_string = ''.join(random.choice(characters) for _ in range(17))
        gift_link = f"https://discord.gift/{random_string}"

        print(Fore.YELLOW + gift_link)
        time.sleep(0.1)
    
    input(Fore.YELLOW + "[>] Press Any Key To Continue")