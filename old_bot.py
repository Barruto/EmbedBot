import os

import discord
import requests
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    #guild = discord.utils.get(client.guilds, name=GUILD)

    #print(
    #    f'{client.user} is connected to the following guild:\n'
    #    f'{guild.name}(id: {guild.id})'
    #)

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    #if message.content == '99!':
        #response = random.choice(brooklyn_99_quotes)
        #await message.channel.send(response)
    #elif message.content == 'raise-exception':
        #raise discord.DiscordException
    
    #TWITTER HANDLER
    if message.content.startswith('https://www.twitter.com/') or message.content.startswith('https://x.com/'):

        responseList = message.content.split(".com")
        response = "https://vxtwitter.com" + responseList[1]
        await message.channel.send(response) 

    #TIKTOK HANDLER
    if message.content.startswith('https://tiktok.com/'):
        responseList = message.content.split(".com")
        response = "https://vxtiktok.com" + responseList[1]
        await message.channel.send(response)

    if message.content.startswith('https://vm.tiktok.com/'):
        print(message.content)
        
        # Setup chrome driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open a website
        driver.get(message.content)
        
        # print json contentget_url = driver.current_url
        get_url = driver.current_url
        print("The current url is:"+str(get_url))
        
        driver.quit()

        responseList = get_url.split(".com")
        response = "https://vxtiktok.com" + responseList[1]
        await message.channel.send(response) 
        
    #REDDIT HANDLER
    if message.content.startswith('https://www.reddit.com/'):
        responseList = message.content.split(".com")
        response = "https://rxddit.com" + responseList[1]
        await message.channel.send(response) 




@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)