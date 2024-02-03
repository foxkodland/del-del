import discord
from bot_logic import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("ну привет)")

    elif message.content.startswith('!pass'):
        await message.channel.send(gen_pass(20))
       

    elif message.content.startswith('$bye'):
        await message.channel.send("до встречи, жаль, что ты уходишь ((")

    elif 'pizza' in message.content:
        await message.channel.send("кто сказал пицца?)")

    else:
        await message.channel.send(message.content)



client.run("")
