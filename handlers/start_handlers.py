from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from keyboards.genre_keyboards import create_genre_keyboard


# The handler for the /start command
async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create the keyboard layout with two buttons
    keyboard = [
        [
            InlineKeyboardButton("Meloman Chimp", callback_data="meloman"),
            InlineKeyboardButton("No Banana, No Chimp!", callback_data="goodbye"),
        ],
    ]

    # Define the reply markup for inline keyboard
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the welcome message with the inline keyboard
    await update.message.reply_text(
        "Got some Banana Vibe? 🍌🎶", reply_markup=reply_markup
    )
