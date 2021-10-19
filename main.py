import os
import discord
from PIL import Image
import requests
from io import BytesIO
import json
import random
from keep_alive import keep_alive
import http.client

client = discord.Client()

mauy = ["kapoy", "hasul", "hasol","hahay","maka walag gana", "ambot nalang jud","binuang", "giatay"]

encourage = ["OKAY RANA OI AMONG PLAN GANE BATI KAU", "soss basta dili Impz nga way sudsud", "at least oi dili prehas ds and algo kalisod", "Chillaxxx paareeehhh", "dont be KrAzYyYyY"]

# def retrieve_msg():
#   msg = await self.get_channel(CHANNEL_ID).history(limit=1).flatten()
#   msg = msg[0]

# def love(p1,p2):
#   conn = http.client.HTTPSConnection("love-calculator.p.rapidapi.com")
#   headers = {
#     'x-rapidapi-host': "love-calculator.p.rapidapi.com",
#     'x-rapidapi-key': "c1cff50609msh839109d0dca4086p1b2805jsnd520dd1cb5f2"
#   }
#   conn.request("GET", "/getPercentage?fname={}&sname={}".format(p1,p2), headers=headers)
#   res = conn.getresponse()
#   data = res.read()
#   print(data.decode("utf-8"))

def get_advice():
  url = "https://api.adviceslip.com/advice"
  response = requests.get(url)
  json_data = json.loads(response.text)
  advice = json_data['slip']['advice']
  return advice
def get_dog_pic():
  url = "https://api.thedogapi.com/v1/images/search"
  response = requests.get(url)
  json_data = json.loads(response.text)
  imgUrl = json_data[0]['url']
  return imgUrl
def get_cat_pic():
  url = "https://api.thecatapi.com/v1/images/search"
  response = requests.get(url)
  json_data = json.loads(response.text)
  imgUrl = json_data[0]['url']
  return imgUrl

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('Hello mga b o a n g | logged in as {0.user}'.format(client))

#COMMANDS
@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
  if msg.startswith('$rant internet'):
    await message.channel.send('YAWA JUD ANING GLOBE OI. 1899 PHP AMONG PLAN NYA MURAG GIATAY')
  if msg.startswith('$pity'):
    await message.channel.send('Condolence oy haha')
  if msg.startswith('$teacher sux'):
    await message.channel.send('batia maestroha oi wa juy ayu')
  if msg.startswith('$motivation'):
    quote = get_quote()
    await message.channel.send(quote)
  if msg.startswith('$dogterte'):
    x = get_dog_pic()
    await message.channel.send(x)
  if msg.startswith('$krazy kats'):
    x = get_cat_pic()
    await message.channel.send(x)
  if msg.startswith('$advice'):
    await message.channel.send(get_advice())
  # if msg.startswith("$love {} {}"):
  #   print(string)
  #======================================CUSTOM (FROM FILE NO API)=================
  if msg.startswith('$jay'):
    with open('downloads/jay.png', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)
  if msg.startswith('$fast healing'):
    with open('downloads/rebao.png', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)
  if msg.startswith('$pasumpa'):
    with open('downloads/video-1585152035.mp4', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)
  if msg.startswith('$goodshit'):
    with open('downloads/jc suyop.jpg', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)
  if any(word in msg for word in mauy):
    await message.channel.send(random.choice(encourage))
 
keep_alive()
client.run(os.getenv('sekreto'))
