import os
import discord
from functions import *


# Configuration
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = discord.Client()


@bot.event
async def on_ready():
    '''Notify the readiness of the bot'''
    print(
        f'{bot.user} is connected'
    )


@bot.event
async def on_message(message):
    '''Runs everytime a message is sent to detect a mention'''
    if message.author == bot.user:
        return
    
    # Check if bot id in message for a ping
    if "873485624034877481" in message.content:  
        print("Mention detected".center(100, '-'))
        if 'ar' in message.content:
            lang = 'ara'
        else:
            lang = 'eng'
        
        # Look up the last 200 messages in the channel
        async for mes in message.channel.history(limit=200):
            if mes.attachments:
                # get the last attachment
                url = str(mes.attachments[-1])
                if is_image(url):
                    print("Last image in channel detected".center(100, '-'))
                    try:
                        print("Getting OCR response".center(100, '-'))
                        # Get image text and replace probably mistaken chars
                        response = process_image(url, lang).replace("|", "I").replace("\n", " ")
                        print("Text was successfully processed".center(100, '-'))
                        await message.channel.send(response, tts=True)
                    except:
                        await message.channel.send("Sorry, no text found.")
                    return
        await message.channel.send("No image found in the last 200 messages.")
                    

bot.run(TOKEN)
