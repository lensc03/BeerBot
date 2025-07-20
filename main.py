import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_ID = 1396523890104074392 
FORUM_CHANNEL_ID = 1396397698927562752
POST_THREAD_ID = 1396400667702071397

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

@bot.event
async def on_member_update(before, after):
    role = after.guild.get_role(ROLE_ID)
    if role in after.roles and role not in before.roles:
        print(f"{after} hat die Rolle erhalten")

        forum_channel = after.guild.get_channel(FORUM_CHANNEL_ID)
        if forum_channel:
            thread = forum_channel.get_thread(POST_THREAD_ID)
            if thread:
                await thread.send(f"{after.mention} hat die Rolle erhalten!")
            else:
                print("⚠️ Thread nicht gefunden.")
        else:
            print("⚠️ Forum-Kanal nicht gefunden.")

        await after.remove_roles(role, reason="Automatisch entfernt")

bot.run(os.getenv("TOKEN"))
