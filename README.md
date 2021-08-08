# ReadImage bot

A Discord bot that extracts text from the last image in the channel.  
The bot is deployed and can be invited via [this link](https://discord.com/api/oauth2/authorize?client_id=873485624034877481&permissions=2169856&scope=bot)

## Specifications

- Written in python, the main files are: ImageApp.py and functions.py
- Uses Google tesseract 4.00 model to extract the text
- Uses pytesseract for compatibility with python
- Uses Discord.py package to communicate with Discord API
- Supports Arabic and English

## Usage

1. [Invite the bot](https://discord.com/api/oauth2/authorize?client_id=873485624034877481&permissions=2169856&scope=bot) to your Discord server
2. Mention the bot @ReadImage under the image you want to extract the text from  
(note that it only extracts from the last image in the channel)
4. If the text is in Arabic use "@ReadImage ar"
5. To turn off Text-to-Speech use "@ReadImage off", otherwise it's automatically on.
