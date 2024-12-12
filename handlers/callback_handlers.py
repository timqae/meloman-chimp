import asyncio
from pprint import pprint


from resourses.stickers_ids import (
    THINKING_MONKEY,
    GOODBYE_MONKEY,
    COOL_GLASS_MONKEY,
)

from handlers import genre_menu_handlers
from keyboards.genre_keyboards import genre
from discogs_services.search import Search
from discogs_services.api_client import ApiClient

from telegram import CallbackQuery, Update
from telegram.ext import ContextTypes


client = ApiClient()
search = Search(client)


callback_data_storage = {}


async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_name = update.effective_user.first_name
    chat_id = query.message.chat_id
    callback_data = query.data  # Store the callback data

    # pprint(f"query from: {user_name}")
    # pprint(callback_data_storage.get(chat_id))

    # meloman
    if callback_data == "meloman":
        reply_sticker_msg = await query.message.reply_sticker(COOL_GLASS_MONKEY)
        await asyncio.sleep(3)
        await reply_sticker_msg.delete()

        await genre_menu_handlers.handle_genre_menu(query, genre)

    elif callback_data in genre:  # Handle specific genre selections
        good_choise_msg = await query.message.edit_text(
            f"looking for {query.data}"
        )
        # await asyncio.sleep(3)
        await good_choise_msg.delete()

        thinking_monkey_sticker = await query.message.reply_sticker(THINKING_MONKEY)

        pprint(f"[genre query from -> ] : {user_name}")

        if chat_id not in callback_data_storage:
            callback_data_storage[chat_id] = {}
        callback_data_storage[chat_id]["genre"] = callback_data

        await asyncio.sleep(4)
        await thinking_monkey_sticker.delete()

        genre_pair = callback_data_storage[chat_id]

        reply_msg = search.random_album_choise(genre_pair)

        await query.message.reply_text(reply_msg)
        await asyncio.sleep(2)

        reply_text_msg = await query.message.reply_text("See ya!.")
        reply_sticker_msg = await query.message.reply_sticker(GOODBYE_MONKEY)

        await asyncio.sleep(3)
        await reply_text_msg.delete()
        await reply_sticker_msg.delete()

    elif callback_data.startswith("page_"):  # Handle pagination for genres
        await genre_menu_handlers.handle_genre_menu(query, genre)

    # bye
    elif callback_data == "goodbye":
        reply_text_msg = await query.message.reply_text("Bye, Looser.")
        reply_sticker_msg = await query.message.reply_sticker(GOODBYE_MONKEY)

        await asyncio.sleep(2)
        await reply_text_msg.delete()
        await reply_sticker_msg.delete()
