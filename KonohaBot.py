import discord
from discord.ext import commands

#Token
token = 'NzM2ODg2MDgxMTM1NDQ0MDIx.Xx1UpA.wDzxUvrH98pft70NxYTKtCbh77g'

#Prefix
PREFIX = '!'
client = commands.Bot(command_prefix= PREFIX)
client.remove_command('help')

#Bot connected
@client.event
async def on_ready():
    print("Bot connected")

    await client.change_presence(activity = discord.Game('Конохе ({}'.format(PREFIX) + 'help)'))

#Auto rol
@client.event
async def on_member_join(member):
    chennel = client.get_channel(711720653828522044)
    role = discord.utils.get(member.guild.roles, id = 711730219207098439)
    print("user connected")
    await member.add_roles(role)
    # await = chennel.send(embed = discord.Embed(description = f'Игрок {member.name} присоеденился к тусе'))

@client.event
async def on_member_join(member):
    print("user connected")

@client.event
async def on_member_remove(member):
    print("user remove")

#command !hello
@client.command(pass_context=True)
async def hello(ctx):
    
    await ctx.send(embed=discord.Embed(description="Дороу"))

#!info
@client.command()
async def info(ctx):
    emb = discord.Embed(title = '*#заявка-на-вступление*', url='https://discord.gg/4a4nMJD', description='**Чтобы вступить в город вы должны оформить заявку следующего форматика А4:**', color=0xff6400)
    emb.set_author(name='Город Коноха', url='https://discord.gg/4a4nMJD', icon_url='https://img.pngio.com/naruto-konoha-leaf-village-symbol-sticker-naruto-in-2019-konoha-symbol-png-1064_1064.png')
    emb.set_thumbnail(url='https://sun1-93.userapi.com/Hl4N_tWMTttCd_QJyf75t7Dz36kZbk1jIKmiSw/dI25OU11fb8.jpg')
    emb.add_field(name='**1. Представтесь пожалуйста**', value='имя/ник', inline=False)
    emb.add_field(name='**2. Солько часов в сутки вы играете на сервере? Сколько из них вы готовы посвятить конкретно городу?**', value='1/24. 1/24', inline=False)
    emb.add_field(name='**3. Сколько вам лет?**', value='18', inline=False)
    emb.add_field(name='**4. Ваш пол?**', value='мужской/женский', inline=False)
    emb.add_field(name='**5. Что вы умеете?**', value='строитель/фермер/ресурсер и тд', inline=False)
    emb.add_field(name='**6. Почему мы именно вы?**', value='потому что я крутой', inline=False)
    emb.add_field(name='**7. Почему именно наш город?**', value='потому что вы крутые', inline=False)
    emb.add_field(name='**8. Какую пользу вы принесёте городу?**', value='буду какать', inline=False)
    emb.add_field(name='**9. Как хорошо вы ладите с людьми?**', value='отлично/плохо', inline=False)
    emb.add_field(name='**10. Будете ли вы слушаться, и выполнять задания?**', value='да/нет', inline=False)
    emb.add_field(name='**11. Доп инфа от вас**', value='я воняю попой', inline=False)
    emb.add_field(name='​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀', value='​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀', inline=False)
    emb.add_field(name='*P.S Если вы строитель/фермер/ланшафтер и тд придоставте скрины ваших построек/ферм и тд.*', value='***чтобы повысить шанс принятия в город***', inline=False)
    emb.add_field(name='*Также шанс принятия в город сиьно возрастёт если вы:*', value='***Крутой строитель, деффка, или друг Наруто***', inline=False)
    emb.set_footer(text='P.S.S При вступлении в город вы получаете роль "На испытательном сроке". Это значит, что на ближайшем собрании города вас кикнут или добавят полноценно. Если вы не будете только АФКшить, воровать ресурсы, и не приносить ничего в материальном, рабочем или интелектуальном плане - кик. Если вы мудак, или не нравитесь большенству жителей, или вы соврали оформляя заявку - кик до собрания')
    
    await ctx.channel.purge(limit = 1)
    await ctx.author.send(embed=emb)

