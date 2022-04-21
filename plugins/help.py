from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"This is **kingdom family product** now send send a you tube url and select the catagori of you want"
    await message.reply_text(helptxt)
