# ---------------------------------------------
# Uni the Cat Discord Bot Test🐾
# Author: Paul Rakestraw
# Version: 2.0.3
# Date Released: April 15, 2025
#
# Description:
# A playful and interactive Discord bot powered by OpenAI.
# Uni responds to messages with cat-like charm and can attach
# random images of Uni from a local image folder. Designed
# with testing support, environment-safe handling, and GPT-4
# personality generation.
#
# Key Features:
# - Responds to "* uni *" with GPT-4 messages
# - Sends random non-repeating images of Uni
# - Auto-loads .jpg files from /images folder
# - Ignores messages outside designated test server (if enabled)
# - Supports keyword triggers like "uni image" or "uni picture"
# ---------------------------------------------


from imaplib import Commands
import discord
import random
import os
from openai import OpenAI

# Initialize OpenAI
chatter = OpenAI(api_key='openai key')

# List of Uni's adorable images
uni_pictures = [f for f in os.listdir("images") if f.lower().endswith(".jpg")]

# Create a custom client
class Client(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_image = None  # 🔁 Track last image sent

    async def on_ready(self):
        print(f'🐾 Bot online as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # === If user posts image in the 'upload-image' channel ===
        if message.channel.id == 1413362818484404387:
            if message.attachments:
                for attachment in message.attachments:
                    if attachment.filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                        folder = "images"
                        os.makedirs(folder, exist_ok=True)

                        filepath = os.path.join(folder, attachment.filename)
                        await attachment.save(filepath)

                        print("Photo saved")

                        return

        msg = message.content.lower()

        # === If the user requests an image ===
        if 'uni' in msg and ('image' in msg or 'picture' in msg):
            available_images = [img for img in uni_pictures if img != self.last_image]
            image_file = random.choice(available_images)
            image_path = os.path.join("images", image_file)

            if os.path.exists(image_path):
                try:
                    file = discord.File(image_path, filename=image_file)
                    await message.channel.send(file=file)
                    self.last_image = image_file
                    return
                except Exception as e:
                    print(f"Failed to send image: {e}")
                    await message.channel.send("Oops! I couldn't find my favorite fur-tograph 😿")

        # === Otherwise, normal Uni reply ===
        elif 'uni' in msg:
            
            username = message.author.display_name if message.guild else message.author.name

            print(f"Message from {message.author}: {message.content}")
            if 'uni' in msg and ('gym' in msg or 'motivation' in msg or 'workout' in msg or 'lift' in msg):
                print("Gym Motivation Statement")
                response = chatter.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"Write a brutal self depricating gym motivation sentence with no quotes that relates to the message. End the statement with 'From uni'"},
                    {"role": "user", "content": message.content}
                ],
                n=1
                )
            elif random.random() < 0.4:
                response = chatter.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are Uni the Cat. Respond to a user named {username} with a playful,mean tone, and greet them personally."},
                    {"role": "user", "content": message.content}
                ],
                n=1
            )
            else:
                response = chatter.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are Uni the Cat. Respond to a user named {username} with a playful,cat-like tone, and greet them personally."},
                    {"role": "user", "content": message.content}
                ],
                n=1
            )

            reply = response.choices[0].message.content.strip()
            print(f"🗨️ Uni replied to : {reply}")
            print(f"Token Usage {response.usage.total_tokens}")

            if random.random() < 0.2:
                available_images = [img for img in uni_pictures if img != self.last_image]
                image_file = random.choice(available_images)
                image_path = os.path.join("images", image_file)

                if os.path.exists(image_path):
                    try:
                        file = discord.File(image_path, filename=image_file)
                        await message.channel.send(reply, file=file)
                        self.last_image = image_file
                        return
                    except Exception as e:
                        print(f"Failed to send image: {e}")

            await message.channel.send(reply)

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Start the bot
client = Client(intents=intents)
client.run('Discord application key')
