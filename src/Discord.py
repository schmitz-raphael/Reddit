import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os
import reddit_bot


#load env
load_dotenv()
#get the token
token = os.getenv("TOKEN")


#create an instance of the discord bot
bot = commands.Bot()

#also create an instance of the wrapper class for reddit
reddit_bot = reddit_bot.Bot()



#create an on_ready event handler
@bot.event
async def on_ready():
    #print
    print(f'We have logged in as {bot.user}')

#create an on_message event handler
async def on_message(message):
    print("Hello")
    posts = reddit_bot.getMostRecentPosts("PedroPeepos")

    for post in posts:
        await bot.get_channel(1241113176787914823).send(post.title)


bot.run(token)
