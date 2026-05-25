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

bot = commands.Bot(command_prefix="!", intents=intents)

class VerifyButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.success, custom_id="ragecore_verify")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        role_name = "Verified"

        role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role is None:
            role = await interaction.guild.create_role(name=role_name)

        if role in interaction.user.roles:
            await interaction.response.send_message(
                "You are already verified.",
                ephemeral=True
            )
            return

        await interaction.user.add_roles(role)

        embed = discord.Embed(
            title="✅ Verification Complete",
            description="Welcome to Ragecore Services.",
            color=0xffffff
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.event
async def on_ready():
    bot.add_view(VerifyButton())
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="setupverify", description="Create the verification panel.")
@app_commands.checks.has_permissions(administrator=True)
async def setupverify(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Ragecore Services Verification",
        description=(
            "Click the button below to verify and gain access to the server."
        ),
        color=0xffffff
    )

    file = discord.File("ragecore_logo.png", filename="ragecore_logo.png")
    embed.set_thumbnail(url="attachment://ragecore_logo.png")
    embed.set_footer(text="Ragecore Services")

    await interaction.channel.send(
        embed=embed,
        file=file,
        view=VerifyButton()
    )

    await interaction.response.send_message(
        "Verification panel created.",
        ephemeral=True
    )

@setupverify.error
async def setupverify_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message(
            "You need administrator permissions to use this command.",
            ephemeral=True
        )

bot.run(TOKEN)
