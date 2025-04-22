# discord-ai-bot
**Author:** Paul Rakestraw
**Version:** 2.0.0
**Release Date:** April 15, 2025

This customizable Discord chatbot is powered by OpenAI's GPT-4. It responds to user messages with tailored responses that can be changed and altered inside the source code. Built with safety and security in mind, the chatbot only operates in designated enviroments and has specific triggers for message events. 

## Features 

- **AI Chat Responses:** Uses OpenAI GPT-4to respond to custom personalitiy and behavior
- **Image Sender:** Sends random '.jpg' images from a folder (non repeating) from local folder
- **Trigger Phrases:** Built with capabilties of recognizing specific keywords and special responses
- **Server Isolation Support:** Can be configured to ignore messages outside test servers
- **Memory Aware:** Remembers last image sent to avoid repeating images

# How to Run

1. **Install dependencies**

- Install discord.py
  - Mac/linux: python3 -m pip install -U discord.py
  - Windows: py -3 -m pip install -U discord.py
- Install OpenAI API
  - All systems: pip install openai

2. **Prepare image folder**

- Place '.jpg' images of your choice in a folder called images in the same directory as the script
  
3. **Set your API key**

- Replace the 'api_key' place holders at the top (OpenAI)

4. **Set your Discord Bot Token**
   
- Replace the 'Discord Application Key' with discord app token
- Token and bot setup can be found on Discord's developer portal

5. **Run the Bot**

- Run python3 bot.py or py3 bot.py in the terminal
- To have the boy run 24/7 you must find a hosting server or keep your computer on

## Configuration Tips

- Make sure to have 'Message Content Intent' enabled in the bot settings on the Discord Developer Portal
- When testing a new version it is recommended to test it on a seperate test server. You can add logic to restrict responses to a specific 'guild.id'

# Project Structure
discord-ai-bot

├── images/               # Folder containing .jpg images

├── bot.py                # Main bot script

├── README.md             # This file


# Safety Note 
- Make sure that you do **NOT** share or hard-code sensitive credentials (like API keys or tokens) in production
- This script is still in it's early development and still needs adaption for secure deployment
 
