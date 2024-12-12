from keyboards.genre_keyboards import create_genre_keyboard

async def handle_genre_menu(query, genre_list):
    # Extract the requested page number
    if query.data.startswith("page_"):
        page = int(query.data.split("_")[1])
    else:
        page = 0

    # Generate the keyboard for the requested page
    reply_markup = create_genre_keyboard(genre_list, page=page)

    # Update the message with the new keyboard
    await query.message.edit_text("Select Genre, Chimp:", reply_markup=reply_markup)
