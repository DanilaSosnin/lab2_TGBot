from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text="Мне не хватает мотивации")
        ],
        [
            KeyboardButton(text="Давай поиграем в кости")
        ],
        [
            KeyboardButton(text="Кто хочет стать миллионером?")
        ],
        [
            KeyboardButton(text="Что ты умеешь?")
        ]
    ],
    resize_keyboard=True,
    #one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

millionaire_kb = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text="A"),
            KeyboardButton(text="B"),
            KeyboardButton(text="C"),
            KeyboardButton(text="D")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)



