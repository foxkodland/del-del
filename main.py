import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):  # $hello
    await ctx.send(f'Привет! как дела?)')


@bot.command(name='дайПароль')
async def password(ctx): # $password
    await ctx.send(gen_pass(20))

@bot.command()
async def heh(ctx, count_heh = 5): # $heh 10
    await ctx.send("he" * count_heh)

@bot.event  
async def on_message(message): # ловит все текстовые сообщения
    
    if message.content == 'Привет':
        await message.channel.send("Я рад тебя видеть")

    if message.content.startswith("Привет"):
        await message.reply("Рад тебя видеть снова!", mention_author=True)


    # ответ человеку
    await message.reply("Рад тебя видеть снова!", mention_author=True)        
    
    #Важно для работы команд!! 
    await bot.process_commands(message)

bot.run("")
