# discord-ai-bot
**Author:** Paul Rakestraw
**Version:** 2.1.0
**Release Date:** April 15, 2025
**Version Update Date:** September 12, 2025

This customizable Discord chatbot is powered by OpenAI's GPT-4. It responds to user messages with tailored responses that can be changed and altered inside the source code. Built with safety and security in mind, the chatbot only operates in designated enviroments and has specific triggers for message events. 

## Latest Features 
- **Gym Motivation:** Added Harsh Gym Motivation that's activated on keywords, 'Gym', 'Motivation', or 'Lift'
- **Image Saving Capability:** The bot can now detect and save images when an image is posted in a specific text channel.
  
## Base Features 
- **AI Chat Responses:** Uses OpenAI GPT-4to respond to custom personalitiy and behavior
- **Image Sender:** Sends random '.jpg' images from a folder (non repeating) from local folder
- **Trigger Phrases:** Built with capabilties of recognizing specific keywords and special responses
- **Server Isolation Support:** Can be configured to ignore messages outside test servers
- **Memory Aware:** Remembers last image sent to avoid repeating images

## How to Run

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

4. **Set your Discord Bot Token and Text Channel Codes**
   
- Replace the 'Discord Application Key' with discord app token
- Token and bot setup can be found on Discord's developer portal
- Replace text channel codes with your own 

5. **Run the Bot**

- Run python3 bot.py or py3 bot.py in the terminal
- To have the boy run 24/7 you must find a hosting server or keep your computer on

## Configuration Tips

- Make sure to have 'Message Content Intent' enabled in the bot settings on the Discord Developer Portal
- When testing a new version it is recommended to test it on a seperate test server. You can add logic to restrict responses to a specific 'guild.id'

## Project Structure
discord-ai-bot

├── images/               # Folder containing .jpg images

├── bot.py                # Main bot script

├── README.md             # This file

├── .env                  # Encrypted file containting API keys and channel IDs


# Safety Note 
- Make sure that you do **NOT** share or hard-code sensitive credentials (like API keys or tokens) in production
- **DO NOT** insert your API keys and channel IDs directly into the code, this leaves your keys exposed. 
- **ALL** keys and channel IDs need to be saved in a .env file
 
