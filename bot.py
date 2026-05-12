import os
import discord
from keep_alive import keep_alive

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("TOKEN not found! حط التوكن في Environment Variables باسم TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

auto_replies = {
    "مرحبا": "يا اهلا وسهلا 👋",
    "مين عمك": "انت عمي 😎",
    "السلام عليكم": "وعليكم السلام 🌹",
    "هلا": "هلا وغلا 😎",
    "هاي": "هاي 👋",
    "كيفك": "تمام الحمدلله 😁",
    "شو الأخبار": "كلو تمام 🔥",
    "وينك": "موجود 😎",
    "مين انت": "أنا بوت D4rk S0ciety 🤖",
    "باي": "مع السلامة 👋",
    "تصبح على خير": "وانت من أهله 🌙",
    "صباح الخير": "صباح النور ☀️",
    "مساء الخير": "مساء النور 🌙",
    "احبك": "وأنا أحبكم يا أعضاء السيرفر 😎",
    "بوت": "نعم؟ 🤖",
    "سيب": "سييييب 🔥",
    "هههه": "😂",
    "lol": "😂",
    "xd": "🤣",
    "gg": "GG 🔥",
    "wp": "Well Played 👏",
    "ctf": "Cyber Security 🔥",
    "osint": "Open Source Intelligence 👀",
    "web": "Web Exploitation 🌐",
    "crypto": "Cryptography 🔐",
    "forensics": "Digital Forensics 🕵️",
    "reverse": "Reverse Engineering ⚙️",
    "ping": "pong 🏓",
    "شكرا": "العفو 🌹",
    "يسلمو": "حبيب قلبي 😎",
    "مساعدة": "شو بدك أساعدك؟ 👀",
    "وين الفلاق": "دور منيح 😏",
    "flag": "يمكن الفلاق قريب 👀",
    "cyber": "Security Never Sleeps 🔥",
    "discord": "أفضل تطبيق 😎",
    "هاي مين": "أنا البوت تبع D4rk S0ciety 🤖",
    "مين المطور": "سراج 😎",
    "dark": "D4rk S0ciety 🔥",
    "ctftime": "وقت التحديات 😈",
    "hack": "Ethical Hacking Only 😎",
    "hello": "Hello 👋",
    "hi": "Hi 😁",
    "good night": "Good Night 🌙",
    "good morning": "Good Morning ☀️",
    "welcome": "أهلًا وسهلًا 🌹",
    "test": "البوت شغال ✅",
    "admin": "الإدارة موجودة 👀",
    "virus": "احذر من الملفات المشبوهة ☠️",
    "kali": "Kali Linux 🔥",
    "python": "Python رهيبة 😎",
    "linux": "Linux >>> 🔥",
    "windows": "ويندوز جيد برضه 😅",
    "robot": "🤖",
    "sus": "📮",
    "among us": "SUS 😳",
    "help": "كيف بقدر أساعدك؟ 👀",
    "music": "🎵",
    "game": "🎮",
    "valorant": "Headshot 🔥",
    "minecraft": "⛏️",
    "roblox": "Roblox Studio 😎",
    "whoami": "أنت عضو رهيب 😎",
    "bye bye": "نشوفك قريب 👋",
    "brb": "خد راحتك 😁",
    "afk": "لا تطول علينا 👀",
    "noob": "😭",
    "pro": "🔥🔥🔥",
    "wow": "😮",
    "nice": "😎",
    "lets go": "🔥🔥🔥",
    "fire": "🔥",
    "cat": "🐱",
    "dog": "🐶",
    "banana": "🍌",
    "pizza": "🍕",
    "burger": "🍔",
    "water": "💧",
    "coffee": "☕",
    "tea": "🍵",
    "phone": "📱",
    "pc": "🖥️",
    "keyboard": "⌨️",
    "mouse": "🖱️",
    "internet": "🌐",
    "wifi": "📶",
    "server": "🖥️",
    "database": "🗄️",
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

    for trigger, reply in auto_replies.items():
        if content == trigger.lower():
            await message.channel.send(reply)
            break

keep_alive()
client.run(TOKEN)
