# sticked "file_id" from the @RawDataBot
CONFUSED_MONKEY_1 = (
    "CAACAgIAAxkBAAEvuF9nTZT0MTWM6NqkfkE8UdXChsekagACnS0AArg1SUk4l-5erVNphzYE"
)
CONFUSED_MONKEY_2 = (
    "CAACAgIAAxkBAAEvuGtnTZe3nKHIIHBtNGJnsVi3aIT0JwACNzMAAhfFaUpLGMciRIeyWzYE"
)
CONFUSED_MONKEY_3 = (
    "CAACAgIAAxkBAAEvuG1nTZf45pmH5fcG4a9_92KzCRv6egACGyIAAkVMSUmXt8Y5yAscFjYE"
)
CONFUSED_MONKEY_4 = (
    "CAACAgIAAxkBAAEvuG9nTZg_YOrfo_YX8bhs8rZmah2cpQAClkcAA1A4SAlcXQLaSM09NgQ"
)

WINTER_MONKEY = (
    "CAACAgIAAxkBAAEvuH1nTZ1rrcq_VszTu0ge98pWTsc3gAACpyQAAkPDsErP2vyUbzLA5DYE"
)

MOBILE_MONKEY = (
    "CAACAgIAAxkBAAEvuI1nTaAFoD0YcYzWRpT1aL6Z0AABQ3oAAncdAAIFQbFKbRNwJX7Ixig2BA"
)

KID_AND_MONKEY = (
    "CAACAgIAAxkBAAEvuJVnTaDOEnSlg4JyN-Tr380JiHedigACSUIAAo8R8UtIMNuT61zgyTYE"
)

CONFUSED_MONKEYS = [
    CONFUSED_MONKEY_1,
    CONFUSED_MONKEY_2,
    CONFUSED_MONKEY_3,
    CONFUSED_MONKEY_4,
]

GOODBYE_MONKEY = "CAACAgIAAxkBAAEvu49nTixtKMgC_VN_8Q-ayNNH5ujdnAACq0cAAgk1UUkSMT1ctN1TnDYE"

COOL_GLASS_MONKEY = "CAACAgIAAxkBAAEvu5NnTi0yY0tC97aTwjMK_QQZtA7zEgACQCIAAnq2YEur-eo2cza__jYE"

THINKING_MONKEY = "CAACAgIAAxkBAAEvwIRnT3vntx9LzT4I3HzFf0cB0XDtkwACSUcAAtlEOEjxI-nz37rbETYE"

# Responses
RESPONSES = {
    "hello": {"messages": ["Hello", 'type "weather"'], "stickers": ["KID_AND_MONKEY"]},
    "weather": {
        "messages": ["wait, I'm checking .....", "{name}, frosty"],
        "stickers": [MOBILE_MONKEY, WINTER_MONKEY],
    },
    "default": {"messages": ["{name}, Say, Hello"], "stickers": CONFUSED_MONKEYS},
}
