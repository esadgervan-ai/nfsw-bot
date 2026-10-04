import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")

@bot.command(name="nsfwyardim")
@commands.nsfw()
async def nsfwyardim(ctx):
    embed = discord.Embed(
        title="🔞 NSFW Menü",
        description="Komutlar: `!foto`, `!gif`, `!video`, `!rastgeleansfw`",
        color=discord.Color.dark_red()
    )
    await ctx.send(embed=embed)

@bot.command(name="foto")
@commands.nsfw()
async def foto(ctx):
    linkler = [
        "https://images.google.com/search?q=hot+model+photography+aesthetic",
        "https://images.google.com/search?q=sensual+dark+art+photo"
    ]
    await ctx.send(f"📸 Fotoğraf: {random.choice(linkler)}")

@bot.command(name="gif")
@commands.nsfw()
async def gif(ctx):
    linkler = [
        "https://images.google.com/search?q=sensual+aesthetic+gif",
        "https://images.google.com/search?q=dark+mood+gif+animation"
    ]
    await ctx.send(f"🎞️ GIF: {random.choice(linkler)}")

@bot.command(name="video")
@commands.nsfw()
async def video(ctx):
    linkler = [
        "https://images.google.com/search?q=hot+model+clips+aesthetic",
        "https://images.google.com/search?q=dark+sensual+video+mood"
    ]
    await ctx.send(f"🎥 Video: {random.choice(linkler)}")

@bot.command(name="rastgeleansfw")
@commands.nsfw()
async def rastgeleansfw(ctx):
    linkler = [
        "https://images.google.com/search?q=hot+model+wallpaper",
        "https://images.google.com/search?q=sensual+dark+aesthetic"
    ]
    await ctx.send(f"🎲 Rastgele: {random.choice(linkler)}")

TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