#!ad
@client.command()
async def ad(ctx, arg):
    emb = discord.Embed(title = '**ОБЪЯВЛЕНИЕ:**', description=('**'+ arg +'**'), color=0xff0000)
    emb.set_author (name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.set_thumbnail (url='https://cdn.pixabay.com/photo/2017/03/28/01/42/attention-2180765_1280.png')

    await ctx.channel.purge(limit = 1)
    await ctx.send(embed=emb)

#help
@client.command()
async def help(ctx):
    emb = discord.Embed(title = '**НАВИГАЦИЯ ПО КОМАНДАМ:**', color=0x0000ff)
    emb.set_thumbnail (url='https://www.pinclipart.com/picdir/big/94-944880_big-image-exclamation-mark-clipart.png')
    emb.add_field(name = '1. **{}help'.format(PREFIX) + '**', value = '`навигация по командам`', inline=False)
    emb.add_field(name = '2. **{}hello'.format(PREFIX) + '**', value = '`просто приветствие с ботом`', inline=False)
    emb.add_field(name = '3. **{}info'.format(PREFIX) + '**', value = '`вся онформация о вступлении в город`', inline=False)
    emb.add_field(name = '4. **{}ad'.format(PREFIX) + '**', value = '`сделать красивое объявление (текст писать в кавычках "текст")`', inline=False)

    await ctx.channel.purge(limit = 1)
    await ctx.send(embed=emb)

#run bot
client.run(token)













# python D:\Код\Python\KonohaBot.py
# python D:\Код\Python\TestBot.py


# class MyClient(discord.Client):
#     async def on__ready(self):
#         print ('Loggen on as {0}!'.format(self.user))

# async def on_message(self, message):
#     print("Message from {0.author}: {0.content}".format(message))


# #join auto roles
# @client.event
# async def on_member_join(member):
#     channel = client.get_channel(724876875293261878)

#     role = discord.utils.get(member.guild.roles, id = 740521519666430014)

#     await member.add_roles(role)
#     await channel.send(embed = discord.Embed(description = f'*Добро пожаловать в discord Конохи, ''{member.name}''. Надеюсь тебе здесь понравтся!*', color = 0x0c0c0c))
# print("Auto role work")


# async def test(ctx):
#     embed = discord.Embed(title заявка-на-вступление, url=https: // discord.gg/4a4nMJD, description=Чтобы вступить в город вы должны оформить заявку следующего форматика А4:, color=0xff0000)
#     embed.set_author(name=Город Коноха, url=https: // discord.gg/4a4nMJD, icon_url=https: // img.pngio.com/naruto-konoha-leaf-village-symbol-sticker-naruto-in-2019-konoha-symbol-png-1064_1064.png)
#     embed.set_thumbnail(url=https: // sun1-93.userapi.com/Hl4N_tWMTttCd_QJyf75t7Dz36kZbk1jIKmiSw/dI25OU11fb8.jpg)
#     embed.add_field(name=1. Представтесь пожалуйста, value=имя/ник, inline=False)
#     embed.add_field(name=2. Солько часов в сутки вы играете на сервере? Сколько из них вы готовы посвятить конкретно городу?, value=от 1 до 24. от 1 до 24, inline=False)
#     embed.add_field(name=3. Сколько вам лет?, value=18, inline=False)
#     embed.add_field(name=4. Ваш пол?, value=мужской/женский, inline=False)
#     embed.add_field(name=5. Что вы умеете?, value=строитель/фермер/ресурсер и тд, inline=False)
#     embed.add_field(name=6. Почему мы именно вы?, value=потому что я крутой, inline=False)
#     embed.add_field(name=7. Почему именно наш город?, value=потому что вы крутые, inline=False)
#     embed.add_field(name=8. Какую пользу вы принесёте городу?, value=буду какать, inline=False)
#     embed.add_field(name=9. Как хорошо вы ладите с людьми?, value=отлично/плохо, inline=False)
#     embed.add_field(name=10. Будете ли вы слушаться, и выполнять задания?, value=да/нет, inline=False)
#     embed.add_field(name=11. Доп инфа от вас, value=я воняю попой, inline=True)
#     embed.add_field(name=P.S Если вы строитель/фермер/ланшафтер и тд придоставте скрины ваших построек/ферм и тд., value=в этом случае шанс принятия в город сильно вырастет, inline=True)
#     embed.add_field(name=Шанс принятия в город сиьно возрастёт если вы:, value=Крутой строитель, деффка, или друг Наруто, inline=True)
#     embed.set_footer(text=P.S.S При вступлении в город вы получаете роль "На испытательном сроке". Это значит, что на ближайшем собрании города вас кикнут или добавят полноценно. Если вы не будете только АФКшить, воровать ресурсы, и не приносить ничего в материальном, рабочем или интелектуальном плане - кик. Если вы мудак, или не нравитесь большенству жителей, или вы соврали оформляя заявку - кик до собрания)
#     await self.bot.say(embed=embed)
