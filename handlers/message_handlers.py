import random
import asyncio
from pprint import pprint

from resourses.stickers_ids import CONFUSED_MONKEYS, KID_AND_MONKEY

from handlers import genre_menu_handlers, start_handlers

from telegram import Update
from telegram.ext import ContextTypes


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text.lower().strip()
    user_name = update.effective_user.first_name

    if user_msg == "start":
        # Send the sticker and message
        pprint(f"[START ->] {user_name}")
        reply_msg = await update.message.reply_sticker(KID_AND_MONKEY)
        await asyncio.sleep(1)  # Wait for 1 second

        # Send the "What’s up, chimp?" message and handle the start
        reply_text_msg = await update.message.reply_text(f"What’s up, chimp?")
        await start_handlers.handle_start(update, context)

        # After a timeout (e.g., 5 seconds), delete both the sticker and text messages
        await asyncio.sleep(3)  # Adjust the timeout as needed
        await reply_msg.delete()  # Delete the sticker
        await reply_text_msg.delete()  # Delete the text message

    else:
        random_sticker = random.choice(CONFUSED_MONKEYS)
        # Send the message and sticker about the wrong input
        reply_sticker_msg = await update.message.reply_sticker(random_sticker)
        reply_text_msg = await update.message.reply_text(
            f'Do not mess with Chimp, {user_name.capitalize()}. Let\'s "start"'
        )

        # After a timeout (e.g., 5 seconds), delete both the message and sticker
        await asyncio.sleep(5)  # Adjust the timeout as needed
        await reply_text_msg.delete()  # Delete the text message
        await reply_sticker_msg.delete()  # Delete the sticker
