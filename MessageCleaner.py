import discord, asyncio
from os import system
import shutil
import subprocess
import socket, sys, discord, base64, mysql.connector, threading, requests
from tpblite import TPB
from sys import argv
import psutil
import logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
import json
import requests, os, json, time, threading
import queue as _queue
#import ctypes ctypes.windll.kernel32.SetConsoleTitleA("M")
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + ' Message Cleaner: By Darkky.')
print('  ')
print('  ')
print('{}╔╦╗┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┬  ┌─┐┌─┐┌┐┌┌─┐┬─┐{}'.format(Fore.WHITE, Fore.LIGHTWHITE_EX))
print('{}║║║├┤ └─┐└─┐├─┤│ ┬├┤   ║  │  ├┤ ├─┤│││├┤ ├┬┘{}'.format(Fore.BLUE, Fore.LIGHTWHITE_EX))
print('{}╩ ╩└─┘└─┘└─┘┴ ┴└─┘└─┘  ╚═╝┴─┘└─┘┴ ┴┘└┘└─┘┴└─{}'.format(Fore.RED, Fore.LIGHTWHITE_EX))
print(Fore.RESET)
print('  ')
token = input(f'Token = ')
init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + ' Message Cleaner: By Darkky.')
print('  ')
print('  ')
print('{}╔╦╗┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┬  ┌─┐┌─┐┌┐┌┌─┐┬─┐{}'.format(Fore.WHITE, Fore.LIGHTWHITE_EX))
print('{}║║║├┤ └─┐└─┐├─┤│ ┬├┤   ║  │  ├┤ ├─┤│││├┤ ├┬┘{}'.format(Fore.BLUE, Fore.LIGHTWHITE_EX))
print('{}╩ ╩└─┘└─┘└─┘┴ ┴└─┘└─┘  ╚═╝┴─┘└─┘┴ ┴┘└┘└─┘┴└─{}'.format(Fore.RED, Fore.LIGHTWHITE_EX))
print(Fore.RESET)
print('  ')
print('{}╔══════════════ Discord Cleaner  ══════════════╗{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║                                              ║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║            Type: $clear in chat              ║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║                                              ║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}╚══════════════════════════════════════════════╝{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()

def murder(cmd):
    subprocess.call(cmd, shell=True)
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == '$clear':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass     

client.run(token, bot=False)