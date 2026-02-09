from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


back_values = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад <-", callback_data="back_values")]
])

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="главное меню" , callback_data="main_menu")]
])


#                               0                          1                    2                              3                              4                    5                                           
inline_values = ["🔹 Gracious Professionalism", "🔹 Coopertition", "🔹 Командная работа", "🔹 Инженерное мышление и обучение", "🔹 Вклад в сообщество", "🏁 Заключение"]

ftc_link = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Про ftс" , url="https://www.firstinspires.org/programs/ftc/")],
    [InlineKeyboardButton(text="главное меню" , callback_data="main_menu")]
])

fll_link = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Про fll" , url="https://www.firstinspires.org/programs/fll/")],
    [InlineKeyboardButton(text="главное меню" , callback_data="main_menu")]
])

async def build_values():
    keyboard = InlineKeyboardBuilder()
    for i in range(len(inline_values)):
        keyboard.add(InlineKeyboardButton(text=inline_values[i], callback_data=f'values_{i}'))
    keyboard.add(InlineKeyboardButton(text="главное меню" , callback_data="main_menu"))
    return keyboard.adjust(2).as_markup()

async def create_buttons_with_link(stage):
    if stage == "fll":
        keyboard = InlineKeyboardBuilder()
        keyboard.add(InlineKeyboardButton(text="fll link" , link="https://www.firstinspires.org/programs/fll/"))
        keyboard.add(InlineKeyboardButton(text="главное меню" , callback_data="main_menu"))
    elif stage=="ftc":
        keyboard = InlineKeyboardBuilder()
        keyboard.add(InlineKeyboardButton(text="fts link" , link="https://www.firstinspires.org/programs/ftc/"))
        keyboard.add(InlineKeyboardButton(text="главное меню" , callback_data="main_menu"))
    return keyboard.adjust(2).as_markup()


    
