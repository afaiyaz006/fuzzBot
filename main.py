
import discord
import os
import random

client = discord.Client()
my_secret = os.environ['TOKEN']
motivational_quotes=[""]

trigger_list=("fuzz","fuzzy","feeling down","motivation","inspire","dull")
dialog_file="dialogs.txt"
  
with open(dialog_file,encoding="UTF-8") as myfile:
  text=myfile.read()

motivational_quotes=text.split("\n\n")  
 
  
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith(trigger_list):
        random_index=random.randint(1,len(motivational_quotes)-1)
        random_message=motivational_quotes[random_index]    
        await message.channel.send(random_message)
    
client.run(my_secret)