from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=26484720,
    api_hash="fe77fbf0cae9f7f5ece37659e2466cf1",
    bot_token="6305475220:AAEK9B4q8y-zDIUn4hCrpp5a-l6C-JLt7jY",#توكن المصنع
    plugins=dict(root="Mody")
    )

DEVS = ["UP_UO"] 


async def start_ahmedbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
