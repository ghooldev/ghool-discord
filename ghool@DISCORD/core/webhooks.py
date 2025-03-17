# All functions and assets related to webhooks will be stored here.

from colorama import Fore, Style
import time
import requests
import os
import random

webhooks_art = r'''
                        [01] > Back             [02] > Spammer          [03] > Pastebin
                        [04] > List             [05] > Controller


'''

def webhookspam():
    print(Fore.YELLOW + "[>] You are about to start controlling a webhook." + Style.RESET_ALL)

    weburl = input(Fore.MAGENTA + "[?] Enter a Webhook URL (or 'b' to go back): " + Style.RESET_ALL)
    if weburl.lower() == 'b':
        return
    
    msg = input(Fore.MAGENTA + "[?] Enter a Message to Spam (or 'b' to go back): " + Style.RESET_ALL)
    if msg.lower() == 'b':
        return
    
    if not msg:
        print(Fore.RED + "[-] Message cannot be empty. Please enter a message." + Style.RESET_ALL)
        time.sleep(1)
        return
    
    username = input(Fore.MAGENTA + "[?] Enter a Webhook Username (or 'b' to go back): " + Style.RESET_ALL)
    if username.lower() == 'b':
        return
    
    if not username:
        print(Fore.RED + "[-] Username cannot be empty. Please enter a username." + Style.RESET_ALL)
        time.sleep(1)
        return

    # Message content
    data = {
        "content": msg,
        "username": username
    }

    os.system("cls")

    print(Fore.YELLOW + "[>] Starting webhook controller with " + weburl + Style.RESET_ALL)

    while True:
        # Sending the message
        response = requests.post(weburl, json=data)

        # Check the response
        if response.status_code == 204:
            print(Fore.GREEN + f'Message Successful | {weburl[:12]} | {response.status_code}' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'Message Unsuccessful | {weburl[:12]} | {response.status_code}' + Style.RESET_ALL)

def pastebinwebspam():
    print(Fore.YELLOW + "[>] You are about to start spamming a webhook." + Style.RESET_ALL)

    weburl = input(Fore.MAGENTA + "[?] Enter a Webhook URL (or 'b' to go back): " + Style.RESET_ALL)
    if weburl.lower() == 'b':
        return
    
    username = input(Fore.MAGENTA + "[?] Enter a Webhook Username (or 'b' to go back): " + Style.RESET_ALL)
    if username.lower() == 'b':
        return
    
    if not username:
        print(Fore.RED + "[-] Username cannot be empty. Please enter a username." + Style.RESET_ALL)
        time.sleep(1)
        return

    with open('assets/messages/webhooks/pastebin.txt') as f:
        messages = f.read().splitlines()
    
    os.system("cls")

    print(Fore.YELLOW + "[>] Starting webhook spammer with " + weburl + Style.RESET_ALL)

    while True:
        msg = random.choice(messages)

        # Message content
        data = {
            "content": msg,
            "username": username
        }

        # Sending the message
        response = requests.post(weburl, json=data)

        # Check the response
        if response.status_code == 204:
            print(Fore.GREEN + f'Message Successful | {weburl[:12]} | {response.status_code}' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'Message Unsuccessful | {weburl[:12]} | {response.status_code}' + Style.RESET_ALL)

def listwebspam():
    print(Fore.YELLOW + "[>] You are about to start spamming a webhook." + Style.RESET_ALL)

    weburl = input(Fore.MAGENTA + "[?] Enter a Webhook URL (or 'b' to go back): " + Style.RESET_ALL)
    if weburl.lower() == 'b':
        return
    
    username = input(Fore.MAGENTA + "[?] Enter a Webhook Username (or 'b' to go back): " + Style.RESET_ALL)
    if username.lower() == 'b':
        return
    
    if not username:
        print(Fore.RED + "[-] Username cannot be empty. Please enter a username." + Style.RESET_ALL)
        time.sleep(1)
        return
    
    os.system("cls")

    with open('assets/messages/webhooks/list.txt') as f:
        messages = f.read().splitlines()

    print(Fore.YELLOW + "[>] Starting webhook spammer with " + weburl + Style.RESET_ALL)

    for msg in messages:

        # Message content
        data = {
            "content": msg,
            "username": username
        }

        # Sending the message
        response = requests.post(weburl, json=data)

        # Check the response
        if response.status_code == 204:
            print(Fore.GREEN + f'Message Successful | {weburl[:12]} | {response.status_code}' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'Message Unsuccessful | {weburl[:12]} | {response.status_code}' + Style.RESET_ALL)