# ReadImage bot

A Discord bot that extracts text from the last image in the channel. It uses tesseract 5.x to extract text from images, so its limitations are akin to the limitation of tesseract. 
#### Due to the limited heroku plan, the deployment is currently off. However, you can create your own clone by following "How to clone it" section.

![Bot Preview](https://user-images.githubusercontent.com/82774404/228958434-8f6b010e-9d6e-4551-b37f-cffe9b638f6b.png)

## Specifications

- Written in python, the main files are: ImageApp.py and functions.py
- Uses Google tesseract 5.x model to extract the text
- Uses pytesseract for compatibility with python
- Uses Discord.py package to communicate with Discord API
- Supports Arabic and English
- Easy commands (only need to ping)

## Usage

1. [Invite the bot](https://discord.com/api/oauth2/authorize?client_id=873485624034877481&permissions=2147555328&scope=bot) to your Discord server. If you want to invite your clone, replace YOUR_BOT_ID_HERE in the following URL: (https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_ID_HERE&permissions=2147555328&scope=bot)

2. Mention the bot @ReadImage under the image you want to extract the text from  
(note that it only extracts from the last image in the channel)

4. If the text is in Arabic use "@ReadImage ara"

5. To turn off Text-to-Speech use "@ReadImage off", otherwise it's automatically on.

## How to clone it

1. Create an application in Discord following the instructions [here](https://discordpy.readthedocs.io/en/stable/discord.html).

2. You'll need to install tesseract 5.x on the host or the place you're running this application from and install the languages you need, the bot is configured for Arabic and English by default. Tesseract [documentation](https://tesseract-ocr.github.io/tessdoc/Installation.html) will help. Locate where it's stored, this info will be used later.

3. Install the python packages named in requirements.txt

4. Clone or download this repository.

5. Open ImageApp.py and follow the commented instructions:

![Parameters](https://user-images.githubusercontent.com/82774404/228966983-0c78399f-e30c-4a0f-897c-9110833a8d5e.png)

6. Open functions.py and specify the location of your tesseract model. You can comment the command out if tesseract is in PATH as an environment variable. But for deployment purposes this must be specified.

![Tesseract location](https://user-images.githubusercontent.com/82774404/228968499-bb209ece-ffdb-40fa-9cd8-d297adff370d.png)

7. Run ImageApp.py by the command:
```cmd
python ImageApp.py
```

8. If everything is up and running, scroll up to the "Usage" section and follow it if you have not already read it. (:

## Justification

- The bot only reads the last image to keep commands as simple as possible
- Mentioning is used as a command due to the many ways commands can conflict with other bots
- The other files are important for Heroku deployment for installing and connecting dependencies
- Have tried to make the code as clean and understandable as possible 
