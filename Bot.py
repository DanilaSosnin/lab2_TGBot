import random
import Keyboard
import time
import millionaire
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import StateFilter, Command


true_answer = '-@e■ '
round_millionaire = 1

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

answers = ['A', 'B', 'C', 'D']
balance = 0


def Load_True_Answer(A, B, C, D, answer):
    global true_answer
    temparr = [A, B, C, D]
    for i in range(4):
        if temparr[i] == answer:
            true_answer = answers[i]
            break


def Load_Question():
    (quest, A, B, C, D, answer) = millionaire.loadquests(round_millionaire)
    return quest, A, B, C, D, answer


quest = '0'
A = '0'
B = '0'
C = '0'
D = '0'
answer = '0'


@dp.message(Command("start"), StateFilter(None))
async def start(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}.", reply_markup=Keyboard.main_kb)


@dp.message()
async def echo(message: Message):
    global quest, A, B, C, D, answer
    global round_millionaire
    msg = message.text.lower()

    #ИГРА В КОСТИ
    if msg == 'давай поиграем в кости':
        await bot.send_message(message.from_user.id, "На твоём кубике выпало: ")
        user_data = await bot.send_dice(message.from_user.id)
        user_data = user_data.dice.value

        time.sleep(1)
        await bot.send_message(message.from_user.id, "На моём кубике выпало: ")
        bot_data = await bot.send_dice(message.from_user.id)
        bot_data = bot_data.dice.value

        time.sleep(5)
        if bot_data > user_data:
            await bot.send_message(message.from_user.id, "Я победил!")
        elif bot_data < user_data:
            await bot.send_message(message.from_user.id, "Поздравляю, твоя победа!")
        else:
            await bot.send_message(message.from_user.id, "Ничья!")

    #ВЕРНУТЬСЯ В МЕНЮ
    elif msg == 'назад':
        await message.answer(f"Что ты хочешь, {message.from_user.first_name}?", reply_markup=Keyboard.main_kb)

    #МОТИВАТОР
    elif msg == 'мне не хватает мотивации':
        f = open("images.txt", "r")
        lines = 0
        for line in f:
            lines += 1
        f.close()
        random_image = random.randint(0, lines)
        f = open("images.txt", "r")
        current_line = 0
        for i in f:
            if random_image == current_line:
                await bot.send_photo(message.from_user.id, i)
                break
            current_line += 1
        f.close()

    elif msg == "что ты умеешь?":
        await message.answer(open("info.txt", 'r').read())

    #МИЛЛИОНЕР
    elif msg == "кто хочет стать миллионером?":
        round_millionaire = 0
        (quest, A, B, C, D, answer) = Load_Question()
        await message.answer(quest + "\nA. " + A + "\nB. " + B + "\nC. " + C + "\nD. " + D, reply_markup=Keyboard.millionaire_kb)
        Load_True_Answer(A, B, C, D, answer)

    elif msg.upper() in answers:
        global true_answer
        global balance
        current_answer = answer
        if true_answer == message.text.upper():
            round_millionaire += 1
            if round_millionaire < 5:           #ЕСЛИ ИГРА НЕ ОКОНЧЕНА
                (quest, A, B, C, D, answer) = Load_Question()
                balance = balance + round_millionaire * 1000 + (round_millionaire - 1) * 1000
                await message.answer("Правильно. Вы проходите в следующий этап. \nВаш баланс: " + str(balance))
                await message.answer(quest + "\nA. " + A + "\nB. " + B + "\nC. " + C + "\nD. " + D, reply_markup=Keyboard.millionaire_kb)
                Load_True_Answer(A, B, C, D, answer)
            else:
                balance = balance + round_millionaire * 1000 + (round_millionaire - 1) * 1000
                await message.answer("Правильно. Поздравляю, Вы выиграли " + str(balance) + "!", reply_markup=Keyboard.main_kb)
                round_millionaire = 1
                balance = 0
        else:
            await message.answer("Увы, это неправильно. Правильный ответ - " + current_answer + ". Вы выбываете. \nВаш баланс: " + str(balance), reply_markup=Keyboard.main_kb)
            round_millionaire = 1
            balance = 0

    else:
        await message.answer(f"{message.from_user.first_name}, я не понимаю что ты от меня хочешь", reply_markup=Keyboard.main_kb)
        round_millionaire = 1
        balance = 0


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)