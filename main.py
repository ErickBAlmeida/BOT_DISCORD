import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv("private/.env")

from config import Canais

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.command()
async def ajuda(ctx:commands.Context):
    await ctx.reply(f""" Lista de comandos:

`.ola` -> Vai te cumprimentar
""")

@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.name

    if nome == 'yrlz':
        await ctx.reply("VAI TOMAR NO CU " + nome)
    else: 
        await ctx.reply(F"Opa, {nome}, bão?")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = Canais.Bem_vindo
    await canal.send(f"🎣 BAGRE FISGADO!!! {membro.mention} acabou de entrar no servidor!!")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        canal = after.channel

        if canal.id == 1420576410983989248:
            if len(canal.members) == 1:
                diretoria = Canais.Diretoria
                await diretoria.send(f"@everyone hora da call")

@bot.event
async def on_ready():
    Canais.Bem_vindo = bot.get_channel(1431693927488032891)
    Canais.Diretoria = bot.get_channel(1426320430607896666)
    print("Bot inicializado!")
    

bot.run(os.getenv("TOKEN"))