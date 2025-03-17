from pystyle import Colorate, Colors
import os
from core.settings import *
from core.raider import *
from core.webhooks import *
from core.misc import *
from core.tools import *
from colorama import Fore, init
import time
import configparser

# Initialize colorama
init(autoreset=True)

# Read the config.ini file
config = configparser.ConfigParser()
config.read(os.path.join("assets", "config", "config.ini"))

# Get the theme from the General section
themegradient = config.get("General", "themegradient", fallback="red")  # Default to 'red' if not found
themeinput = config.get("General", "themeinput", fallback="RED")

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
                        [04] > Tools            [05] > Exit

'''
        self.setup()

    def setup(self):
        os.system('cls')
        self.homemenu()

    def banner(self):
        # Apply dynamic theme to the banner color
        theme_color = getattr(Colors, themegradient + "_to_black")  # Fallback to red_to_black if theme is invalid
        print(Colorate.Vertical(theme_color, self.banner_art))
    
    def homemenu(self):
        while True:
            os.system('title ghool@MAIN')
            os.system('cls')
            self.banner()
            theme_color = getattr(Colors, themegradient + "_to_black")
            print(Colorate.Vertical(theme_color, self.home_art))
            inp = input(getattr(Fore, themeinput) + "[ghool@MENU] > ")

            if inp == "1":
                self.settingsmenu()
            elif inp == "2":
                self.raidermenu()
            elif inp == "3":
                self.webhooksmenu()
            elif inp == "4":
                self.toolsmenu()
            elif inp == "5":
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
            theme_color = getattr(Colors, themegradient + "_to_black")
            print(Colorate.Vertical(theme_color, settings_art))
            inp = input(getattr(Fore, themeinput) + "[ghool@SETTINGS] > ")

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
            theme_color = getattr(Colors, themegradient + "_to_black")
            print(Colorate.Vertical(theme_color, raider_art))
            inp = input(getattr(Fore, themeinput) + "[ghool@RAIDER] > ")

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
            elif inp == "7":
                os.system("cls")
                self.banner()
                emojiraider()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.raidermenu()

    def webhooksmenu(self):
        while True:
            os.system('title ghool@WEBHOOKS')
            os.system('cls')
            self.banner()
            theme_color = getattr(Colors, themegradient + "_to_black")
            print(Colorate.Vertical(theme_color, webhooks_art))
            inp = input(getattr(Fore, themeinput) + "[ghool@WEBHOOKS] > ")

            if inp == "1":
                self.homemenu()
            if inp == "2":
                os.system("cls")
                self.banner()
                webhookspam()
            if inp == "3":
                os.system("cls")
                self.banner()
                pastebinwebspam()
            if inp == "4":
                os.system("cls")
                self.banner()
                listwebspam()
            else:
                print(Fore.RED + "[-] Invalid Option, Please Try Again!" + Fore.RESET)
                time.sleep(1)
                self.webhooksmenu()
    
    def toolsmenu(self):
        while True:
            os.system('title ghool@TOOLS')
            os.system('cls')
            self.banner()
            theme_color = getattr(Colors, themegradient + "_to_black")
            print(Colorate.Vertical(theme_color, tools_art))
            inp = input(getattr(Fore, themeinput) + "[ghool@TOOLS] > ")

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

# Usage
if __name__ == "__main__":
    ghool = Ghool()