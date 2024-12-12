def format_album_message(title, genre, style, country, year, url):
    # Fallbacks for missing values
    genre = ", ".join(genre) if genre else "Unknown"
    style = ", ".join(style) if style else "Unknown"
    country = country or "Unknown"
    year = year or "Unknown"

    # Encode the title for the YouTube search URL
    youtube_query = "+".join(title.split())
    youtube_url = f"https://www.youtube.com/results?search_query={youtube_query}"

    # Construct the message
    message = (
        f"🎵 < Album Recommendation > 🎵\n\n"
        f"💽 > {title}\n\n"
        f"🎼 > {genre}\n\n"
        f"🎹 > {style}\n\n"
        f"🌍 > {country}\n\n"
        f"📅 > {year}\n\n\""
        f"🔗 [Check it out on Discogs]\n({url})\n\n"
        f"🔍 [Search on YouTube]\n{youtube_url}"
    )
    return message