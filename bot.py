import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class VerifyButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.success, custom_id="verify_button")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):

        role = discord.utils.get(interaction.guild.roles, name="Verified")

        if role is None:
            role = await interaction.guild.create_role(name="Verified")

        await interaction.user.add_roles(role)

        await interaction.response.send_message(
            "✅ You are now verified!",
            ephemeral=True
        )

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="setupverify", description="Setup the verification system")
async def setupverify(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Ragecore Services Verification",
        description="Click the button below to verify.",
        color=discord.Color.dark_gray()
    )

    file = discord.File("ragecore_logo.png", filename="ragecore_logo.png")

embed.set_thumbnail(url="https://raw.githubusercontent.com/frozenxi1143/ragecore-services-bot/main/ragecore_logo.png")

await interaction.channel.send(
    embed=embed,
    view=view,
    file=file
)

bot.run(TOKEN)
