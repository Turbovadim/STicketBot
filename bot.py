import configparser
import disnake
from disnake.ext import commands
from disnake import TextInputStyle

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг

bot = commands.InteractionBot(test_guilds=[int(config["Auth"]["guild_id"])])

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="на развитие Bisquit.Host"))


@bot.slash_command(
    name="create-button",
    description="Заспавнить кнопку создания тикета.",
)
@commands.has_guild_permissions(administrator=True)
async def buttons(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        title="Создать тикет",
        description="Если у вас возникла проблема или вам нужна помощь. Вы можете создать тикет, для этого нажмите на кнопку ниже. Команда поддержки свяжется с вами и постарается Вам помочь.",
        color=0x46ec12,
    )
    await inter.channel.send(
        components=[disnake.ui.Button(label="Создать тикет", style=disnake.ButtonStyle.success, custom_id="+", emoji="📩")],
        embed=embed
    )
    await inter.send("Кнопка успешно создана.", ephemeral=True)

@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["+", "-"]:
        return
    
    if inter.component.custom_id == "+":
        await inter.response.send_modal(modal=MyModal())

    elif inter.component.custom_id == "-":
        await inter.channel.delete()

class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Тема",
                placeholder="Введите тему тикета",
                custom_id="theme",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Описание проблемы",
                placeholder="Подробно опишите вашу проблему.",
                custom_id="description",
                style=TextInputStyle.paragraph,
            ),
        ]
        super().__init__(title="Создать тикет", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        guild22 = inter.guild
        await inter.response.send_message("Ваш тикет создан.", ephemeral=True)
        techSupport = guild22.get_role(int(config["Roles"]["support"]))
        preTechSupport = guild22.get_role(int(config["Roles"]["sub_support"]))
        overwrites = {
            guild22.default_role: disnake.PermissionOverwrite(view_channel=False),
            inter.author: disnake.PermissionOverwrite(view_channel=True),
            techSupport: disnake.PermissionOverwrite(view_channel=True),
            preTechSupport: disnake.PermissionOverwrite(view_channel=True)
        }
        channel = await inter.channel.category.create_text_channel(name= f"ticket-{inter.author}", overwrites=overwrites)
        embed = disnake.Embed(
            title="Ваш тикет",
            color=disnake.Colour.green(),
        )
        for key, value in inter.text_values.items():
            embed.add_field(
                name=replaceName(key),
                value=value[:1024],
                inline=False,
            )
        await channel.send(embed = embed, components=[
            disnake.ui.Button(label="Закрыть тикет", style=disnake.ButtonStyle.danger, custom_id="-", emoji="🔒"),
        ])        

def replaceName(arg: str):
    if arg == "theme": 
        return "Тема"
    else: 
        return "Описание"


bot.run(config["Auth"]["token"])