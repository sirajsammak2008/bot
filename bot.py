import os
import discord
from keep_alive import keep_alive
from google import genai

TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if TOKEN is None:
    raise ValueError("TOKEN not found! حط التوكن في Environment Variables باسم TOKEN")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found! حط مفتاح Gemini في Environment Variables")

gemini = genai.Client(api_key=GEMINI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

auto_replies = {
 "ping": "pong 🏓",
"dark": "D4rk S0ciety 🔥",
"مين المطور": "سراج 😎",
    "GR4NTME4WISH!": "kwwsv://zzz.lqvwdjudp.frp/t_242h/"
}

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.strip().lower()

    if content.startswith("!ai "):
        question = message.content[4:].strip()

        if not question:
            await message.channel.send("اكتب سؤالك بعد الأمر `!ai`")
            return

        async with message.channel.typing():
            try:
                response = gemini.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=question
                )

                answer = response.text

                if len(answer) > 1900:
                    answer = answer[:1900] + "\n\n...الرد طويل، اختصرته."

                await message.channel.send(answer)

            except Exception as e:
                await message.channel.send(f"صار خطأ بالذكاء الاصطناعي: `{e}`")

        return

    for trigger, reply in auto_replies.items():
        if content == trigger.lower():
            await message.channel.send(reply)
            break

keep_alive()
client.run(TOKEN)
