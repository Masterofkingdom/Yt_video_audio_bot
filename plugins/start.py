from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡ Our Channel ⚡", url="https://t.me/kingdom_family_chanel"),
         InlineKeyboardButton("⚡ Our Group ⚡", url="https://t.me/kingdom_family")],
        [InlineKeyboardButton("⚡ Share Channel ⚡", url="https://telegram.me/share/url?url=t.me/kingdom_family_chanel")],
        [InlineKeyboardButton("⚡ Share Group ⚡", url="https://telegram.me/share/url?url=t.me/kingdom_family")],
        [InlineKeyboardButton("⚡ kathasayura ⚡", url="https://t.me/kathasayura"),
         InlineKeyboardButton("⚡ stickers ⚡", url="https://t.me/kingdom_family_sticker")],
    ])
    welcomed = f"Hi 👋 <b>{message.from_user.first_name}</b>\nThis is **kingdo family product** This bot can download You tube video and audio \nhelp For more \n\n\n 𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 :- @kingdom_family_chanel"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
