# ReadImage bot

#### Due to the limited heroku plan, the deployment is currently off. If you want to use it, please let me know (:

A Discord bot that extracts text from the last image in the channel. It uses tesseract 5.x to extract text from images, so its limitations are akin to the limitation of tesseract. 
The bot is not hosted anywhere currently but it can be invited via [this link](https://discord.com/api/oauth2/authorize?client_id=873485624034877481&permissions=2169856&scope=bot) 

## Specifications

- Written in python, the main files are: ImageApp.py and functions.py
- Uses Google tesseract 5.x model to extract the text
- Uses pytesseract for compatibility with python
- Uses Discord.py package to communicate with Discord API
- Supports Arabic and English
- Easy commands (only need to ping)

## Usage

1. [Invite the bot](https://discord.com/api/oauth2/authorize?client_id=873485624034877481&permissions=2169856&scope=bot) to your Discord server
2. Mention the bot @ReadImage under the image you want to extract the text from  
(note that it only extracts from the last image in the channel)
4. If the text is in Arabic use "@ReadImage ar"
5. To turn off Text-to-Speech use "@ReadImage off", otherwise it's automatically on.

## Justification

- The bot only reads the last image to keep commands as simple as possible
- Mentioning is used as a command due to the many ways commands can conflict with other bots
- The other files are important for Heroku deployment for installing and connecting dependencies
- Have tried to make the code as clean and understandable as possible 
