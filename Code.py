import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Hola(ctx):
    await ctx.send(f'Hola, soy un bot que sirve para enseñarte como cuidar el medio ambiente! {bot.user}!')

@bot.command()
async def Ambiente(ctx,):
    await ctx.send("El ambiente es el conjunto de elementos naturales y artificiales que rodean a los seres vivos y que influyen en su desarrollo y supervivencia. Estos elementos incluyen el aire, el agua, el suelo, la flora y la fauna, así como también los edificios, las carreteras y otras construcciones humanas.")
@bot.command()
async def mem(ctx):
    with open('plantar/plantar.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def Cuidar(ctx,):
    await ctx.send("1.-Cerrar los grifos que no se utilicen y arreglar las fugas de agua. 2.-Separar la basura en distintos botes según el tipo de residuo: orgánico, vidrio, cartón, plástico y tóxico. 3.-Plantar árboles y sembrar frutas y hortalizas para mejorar la calidad del aire y la biodiversidad.")

bot.run("TU TOKEN!")
