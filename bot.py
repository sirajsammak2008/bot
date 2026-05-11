import discord

TOKEN = "MTUwMzQ4Mzk3OTkxNzk1MTAyNw.GgRQF5.Ck3NXzRLZLaeNEuknANJNGdBPBXgNI1p3VH5o0"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

auto_replies = {

    "مرحبا": "يا اهلا وسهلا 👋",
    "السلام عليكم": "وعليكم السلام 🌹",
    "هلا": "هلا وغلا 😎",
    "هاي": "هاي 👋",
    "كيفك": "تمام الحمدلله 😁",
    "شو الأخبار": "كلو تمام 🔥",
    "وينك": "موجود 😎",
    "مين انت": "أنا بوت الديسكورد 🤖",
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
    "هاي مين": "أنا البوت تبع السيرفر 🤖",
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
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    content = message.content.strip().lower()

    for trigger, reply in auto_replies.items():

        if content == trigger.lower():
            await message.channel.send(reply)
            break

client.run(TOKEN)