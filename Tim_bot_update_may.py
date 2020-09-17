# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import asyncio
import random
from discord.ext.commands import Bot

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello, {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

    if 'TIM' in message.content and 'UNCLE' not in message.content and 'SOME' not in message.content:
        msg = '<:godTim:489885915653865473>'.format(message)
        await client.send_message(message.channel, msg)

    if 'uncle' in message.content and 'tim' not in message.content:
        msg = '<:tim_thonkery:384028119566123019>'.format(message)
        await client.send_message(message.channel, msg)

    if 'uncle tim' in message.content or 'Uncle Tim' in message.content and 'My name is' not in message.content:
        msg = '<:timlove:581349181080469514>'.format(message)
        await client.send_message(message.channel, msg)

    if 'UNCLE TIM' in message.content:
        msg = '<:TimSMASH:489885953872101386>'.format(message)
        await client.send_message(message.channel, msg)

    if 'tim' in message.content and 'angelique' in message.content:
        msg = '<:Timique:489885942216392714>'.format(message)
        await client.send_message(message.channel, msg)

    if 'relt' in message.content or 'RELT' in message.content:
        msg = '<:relt:489885930325409810>'.format(message)
        await client.send_message(message.channel, msg)

    if 'should I follow my Timorrow' in message.content:
         await client.send_message(message.channel, random.choice ([ "Without a doubt!", "Probably!", "Maybe!",
                                                                     "Probably not...", "My sources say no, sorry!"]))

    if 'tim play despacito' in message.content:
        msg = 'https://www.youtube.com/watch?v=kJQP7kiw5Fk'.format(message)
        await client.send_message(message.channel, msg)

    if 'play fight for your style' in message.content or 'play girls be ambitious' in message.content:
        msg = 'https://www.youtube.com/watch?v=O0DaAqkLiDw'.format(message)
        await client.send_message(message.channel, msg)

    if 'play congratulations' in message.content:
        msg = 'https://www.youtube.com/watch?v=oyFQVZ2h0V8'.format(message)
        await client.send_message(message.channel, msg)

    if 'play maria' in message.content:
        msg = 'https://www.youtube.com/watch?v=7yrVfiKrmqc'.format(message)
        await client.send_message(message.channel, msg)

    if 'play break it down' in message.content or 'play dosukoi koi koi' in message.content:
        msg = 'https://www.youtube.com/watch?v=vJPRKOFuAXI'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('are you ready dont you be afraid now'):
        msg = 'Welcome to the new stage! <:angelique:485125194327785473>'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Tim, cheer me up'):
        await client.send_message(message.channel, random.choice(["https://www.youtube.com/watch?v=eHFg3iSlOXQ",
                                                                  "https://www.youtube.com/watch?v=b3sOOBicyDY",
                                                                  "https://www.youtube.com/watch?v=EDVIg21os4w",
                                                                  "https://youtu.be/C22l82kbtGc?t=25s",
                                                                  "https://youtu.be/UNfgjBG5uuM",
                                                                  "https://youtu.be/8_Dm5xkHzio",
                                                                  "https://youtu.be/4sZuN0xXWLc",
                                                                  "https://youtu.be/sz2mmM-kN1I",
                                                                  "https://youtu.be/7cxD1CrapME",
                                                                  "https://youtu.be/phJvde3rXA4",
                                                                  "https://youtu.be/IDDdJ2lAsyI",
                                                                  "https://youtu.be/VhJ7NmU6lJI"]))

    if 'sporty' in message.content or 'Sporty' in message.content:
        msg = '<:rip_sporty:405769464546590720>'.format(message)
        await client.send_message(message.channel, msg)

    if 'flirty' in message.content or 'Flirty' in message.content:
        msg = '<:rip_flirty:405769399614832640>'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Tim, what style should I wear today'):
        await client.send_message(message.channel, random.choice(["You should wear Basic!",
                                                                  "You should wear Girly!",
                                                                  "You should wear Preppy!",
                                                                  "You should wear Lively!",
                                                                  "You should wear Sporty!",
                                                                  "You should wear Psychedelic!",
                                                                  "You should wear Feminine!",
                                                                  "You should wear Chic!",
                                                                  "You should wear Boho-chic!",
                                                                  "You should wear Eastern!",
                                                                  "You should wear Babydoll!",
                                                                  "You should wear Gothic!",
                                                                  "You should wear Flirty!",
                                                                  "You should wear Rock!",
                                                                  "You should wear Bold!!"]))

    if message.content.startswith('Tim, what pattern should I wear today'):
        await client.send_message(message.channel, random.choice(["You should wear Stripes!",
                                                                  "You should wear Checks!",
                                                                  "You should wear Dots!",
                                                                  "You should wear Flowers!",
                                                                  "You should wear Animal print!",
                                                                  "You should wear Camo!",
                                                                  "You should wear a complex pattern!!",
                                                                  "You should wear a plain pattern!",
                                                                  "You should wear a pattern with a logo!",
                                                                  "You should wear a pattern with pictures!",
                                                                  "You should wear a pattern with stars!",
                                                                  "You should wear a pattern with hearts!",
                                                                  "You should wear a pattern with ribbons!",
                                                                  "You should wear a minimal pattern!"]))

    if message.content.startswith('Tim, how much of a fashion disaster'):
        await client.send_message(message.channel, random.choice(["Zero, they're absolutely fabulous!",
                                                                  "They're a one.",
                                                                  "They're a two.",
                                                                  "They're a three.",
                                                                  "They're a four.",
                                                                  "They're a five.",
                                                                  "They're a six.",
                                                                  "They're a seven.",
                                                                  "They're an eight."
                                                                  "They're a nine."
                                                                  "They're a ten, Someone call the fashion police!."]))

    if message.content.startswith('Tim, how gay'):
        await client.send_message(message.channel, random.choice(["They're not gay at all.",
                                                                  "They're a little gay.",
                                                                  "They're kinda gay.",
                                                                  "They're pretty gay.",
                                                                  "They're really gay.",
                                                                  "They're 100% gay."]))

    if message.content.startswith('Tim, who should I take pics with'):
        await client.send_message(message.channel, random.choice(["Take pictures with Rosie!",
                                                                  "Take pictures with Alina!",
                                                                  "Take pictures with Yolanda!",
                                                                  "Take pictures with me! :smirk:",
                                                                  "Take pictures with Angelique!",
                                                                  "Take pictures with some rando lmao",
                                                                  "Take pictures with Ethan!",
                                                                  "Take pictures with Janice!",
                                                                  "Take pictures with Oliver!",
                                                                  "Take pictures with Jim!",
                                                                  "Take pictures with Johann!",
                                                                  "Take pictures with Xiaobai!",
                                                                  "Take pictures with Camilla!",
                                                                  "Take pictures with Fortman!",
                                                                  "Take pictures with Jo!",
                                                                  "Take pictures with Madeira!",
                                                                  "Take pictures with Cece!",
                                                                  "Take pictures with Lorelei!"]))

    if message.content.startswith('Tim, pick a color'):
        await client.send_message(message.channel, random.choice(["I pick White!",
                                                                  "I pick Grey!",
                                                                  "I pick Black!",
                                                                  "I pick Blue!",
                                                                  "I pick Purple!",
                                                                  "I pick Pink!",
                                                                  "I pick Red!",
                                                                  "I pick Brown!",
                                                                  "I pick Orange!",
                                                                  "I pick Yellow!",
                                                                  "I pick Green!"]))

    if message.content.startswith('Tim, what hairstyle should I get?'):
        await client.send_message(message.channel, random.choice(["You should get a crew cut!",
                                                                  "You should get a Side-swept bob!",
                                                                  "You should get a Straight bob!",
                                                                  "You should get a Tousled Crop!",
                                                                  "You should get a pageboy lmao",
                                                                  "You should get Short pigtails!",
                                                                  "You should get a bun! (or double buns.)",
                                                                  "You should get Flicked layers!",
                                                                  "You should get Bouncy spiral curls!",
                                                                  "You should get a Long & Straight!",
                                                                  "You should get Plaited Pigtails!",
                                                                  "You should get Long elegant waves!"]))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')