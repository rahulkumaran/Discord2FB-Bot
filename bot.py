import discord
from discord.ext import commands
import facebook
from discord.ext.commands import Bot

Client = discord.Client()
bot = commands.Bot(command_prefix = "/")	#Tells what the prefix before every command should be.

@bot.event
async def on_ready():
	'''
	Function to just tell us that the
	bot is not active. Everytime you run
	the script this will come up as a confirmation
	'''
	print("Confirmation that "+ bot.user.name + "(" + bot.user.id + ") is running now for you!")

@bot.command(pass_context=True)
async def post(ctx, link_post: str):
	'''
	Command to help share a post on facebook.
	Make sure to pass the link of the post as an argument
	example: /post facebook.com
	MAKE SURE YOUR ACCESS TOKEN IS FOR V2.7
	'''
	graph = facebook.GraphAPI(access_token = "<ENTER YOUR ACCESS TOKEN HERE>", version="2.7")	#Creating object for GraphAPI.
	graph.put_object(parent_object = "me", connection_name = "feed", message = "#PyconIndia #PyconIndia2018 #PyCon :D ", link = link_post)	#Posts on your behalf on facebook.
	await bot.say(":smiley: Done posting it! Glad to help you! :smiley:")	#Sends message to user on discord once posted 

@bot.command()
async def info():
	'''
	Gives necessary info about the bot
	'''
	embed = discord.Embed(title="FBPost Bot", description = "Post on Facebook from Discord using this bot!")
	embed.add_field(name="Author", value="Rahul Arulkumaran")
	await bot.say(embed=embed)

bot.remove_command('help')

@bot.command()
async def help():
	'''
	Gives the list and highlights 
	of what each bot command does
	'''
	embed = discord.Embed(title="FBPost Bot", description = "Post on Facebook from Discord using this bot!")
	embed.add_field(name="/post <post_link>", value="This command posts the given link as your status on Facebook!")
	embed.add_field(name="/info", value="Gives a little info about the bot", inline=False)
	embed.add_field(name="/help", value="Gives this message", inline=False)
	await bot.say(embed=embed)

if(__name__ == "__main__"):
	bot.run("NDUyNDU4MTk5NDEzNjg2Mjg1.DfRt0w.lXARLomO6Em-wmOu6WVdaGp2O9E")	#Do not change this token
