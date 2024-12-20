# This is the main file which brings everything together!

from pystyle import Colorate, Colors
import os
import subprocess
import sys
from core.settings import *
from core.raider import *
from core.webhooks import *
from core.misc import *
from core.tools import *
from core.help import *
from core.nuker import *
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Ghool:
    def __init__(self):
        self.banner_art = r'''
                                                  __                __
                                           ____ _/ /_  ____  ____  / /
                                          / __ `/ __ \/ __ \/ __ \/ / 
                                         / /_/ / / / / /_/ / /_/ / /  
                                         \__, /_/ /_/\____/\____/_/   
                                         /____/                     
                                      _________________________________

'''
        self.home_art = r'''
                        [01] > Settings         [02] > Raider           [03] > Webhooks
                        [04] > Tools            [05] > Nuker            [06] > Help
                                                [07] > Exit

'''
        self.setup()

    def setup(self):
        os.system('cls')
        self.homemenu()

    def banner(self):
        print(Colorate.Vertical(Colors.white_to_black, self.banner_art))
    
    def homemenu(self):
        while True:
            os.system('title ghool@MAIN')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, self.home_art))
            inp = input(F"[ghool@MENU] > ")

            if inp == "1":
                self.settingsmenu()
            elif inp == "2":
                self.raidermenu()
            elif inp == "3":
                self.webhooksmenu()
            elif inp == "4":
                self.toolsmenu()
            elif inp == "5":
                self.nukermenu()
            elif inp == "6":
                self.helpmenu()
            elif inp == "7":
                exitghool()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.homemenu()

    def settingsmenu(self):
        while True:
            os.system('title ghool@SETTINGS')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, settings_art))
            inp = input(F"[ghool@SETTINGS] > ")

            if inp == "1":
                print(f"[-] {Fore.RED}Returning to Home Menu...")
                self.homemenu()
            elif inp == "2":
                counttokens()
                self.settingsmenu()
            elif inp == "3":
                viewtokens()
                self.settingsmenu()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.settingsmenu()

    def raidermenu(self):
        while True:
            os.system('title ghool@RAIDER')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, raider_art))
            inp = input(F"[ghool@RAIDER] > ")

            if inp == "1":
                self.homemenu()
            elif inp == "2":
                os.system("cls")
                self.banner()
                raider()
            elif inp == "3":
                os.system("cls")
                self.banner()
                pastebinraider()
            elif inp == "4":
                os.system("cls")
                self.banner()
                listraider()
                input(Fore.MAGENTA + "[?] Press any key to continue!" + Fore.RESET)
            elif inp == "5":
                os.system("cls")
                self.banner()
                typing()
            elif inp == "6":
                os.system("cls")
                self.banner()
                message()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.raidermenu()

    def webhooksmenu(self):
        while True:
            os.system('title ghool@WEBHOOKS')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, webhooks_art))
            inp = input(F"[ghool@WEBHOOKS] > ")

            if inp == "1":
                self.homemenu()
            if inp == "2":
                os.system("cls")
                self.banner()
                webhookspam()
            if inp == "3":
                os.system("cls")
                self.banner()
                ()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.webhooksmenu()
    
    def toolsmenu(self):
        while True:
            os.system('title ghool@TOOLS')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, tools_art))
            inp = input(F"[ghool@TOOLS] > ")

            if inp == "1":
                self.homemenu()
            if inp == "2":
                os.system("cls")
                self.banner()
                checker()
            if inp == "3":
                os.system("cls")
                self.banner()
                nitrogen()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.toolsmenu()
    
    def nukermenu(self):
        while True:
            os.system('title ghool@NUKER')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, nuker_art))
            inp = input(F"[ghool@NUKER] > ")

            if inp == "1":
                self.homemenu()
            elif inp == "2":
                delete_channels()
            elif inp == "3":
                delete_roles()
            elif inp == "4":
                kick_all()
            elif inp == "5":
                ban_all()
            elif inp == "6":
                create_channels()
            elif inp == "8":
                create_webhooks()
            elif inp == "9":
                delete_webhooks()
            elif inp == "10":
                spam_webhooks()
            elif inp == "11":
                set_server_name()
            elif inp == "12":
                set_server_icon()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.nukermenu()
    
    def helpmenu(self):
        while True:
            os.system('title ghool@HELP')
            os.system('cls')
            self.banner()
            print(Colorate.Vertical(Colors.white_to_black, help_art))
            inp = input(F"[ghool@HELP] > ")

            if inp == "1":
                self.homemenu()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.helpmenu()

# Usage
if __name__ == "__main__":
    ghool = Ghool()