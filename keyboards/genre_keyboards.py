from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# https://support.discogs.com/hc/en-us/articles/360005055213-Database-Guidelines-9-Genres-Styles#genres
genre = [
    "Blues",
    "Brass & Military",
    "Childrens",
    "Classical",
    "Electronic",
    "Folk, World, & Country",
    "Funk / Soul",
    "Hip-Hop",
    "Jazz",
    "Latin",
    "Non-Music",
    "Pop",
    "Reggae",
    "Rock",
    "Stage & Screen",
]

# Function to create the inline keyboard from the genre list
def create_genre_keyboard(genre_list, page=0, items_per_page=5):
    """Generates a paginated inline keyboard for genres."""
    start = page * items_per_page
    end = start + items_per_page
    current_page_genres = genre_list[start:end]

    # Create buttons for the current page
    keyboard = [[InlineKeyboardButton(genre, callback_data=genre)] for genre in current_page_genres]

    # Add navigation buttons if necessary
    navigation_buttons = []
    if start > 0:  # Add 'Previous' button if not on the first page
        navigation_buttons.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"page_{page - 1}"))
    if end < len(genre_list):  # Add 'Next' button if not on the last page
        navigation_buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"page_{page + 1}"))
    if navigation_buttons:
        keyboard.append(navigation_buttons)

    return InlineKeyboardMarkup(keyboard)
