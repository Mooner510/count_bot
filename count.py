import discord
from discord.ext import commands
from discord.utils import get
import os
import time

prefix = '!'
bot = commands.Bot(command_prefix=prefix)

global filed

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")

@bot.event
async def on_message(message):
    user = message.author.display_name
    user_id = message.author.id
    channel_id = message.channel.id
    msg = message.content
    ai = message.author.bot
    arg = msg.split()
    ac = len(arg) - 1
    use_channel = ['730076628490911794']
    admin_list = ['524868734054039554', '672604694463512581']
    if ai == True:
        a = 0
        print("1")
    elif str(channel_id) in use_channel:
        if os.path.isfile("number.txt"):
            with open("number.txt", 'r', encoding='utf-8') as file:
                filed = file.readline()
            
            if str(msg) == "reset":
                if str(user_id) in admin_list:
                    if os.path.isfile("number.txt"):
                        with open("number.txt", 'w+', encoding='utf-8') as file:
                            file.write("0")
                        await message.delete()
                        await message.channel.send("숫자를 리셋하였습니다!\n> 1부터 시작합니다")
                    else:
                        with open("number.txt", 'w+', encoding='utf-8') as file:
                            file.write("0")
                        await message.delete()
                        await message.channel.send("숫자를 리셋하였습니다!\n> 1부터 시작합니다")
                else:
                    await message.delete()
                    mm = await message.channel.send("<@" + str(user_id) + "> 너능 관리자가 아니쟈냥!")
                    time.sleep(4)
                    await mm.delete()
            elif str(arg[0]) == "set":
                if ac >= 1:
                    if str(user_id) in admin_list:
                        try:
                            if int(arg[1]) >= 0 or int(arg[1]) <= 0:
                                with open("number.txt", 'w+', encoding='utf-8') as file:
                                    file.write(str(arg[1]))
                                await message.delete()
                                await message.channel.send("숫자를 리셋하였습니다!\n> **" + str(arg[1]) + "**부터 시작합니다")
                            else:
                                await message.delete()
                        except:
                            await message.delete()
                    else:
                        await message.delete()
                        mm = await message.channel.send("<@" + str(user_id) + "> 너능 관리자가 아니쟈냥!")
                        time.sleep(4)
                        await mm.delete()
                else:
                    await message.delete()
                    mm = await message.channel.send("<@" + str(user_id) + "> 너능 관리자가 아니쟈냥!")
                    time.sleep(4)
                    await mm.delete()
            else:
                try:
                    if int(msg) == int(filed) + 1:
                        await message.delete()
                        await message.channel.send("<@" + str(user_id) + ">  :: **" + str(int(filed) + 1) + "**")

                        with open("number.txt", 'w+', encoding='utf-8') as file:
                            file.write(str(int(filed) + 1))
                    else:
                        await message.delete()
                except:
                    await message.delete()
                    channel = bot.get_channel(id=727765114912112640)
                    await channel.send(str(user) + " ▷ " + str(msg))
        else:
            with open("number.txt", 'w+', encoding='utf-8') as file:
                file.write("0")
            await message.delete()
            await message.channel.send("숫자를 리셋하였습니다!\n> 1부터 시작합니다")

token = os.environ["BOT_TOKEN"]
bot.run(token)
