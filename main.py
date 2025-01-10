import discord
from discord.ext import commands
import requests
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot has connected to Discord!')
#############################################################
class botones_generar_MD_10(discord.ui.View):
    def __init__(self, message):
        super().__init__(timeout=None)
        self.message = message
        self.bot = bot
    @discord.ui.button(label="💻10", style=discord.ButtonStyle.blurple)
    async def inviteBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        
        await self.message.edit(content="""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;33mGenerando b1ns...[0m

```""", view=None)
        for _ in range(10):
         code = random.randint(100000, 999999)
         url = f"https://data.handyapi.com/bin/{code}"
         response = requests.get(url)
         data = response.json()            
         status = data['Status']
         if status == 'SUCCESS':
          await user.send(f"""```ansi
[2;31m[2;36mVALID: {code}[0m[2;31m[0m
```""")
         elif status == 'NOT FOUND': 
          await user.send(f"""```ansi
[2;31mINVALID: {code}[0m
```""")
         else:
          await user.send(f"""```ansi
[2;31mERROR: https://discord.com/developers ha denegado la conexion[0m
```""")


        channel = bot.get_channel(1246269326676463656)
        if channel:
            user_id = interaction.user.id
            embed = discord.Embed(title="`💻`Se han generado b1ns`💻`", description=f"""---------------------------------
**<:coin:1245137042325770361> B1NS GENERADOS: 10

<:usuario:1245137045421035611> USUARIO:  <@{user_id}>

<:dev:1245137043894440049> POWERED BY <@1063538352638394460>**""", color=0x06ebeb)
            embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
            embed.set_footer(text="TX G3N")
            await channel.send(embed=embed)
                
            
        await user.send(f"""```ansi
POWERED BY @santiagortega

[2;33mSe han generado los b1ns[0m

```""")
        
    @discord.ui.button(label="❌50", style=discord.ButtonStyle.gray)
    async def Error_50(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        await user.send("""```ansi
[2;31mERROR: No tienes permisos para generar [2;32m[2;36m50 b1ns[0m[2;32m[0m[2;31m[0m
```""")

    @discord.ui.button(label="❌100", style=discord.ButtonStyle.gray)
    async def Error_100(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        await user.send("""```ansi
[2;31mERROR: No tienes permisos para generar [2;32m[2;36m100 b1ns[0m[2;32m[0m[2;31m[0m
```""")
class botones_generar_MD_50(discord.ui.View):
    def __init__(self, message):
        super().__init__(timeout=None)
        self.message = message
        self.bot = bot
    @discord.ui.button(label="💻10", style=discord.ButtonStyle.blurple)
    async def Gen_10(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user

        await self.message.edit(content="""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;33mGenerando b1ns...[0m

```""", view=None)
        for _ in range(10):
         code = random.randint(100000, 999999)
         url = f"https://data.handyapi.com/bin/{code}"
         response = requests.get(url)
         data = response.json()            
         status = data['Status']
         if status == 'SUCCESS':
          await user.send(f"""```ansi
[2;31m[2;36mVALID: {code}[0m[2;31m[0m
```""")
         elif status == 'NOT FOUND': 
          await user.send(f"""```ansi
[2;31mINVALID: {code}[0m
```""")
         else:
          await user.send(f"""```ansi
[2;31mERROR: https://discord.com/developers ha denegado la conexion[0m
```""")


        channel = bot.get_channel(1246269326676463656)
        if channel:
            user_id = interaction.user.id
            embed = discord.Embed(title="`💻`Se han generado b1ns`💻`", description=f"""---------------------------------
**<:coin:1245137042325770361> B1NS GENERADOS: 10

<:usuario:1245137045421035611> USUARIO:  <@{user_id}>

<:dev:1245137043894440049> POWERED BY <@1063538352638394460>**""", color=0x06ebeb)
            embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
            embed.set_footer(text="TX G3N")
            await channel.send(embed=embed)


        await user.send(f"""```ansi
POWERED BY @santiagortega

[2;33mSe han generado los b1ns[0m

```""")

    @discord.ui.button(label="💻50", style=discord.ButtonStyle.blurple)
    async def Gen_50(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user

                await self.message.edit(content="""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;33mGenerando b1ns...[0m

```""", view=None)
                for _ in range(50):
                 code = random.randint(100000, 999999)
                 url = f"https://data.handyapi.com/bin/{code}"
                 response = requests.get(url)
                 data = response.json()            
                 status = data['Status']
                 if status == 'SUCCESS':
                  await user.send(f"""```ansi
        [2;31m[2;36mVALID: {code}[0m[2;31m[0m
        ```""")
                 elif status == 'NOT FOUND': 
                  await user.send(f"""```ansi
        [2;31mINVALID: {code}[0m
        ```""")
                 else:
                  await user.send(f"""```ansi
        [2;31mERROR: https://discord.com/developers ha denegado la conexion[0m
        ```""")


                channel = bot.get_channel(1246269326676463656)
                if channel:
                    user_id = interaction.user.id
                    embed = discord.Embed(title="`💻`Se han generado b1ns`💻`", description=f"""---------------------------------
        **<:coin:1245137042325770361> B1NS GENERADOS: 50

        <:usuario:1245137045421035611> USUARIO:  <@{user_id}>

        <:dev:1245137043894440049> POWERED BY <@1063538352638394460>**""", color=0x06ebeb)
                    embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
                    embed.set_footer(text="TX G3N")
                    await channel.send(embed=embed)


                await user.send(f"""```ansi
        POWERED BY @santiagortega

        [2;33mSe han generado los b1ns[0m

        ```""")
        

    @discord.ui.button(label="❌100", style=discord.ButtonStyle.gray)
    async def Error_100(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        await user.send("""```ansi
[2;31mERROR: No tienes permisos para generar [2;32m[2;36m100 b1ns[0m[2;32m[0m[2;31m[0m
```""")

class botones_generar_MD_100(discord.ui.View):
    def __init__(self, message):
        super().__init__(timeout=None)
        self.message = message
        self.bot = bot
    @discord.ui.button(label="💻10", style=discord.ButtonStyle.blurple)
    async def Gen_10(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user

        await self.message.edit(content="""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;33mGenerando b1ns...[0m

```""", view=None)
        for _ in range(10):
         code = random.randint(100000, 999999)
         url = f"https://data.handyapi.com/bin/{code}"
         response = requests.get(url)
         data = response.json()            
         status = data['Status']
         if status == 'SUCCESS':
          await user.send(f"""```ansi
[2;31m[2;36mVALID: {code}[0m[2;31m[0m
```""")
         elif status == 'NOT FOUND': 
          await user.send(f"""```ansi
[2;31mINVALID: {code}[0m
```""")
         else:
          await user.send(f"""```ansi
[2;31mERROR: https://discord.com/developers ha denegado la conexion[0m
```""")


        channel = bot.get_channel(1246269326676463656)
        if channel:
            user_id = interaction.user.id
            embed = discord.Embed(title="`💻`Se han generado b1ns`💻`", description=f"""---------------------------------
**<:coin:1245137042325770361> B1NS GENERADOS: 10

<:usuario:1245137045421035611> USUARIO:  <@{user_id}>

<:dev:1245137043894440049> POWERED BY <@1063538352638394460>**""", color=0x06ebeb)
            embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
            embed.set_footer(text="TX G3N")
            await channel.send(embed=embed)


        await user.send(f"""```ansi
POWERED BY @santiagortega

[2;33mSe han generado los b1ns[0m

```""")

    @discord.ui.button(label="💻50", style=discord.ButtonStyle.blurple)
    async def Gen_50(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user

                await self.message.edit(content="""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
            POWERED BY @santiagortega                                   

        [2;33mGenerando b1ns...[0m

        ```""", view=None)
                for _ in range(50):
                 code = random.randint(100000, 999999)
                 url = f"https://data.handyapi.com/bin/{code}"
                 response = requests.get(url)
                 data = response.json()            
                 status = data['Status']
                 if status == 'SUCCESS':
                  await user.send(f"""```ansi
        [2;31m[2;36mVALID: {code}[0m[2;31m[0m
        ```""")
                 elif status == 'NOT FOUND': 
                  await user.send(f"""```ansi
        [2;31mINVALID: {code}[0m
        ```""")
                 else:
                  await user.send(f"""```ansi
        [2;31mERROR: https://discord.com/developers ha denegado la conexion[0m
        ```""")


                channel = bot.get_channel(1246269326676463656)
                if channel:
                    user_id = interaction.user.id
                    embed = discord.Embed(title="`💻`Se han generado b1ns`💻`", description=f"""---------------------------------
        **<:coin:1245137042325770361> B1NS GENERADOS: 50

        <:usuario:1245137045421035611> USUARIO:  <@{user_id}>

        <:dev:1245137043894440049> POWERED BY <@1063538352638394460>**""", color=0x06ebeb)
                    embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
                    embed.set_footer(text="TX G3N")
                    await channel.send(embed=embed)


                await user.send(f"""```ansi
        POWERED BY @santiagortega

        [2;33mSe han generado los b1ns[0m

        ```""")


    @discord.ui.button(label="💻100", style=discord.ButtonStyle.blurple)
    async def Gen_100(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        await self.message.edit(content="""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;33mGenerando b1ns...[0m

```""", view=None)
        for _ in range(100):
                 code = random.randint(100000, 999999)
                 url = f"https://data.handyapi.com/bin/{code}"
                 response = requests.get(url)
                 data = response.json()            
                 status = data['Status']
                 if status == 'SUCCESS':
                  await user.send(f"""```ansi
        [2;31m[2;36mVALID: {code}[0m[2;31m[0m
        ```""")
                 elif status == 'NOT FOUND': 
                  await user.send(f"""```ansi
        [2;31mINVALID: {code}[0m
        ```""")
                 else:
                  await user.send(f"""```ansi
        [2;31mERROR: https://discord.com/developers ha denegado la conexion[0m
        ```""")


        channel = bot.get_channel(1246269326676463656)
        if channel:
                    user_id = interaction.user.id
                    embed = discord.Embed(title="`💻`Se han generado b1ns`💻`", description=f"""---------------------------------
        **<:coin:1245137042325770361> B1NS GENERADOS: 50

        <:usuario:1245137045421035611> USUARIO:  <@{user_id}>

        <:dev:1245137043894440049> POWERED BY <@1063538352638394460>**""", color=0x06ebeb)
                    embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
                    embed.set_footer(text="TX G3N")
                    await channel.send(embed=embed)


        await user.send(f"""```ansi
        POWERED BY @santiagortega

        [2;33mSe han generado los b1ns[0m

        ```""")

class botones_panel(discord.ui.View):
    def __init__(self, inv: str, ctx):
        super().__init__(timeout=None)
        self.inv = inv
        self.ctx = ctx
        

    @discord.ui.button(label="📂Generar", style=discord.ButtonStyle.gray)
    async def generar_MD(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        role_10 = discord.utils.get(user.roles, id=1245891605672493117)
        role_50 = discord.utils.get(user.roles, id=1245891705694064700)
        role_100=discord.utils.get(user.roles, id=1245891736530587693)
        if role_10 is not None:
                    message = await user.send("""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;36mCuantos b1ns quieres generar?[0m
        ```""")
                    view = botones_generar_MD_10(message)
                    await message.edit(view=view)
                    await interaction.response.send_message("`📂`Revisa tu MD\n\n`❌`Si no te llego habilita la funcion para que te lleguen MD de el bot", ephemeral=True)
        elif role_50 is not None:
                    message = await user.send("""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;36mCuantos b1ns quieres generar?[0m
        ```""")
                    view = botones_generar_MD_50(message)
                    await message.edit(view=view)
                    await interaction.response.send_message("`📂`Revisa tu MD\n\n`❌`Si no te llego habilita la funcion para que te lleguen MD de el bot", ephemeral=True)
        
        elif role_100 is not None:
                            message = await user.send("""```ansi
  _______  __    ___________ _   __
 /_  __/ |/ /   / ____/__  // | / /
  / /  |   /   / / __  /_ </  |/ / 
 / /  /   |   / /_/ /___/ / /|  /  
/_/  /_/|_|   \____//____/_/ |_/   
    POWERED BY @santiagortega                                   

[2;36mCuantos b1ns quieres generar?[0m
```""")
                            view = botones_generar_MD_100(message)
                            await message.edit(view=view)
                            await interaction.response.send_message("`📂`Revisa tu MD\n\n`❌`Si no te llego habilita la funcion para que te lleguen MD de el bot", ephemeral=True)
        else:
            embed = discord.Embed(
                title="`❌`No puedes generar",
                description=f"`📂`No tienes los permisos para generar b1ns\n\n`💾`Si quieres comprar o crees que es un error abre ticket",
                color=0x0cf1f1
            )
            embed.set_footer(text="POWERED BY @santiagortega")
            await interaction.response.send_message(embed=embed, ephemeral=True)
                    


@bot.command()
async def b1ns_panel_583958385937204(ctx: commands.Context):
        embed = discord.Embed(
            title="GEN B1NS",
            description=f"**`💳`Generador de B1NS\n\n`🔋`100% GARANTIA DE TENER B1NS VALIDOS\n\n`💾`Mas info @santiagortega\n\n`📂`APLICA: **<#1245884315846311957>",
            color=0x0cf1f1
        )
        embed.set_image(url="https://share.creavite.co/66562b64520faf7ee10a6de2.gif")
        embed.set_footer(text="POWERED BY @santiagortega")
        inv="https://discord.com/invite/onix"  
        await ctx.send(embed=embed, view=botones_panel(inv, ctx))
        
bot.run('AQUI_PONES_EL_TOKEN')
