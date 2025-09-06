'''import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQxMDU4MjIwMTQxNzk5MDE1NA.GLTK-g.O1ocfU0mehtZlHCG4PkQLzGKRg_P_SXf7zpGNQ') # Replace with your own token.
async def on_message(self, message):
  if message.author == self.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello World!')'''

import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
         print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # Don't let the bot respond to itself
        if message.author == self.user:
            return  

        # Respond when someone types "$hello"
        if message.content == ("$meme"):
            await message.channel.send(get_meme())

# Enable intents so bot can read messages
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("MTQxMDU4MjIwMTQxNzk5MDE1NA.GLTK-g.O1ocfU0mehtZlHCG4PkQLzGKRg_P_SXf7zpGNQ")
