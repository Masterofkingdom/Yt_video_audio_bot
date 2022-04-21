from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"This is **kingdom family product** now send a you tube url and Select the category you want"
    await message.reply_text(helptxt)
