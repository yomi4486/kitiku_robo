from PIL import Image,ImageDraw,ImageFont
import discord,os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("BOT_TOKEN")
APPLICATION_ID = os.environ.get("APPLICATION_ID")

client = discord.Client(intents = discord.Intents.all())
def image_process(base_text:str):

    
    if len(base_text) > 30:
        return 1
    if not "\n" in base_text:
        base_text = f"{base_text[:14]}\n{base_text[14:]}"

    img = Image.open('main.jpg')
    font = ImageFont.truetype('LightNovelPOPv2.otf', 40) # フォントは自分で探してクレメンス宇ううううううううううううううううううううううううううううううううううううううううううううううううううううううううはんｒふぃうあｈんうぇるいがんれｗぎうあｒねういんごうあねｈふいあえｒがうんｇヴぃあえるｈんがれ
    draw = ImageDraw.Draw(img)

    #左上の点のx座標, 左上の点のy座標, 右下の点のx座標, 右下の点のy座標
    it = draw.textbbox((431, 230), base_text,align='center')
    i1 = it[0]
    i2 = it[2]

    l = int(i1)+int(i2)
    x = l / 4

    draw.text((431-x, 230), base_text, 'black',font=font,align='center')
    img.save("result.jpg")
    return 0

@client.event
async def on_ready():
    print(f"Ready: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:return
    if f"<@{APPLICATION_ID}>" in message.content:
        text = message.content.replace(f"<@{APPLICATION_ID}> ","").replace(f"<@{APPLICATION_ID}>","").replace("...","…")
        if len(text) == 0:
            await message.reply(content=f"`@mention テキスト`で画像作れるのに...")
            return
        if image_process(base_text=f"{text}") == 0:
            await message.reply(content="",file=discord.File(f'result.jpg'))
        else:
            await message.reply(content="文字数減らせばいいのに...(30文字まで)")
        
client.run(TOKEN)