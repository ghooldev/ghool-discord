# All functions and assets related to raider will be stored here.

from colorama import Fore, Style, init
import time
import threading
import requests
import random
import os

raider_art = r'''
                        [01] > Back             [02] > Spammer          [03] > Pastebin
                        [04] > List             [05] > Typing


'''

def raider():
    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()
        
    os.system(f"title ghool@RAIDER w/ tokens: {len(tokens)}")  # Use len(tokens) to display the count
    print(Fore.YELLOW + "[>] You are about to start spamming a channel with a custom message." + Style.RESET_ALL)
    chid = input(Fore.MAGENTA + "[?] Enter a Channel ID (or 'b' to go back): " + Style.RESET_ALL)
    if chid.lower() == 'b':
        return  # Go back to main menu

    if not chid.isdigit():
        print(Fore.RED + "[-] Invalid Channel ID. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    msg = input(Fore.MAGENTA + "[?] Enter a Message to Spam (or 'b' to go back): " + Style.RESET_ALL)
    if msg.lower() == 'b':
        return

    if not msg:
        print(Fore.RED + "[-] Message cannot be empty. Please enter a message." + Style.RESET_ALL)
        time.sleep(1)
        return
    
    threadnum = input(Fore.MAGENTA + "[?] How many threads? (Per Token) (or 'b' to go back): " + Style.RESET_ALL)
    if threadnum.lower() == 'b':
        return  # Go back to main menu

    if not threadnum.isdigit():
        print(Fore.RED + "[-] Invalid Thread Number. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    threadnum = int(threadnum)

    os.system("cls")

    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()

    print(Fore.YELLOW + "[>] Starting spam process with " + str(len(tokens)) + " tokens." + Style.RESET_ALL)

    def spam(token, chid, message):
        while True:
            url = f'https://discord.com/api/v9/channels/{chid}/messages'
            headers = {'Authorization': token}
            data = {'content': message}

            response = requests.post(url, json=data, headers=headers)

            if response.status_code in [200, 204]:
                print(Fore.GREEN + f'Message Successful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'Message Unsuccessful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)

    # List to hold threads
    threads = []

    # Start threads for each token based on threadnum
    for token in tokens:
        for _ in range(threadnum):
            thread = threading.Thread(target=spam, args=(token, chid, msg))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

def pastebinraider():
    # Read tokens early to know their count
    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()

    os.system(f"title ghool@RAIDER w/ tokens: {len(tokens)}")  # Use len(tokens) to display the count
    print(Fore.YELLOW + "[>] You are about to start spamming a channel with messages from Pastebin." + Style.RESET_ALL)
    chid = input(Fore.MAGENTA + "[?] Enter a Channel ID (or 'b' to go back): " + Style.RESET_ALL)
    if chid.lower() == 'b':
        return  # Go back to main menu

    if not chid.isdigit():
        print(Fore.RED + "[-] Invalid Channel ID. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    threadnum = input(Fore.MAGENTA + "[?] How many threads? (Per Token) (or 'b' to go back): " + Style.RESET_ALL)
    if threadnum.lower() == 'b':
        return  # Go back to main menu

    if not threadnum.isdigit():
        print(Fore.RED + "[-] Invalid Thread Number. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    threadnum = int(threadnum)

    os.system("cls")

    # Messages are read after validating the inputs
    with open('assets/messages/tokens/pastebin.txt') as f:
        messages = f.read().splitlines()

    print(Fore.YELLOW + "[>] Starting spam process with " + str(len(tokens)) + " tokens and " + str(len(messages)) + " messages." + Style.RESET_ALL)

    def spam(token, chid):
        while True:
            message = random.choice(messages)
            url = f'https://discord.com/api/v9/channels/{chid}/messages'
            headers = {'Authorization': token}
            data = {'content': message}

            response = requests.post(url, json=data, headers=headers)

            if response.status_code in [200, 204]:
                print(Fore.GREEN + f'Message Successful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'Message Unsuccessful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)

    # List to hold threads
    threads = []

    # Start threads for each token based on threadnum
    for token in tokens:
        for _ in range(threadnum):
            thread = threading.Thread(target=spam, args=(token, chid))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

def typing():
        # Read tokens early to know their count
    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()

    os.system(f"title ghool@RAIDER w/ tokens: {len(tokens)}")  # Use len(tokens) to display the count
    print(Fore.YELLOW + "[>] You are about to start typing in a channel." + Style.RESET_ALL)
    chid = input(Fore.MAGENTA + "[?] Enter a Channel ID (or 'b' to go back): " + Style.RESET_ALL)
    if chid.lower() == 'b':
        return

    threadnum = input(Fore.MAGENTA + "[?] How many threads? (Per Token) (or 'b' to go back): " + Style.RESET_ALL)
    if threadnum.lower() == 'b':
        return  # Go back to main menu

    if not threadnum.isdigit():
        print(Fore.RED + "[-] Invalid Thread Number. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    threadnum = int(threadnum)
    
    os.system("cls")

    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()

    print(Fore.YELLOW + "[>] Starting typing process with " + str(len(tokens)) + " tokens." + Style.RESET_ALL)

    def spam(token, chid):
        while True:
            url = f'https://discord.com/api/v9/channels/{chid}/typing'
            headers = {'Authorization': token}

            response = requests.post(url, headers=headers)

            if response.status_code in [200, 204]:
                print(Fore.GREEN + f'[+] Request Successful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'[-] Request Unsuccessful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            
            time.sleep(3)
    
    threads = []

    # Start a thread for each token
    for token in tokens:
        thread = threading.Thread(target=spam, args=(token, chid))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def message():
        print(Fore.YELLOW + "[>] You are about to send a single message using all tokens in a channel." + Style.RESET_ALL)
        chid = input(Fore.MAGENTA + "[?] Enter a Channel ID (or 'b' to go back): " + Style.RESET_ALL)
        if chid.lower() == 'b':
            return

        if not chid.isdigit():
            print(Fore.RED + "[-] Invalid Channel ID. Please enter a numeric value." + Style.RESET_ALL)
            time.sleep(1)
            message()
        
        msg = input(Fore.MAGENTA + "[?] Enter a Message to Send (or 'b' to go back): " + Style.RESET_ALL)
        if msg.lower() == 'b':
            return
        
        if not msg:
            print(Fore.RED + "[-] Message cannot be empty. Please enter a message." + Style.RESET_ALL)
            time.sleep(1)
            message()
        
        os.system("cls")

        with open('assets/config/tokens.txt') as f:
            tokens = f.read().splitlines()

        print(Fore.YELLOW + "[>] Starting send process with " + str(len(tokens)) + " tokens." + Style.RESET_ALL)

        def send(token, chid, message):
            url = f'https://discord.com/api/v9/channels/{chid}/messages'
            headers = {'Authorization': token}
            data = {'content': message}

            response = requests.post(url, json=data, headers=headers)

            if response.status_code in [200, 204]:
                print(Fore.GREEN + f'Message Successful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'Message Unsuccessful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
        
        threads = []

        # Start a thread for each token
        for token in tokens:
            thread = threading.Thread(target=send, args=(token, chid, msg))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

def listraider():
    # Read tokens early to know their count
    with open('assets/config/tokens.txt') as f:
        tokens = f.read().splitlines()

    os.system(f"title ghool@RAIDER w/ tokens: {len(tokens)}")  # Use len(tokens) to display the count
    print(Fore.YELLOW + "[>] You are about to start spamming a channel with messages from List." + Style.RESET_ALL)
    chid = input(Fore.MAGENTA + "[?] Enter a Channel ID (or 'b' to go back): " + Style.RESET_ALL)
    if chid.lower() == 'b':
        return  # Go back to main menu

    if not chid.isdigit():
        print(Fore.RED + "[-] Invalid Channel ID. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    threadnum = input(Fore.MAGENTA + "[?] How many threads? (Per Token) (or 'b' to go back): " + Style.RESET_ALL)
    if threadnum.lower() == 'b':
        return  # Go back to main menu

    if not threadnum.isdigit():
        print(Fore.RED + "[-] Invalid Thread Number. Please enter a numeric value." + Style.RESET_ALL)
        time.sleep(1)
        return

    threadnum = int(threadnum)

    os.system("cls")

    # Messages are read after validating the inputs
    with open('assets/messages/tokens/list.txt') as f:
        messages = f.read().splitlines()

    print(Fore.YELLOW + "[>] Starting spam process with " + str(len(tokens)) + " tokens and " + str(len(messages)) + " messages." + Style.RESET_ALL)

    def spam(token, chid):
        for message in messages:
            url = f'https://discord.com/api/v9/channels/{chid}/messages'
            headers = {'Authorization': token}
            data = {'content': message}

            response = requests.post(url, json=data, headers=headers)

            if response.status_code in [200, 204]:
                print(Fore.GREEN + f'Message Successful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'Message Unsuccessful | {token[:12]} | {response.status_code}' + Style.RESET_ALL)

    # List to hold threads
    threads = []

    # Start threads for each token based on threadnum
    for token in tokens:
        for _ in range(threadnum):
            thread = threading.Thread(target=spam, args=(token, chid))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()