import discord
from discord.ext import commands
import facebook
from discord.ext.commands import Bot

Client = discord.Client()
bot = commands.Bot(command_prefix = "/")

@bot.event
async def on_ready():
	print("Logged in as "+ bot.user.name + " " + bot.user.id)

@bot.command(pass_context=True)
async def post(ctx, link_post: str):
	graph = facebook.GraphAPI(access_token = "EAACEdEose0cBAHUUH7siZCrHjohpFdZBrHhC7Y4BrHYTOWIDfurklFR7P3QBaQOr3d2KdyYoTXCmdJ8hvvucbl9ZAtld5T2pGbafqVc6Qffn1EAWYoYYSVcaimLhZCgZBsQVQZCMpZBEgAhWhPuYwPJCUJr2fPR52AkP6EyeWwWKeuohie6MVdRCJTj7sW0P9cWloO2AaVM7AZDZD", version="2.7")

	graph.put_object(parent_object = "me", connection_name = "feed", message = "#PyconIndia #PyconIndia2018 #PyCon :D ", link = link_post)
	await bot.say(":smiley: Done posting it! Glad to help you! :smiley:")

@bot.command()
async def info():
	embed = discord.Embed(title="FBPost Bot", description = "Post on Facebook from Discord using this bot!")
	embed.add_field(name="Author", value="Rahul Arulkumaran")

	await bot.say(embed=embed)

bot.remove_command('help')

@bot.command()
async def help():
	embed = discord.Embed(title="FBPost Bot", description = "Post on Facebook from Discord using this bot!")
	embed.add_field(name="/post <post_link>", value="This command posts the given link as your status on Facebook!")
	embed.add_field(name="/info", value="Gives a little info about the bot", inline=False)
	embed.add_field(name="/help", value="Gives this message", inline=False)
	await bot.say(embed=embed)

bot.run("NDUyNDU4MTk5NDEzNjg2Mjg1.DfRt0w.lXARLomO6Em-wmOu6WVdaGp2O9E")
