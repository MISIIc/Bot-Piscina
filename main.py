import discord
from discord.ext import commands
from imageai.Detection import ObjectDetection

def get_class(model_path, image_path):

    detector = ObjectDetection()
    model_path = "yolov3.pt"
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()

    detections = detector.detectObjectsFromImage(
        input_image=image_path,
        output_image_path="risultato.jpg",
        minimum_percentage_probability=30)
    return len(detections)

pass


# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Abbiamo fatto l'accesso come {bot.user}")


@bot.command()
async def save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            fileurl = attachment.url
            print(filename)
            print(fileurl)
            await attachment.save(f"./{filename}")
            #await ctx.send(f"L'immagine è stata salvata in {fileurl}
            await ctx.send(get_class(model_path="yolov3", image_path=filename))
    else:
        ctx.send("Hai dimenticato la fotografia")



bot.run("TOKEN")