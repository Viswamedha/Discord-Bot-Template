from discord import activity
from discord.ext import commands
import discord
from decouple import config

TOKEN = config('TOKEN')
PREFIX = config('PREFIX')

bot = commands.Bot(
    command_prefix = PREFIX,
    help_command = None,
    case_insensitive = True,
    description = 'Test Bot',
    activity = discord.Activity(type=discord.ActivityType.watching, name="for `"+ PREFIX +"help`"),
)

@bot.command(name = 'help')
async def _help(context: commands.Context, command: str = None):
    embed = discord.Embed(title = 'Help', description = 'Hello this is the help command! ')
    if command is None:
        embed.add_field(name = 'Commands', value = '```ping, hello, bye```', inline = False)
        embed.add_field(name = 'Usage', value = '`Use `'+ PREFIX +'help <command>` for more specific support! ')
    elif command == 'ping':
        embed.add_field(name = 'Ping', value = 'Returns a response of Pong! ')
    elif command == 'hello':
        embed.add_field(name = 'Hello', value = 'Makes you feel better! ')
    elif command == 'bye':
        embed.add_field(name = 'Bye', value = 'Makes me feel sad! ')
    await context.send(embed = embed)
    
@bot.command()
async def ping(context: commands.Context):
    await context.send('Pong! ')

@bot.command()
async def hello(context: commands.Context):
    await context.reply('Hi!')

@bot.command()
async def bye(context: commands.Context):
    await context.reply('ByeBye :wave:')

if __name__ == '__main__':
    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        bot.close()



