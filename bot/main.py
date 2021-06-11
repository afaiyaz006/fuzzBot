import discord
import os
import random
import TenGiphPy
tenor="GKVAA6BRJEHX"
t=TenGiphPy.Tenor(tenor) 

client = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")

motivational_quotes=[""]
emoji = '\N{THUMBS UP SIGN}'

trigger_list=["fuzz","fuzzy","feeling down","motivation","inspire","dull","feeling"]
dialog_file="bot/dialogs.txt"


with open(dialog_file,encoding="UTF-8") as myfile:
  text=myfile.read()

motivational_quotes=text.split("\n\n")  
async def getGif(msg):
   gifUrl=await t.arandom("surprise")
   return gifUrl     

  
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if any(word in message.content.lower() for word in trigger_list):
        random_index=random.randint(1,len(motivational_quotes)-1)
        random_message=motivational_quotes[random_index]    
        await message.channel.send(random_message)
    if("hello" in message.content.lower()):
        await message.channel.send("Hello "+message.author.mention)
        await message.add_reaction(emoji)
    
    if("surprise" in message.content):
        #gifUrl=await t.arandom("surprise")
        mentions=[m.mention for m in message.mentions]
        if(len(mentions)>0):
          mention_list = ", ".join(mentions[:-1]) + " " + mentions[-1]
          await message.channel.send("surprise "+mention_list)
          await message.channel.send(await getGif("surprise"))
        else:
          await message.channel.send("surprise "+message.author.mention)
          await message.channel.send(await getGif("surprise"))

if __name__=="__main__":
    client.run(TOKEN)
