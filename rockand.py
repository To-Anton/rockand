import run_bot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import batton as kb
import random

bot = Bot(token=run_bot.TOKEN)
dp: Dispatcher = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привіт! 👋", reply_markup=kb.greet_kb)


@dp.message_handler(commands=['help'])
async def menu1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Давай допоможу. Обери один з варіантів', reply_markup=kb.greet_kb3)


@dp.message_handler(text=["✊", "✌", "✋"])
async def process_start1(message: types.Message):
    rand = ["✊", "✌", "✋"]
    rand = random.choice(rand)
    await bot.send_message(message.from_user.id, str(random.choice(rand)))
    if message.text == '✊' and rand == '✊':
        await bot.send_message(message.from_user.id, 'Нічія! Ще?')
    elif message.text == '✊' and rand == '✌':
        await bot.send_message(message.from_user.id, 'Перемога! 👏')
    elif message.text == '✊' and rand == '✋':
        await bot.send_message(message.from_user.id, 'Поразка! 😲')
    else:
        if message.text == '✌' and rand == '✊':
            await bot.send_message(message.from_user.id, 'Програш! Ще?')
        elif message.text == '✌' and rand == '✌':
            await bot.send_message(message.from_user.id, 'Нічія! 😳')
        elif message.text == '✌' and rand == '✋':
            await bot.send_message(message.from_user.id, 'Перемога! Вітаю!')
        else:
            if message.text == '✋' and rand == '✊':
                await bot.send_message(message.from_user.id, 'Перемога! 💙💛')

            elif message.text == '✋' and rand == '✌':
                await bot.send_message(message.from_user.id, 'Програш! Відіграєшся?')
            elif message.text == '✋' and rand == '✋':
                await bot.send_message(message.from_user.id, 'Нічия, давай ще!')


@dp.message_handler()
async def menu(message: types.Message):
    if message.text == '✊✌✋':
        await bot.send_message(message.from_user.id, 'Да почнеться битва', reply_markup=kb.greet_kb2)  # тут додати саму
    elif message.text == '🎲 Рандомні операції':
        await bot.send_message(message.from_user.id, 'Обирай ось тобі 🗝', reply_markup=kb.greet_kb_20)
    elif message.text == 'Від 0 до 100':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(0, 100)))
    elif message.text == 'Від 0 до 1000':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(0, 1000)))
    elif message.text == 'Гральний кубик 🎲':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(1, 6)))
    elif message.text == 'Гральні кубики 🎲🎲':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(1, 12)))
    elif message.text == '⬅ Нaзад':
        await bot.send_message(message.from_user.id, 'Хто шукає, той завжди 🦝', reply_markup=kb.greet_kb1)
    elif message.text == 'Привіт! 👋':
        await bot.send_message(message.from_user.id, '👋', reply_markup=kb.greet_kb1)
    elif message.text == 'Як грати в цу-є-фа?':
        await bot.send_message(message.chat.id, "Лови силку на правила гри: "
                                                "https://uk.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BC%D1%96%D0%BD%D1%8C-%D0%BD%D0%BE%D0%B6%D0%B8%D1%86%D1%96-%D0%BF%D0%B0%D0%BF%D1%96%D1%80",
                               reply_markup=kb.greet_kb_2)
    elif message.text == '💯 допомога':
        await bot.send_message(message.from_user.id, 'Давай допоможу. Обери один з варіантів',
                               reply_markup=kb.greet_kb3)
    elif message.text == 'Ні' or message.text == 'ні':
        await bot.send_message(message.from_user.id, 'Шкода')
    elif message.text == '😱 Що ти таке?':
        await bot.send_message(message.from_user.id,
                               'Отакої.\nЯ бот, який кидає тобі виклик в «камень, ножниці, папір», '
                               '(«чі-чі-ко», «раз-два три» чи «цу-є-фа») і я буду '
                               'достойним супротивником, можеш перевірити 😝.\nТакож я можу '
                               'видавати рандомні числа з 0 до 100 або до 1000.Ще можу допомогти тобі '
                               'якщо в тебе немає кубика.\nПотестуй '
                               'мене. Може я '
                               'щось додам ще, та я погано вчуся але добре граю 😏', reply_markup=kb.greet_kb_2)
    elif message.text == '⬅ Назад':
        await bot.send_message(message.from_user.id, 'Що ти обереш, кексику?', reply_markup=kb.greet_kb1)
    elif message.text == 'А що таке рандом?':
        await bot.send_message(message.chat.id, 'Ось тобі статейка з Вікіпедії: '
                                                'https://uk.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_%D0%BF%D1%81%D0%B5%D0%B2%D0%B4%D0%BE%D0%B2%D0%B8%D0%BF%D0%B0%D0%B4%D0%BA%D0%BE%D0%B2%D0%B8%D1%85_%D1%87%D0%B8%D1%81%D0%B5%D0%BB',
                               reply_markup=kb.greet_kb_2)
    elif message.text == 'Привіт' or message.text == 'привіт' or message.text == 'Так' or message.text == \
            'так':  # прибери з великої букви
        await bot.send_message(message.from_user.id, 'Радий тобі! Сподіваюсь бути тобі корисним.')
    elif message.text == 'привет' or message.text == 'Привет' or message.text == 'Здорова' or message.text == 'Hi' or \
            message.text == 'hi' or message.text == 'Ку':
        await bot.send_message(message.from_user.id,
                               'Ти вже вибач, але я знаю леше українську мову, щелепа не так розташована'
                               'і усілякі подібні штуки, тому прошу пиши українською.')
    elif message.text == 'Хорошо' or message.text == 'ok' or message.text == 'Дяк' or message.text == 'дяк' or \
            message.text == 'Дякую' or message.text == 'дякую' or message.text == 'Гаразд' or \
            message.text == 'Добре' or message.text == 'гаразд' or \
            message.text == 'ок' or message.text == 'Звичайно' or \
            message.text == 'хорошо' or \
            message.text == 'Ок':
        await bot.send_message(message.from_user.id, 'Тоді тисни на вбудовану клавіатуру, це буде зручніше. 😜')
    elif message.text == 'Сука' or message.text == 'сука' or message.text == 'хуй' or message.text == 'Хуй' or \
            message.text == 'Нихуя' or message.text == 'нихуя' or message.text == 'Бля' or message.text == 'бля' or \
            message.text == 'Похуй' or message.text == 'похуй' or message.text == 'пахую' or message.text == \
            'нахуй' or message.text == 'Иди на хуй' or message.text == 'иди нахуй' or message.text == 'иди на хуй!' or \
            message.text == 'ХУЙ' or message.text == 'пидор' or message.text == 'Пидор' or message.text == 'пидарас' or \
            message.text == 'Пидарас' or message.text == 'Пизда' or message.text == 'пизда':
        await message.delete()
        await bot.send_message(message.from_user.id, 'Бувай-бувай,засранцю 🐓')
    elif message.text == 'Нет' or message.text == 'нет' or message.text == 'не' or message.text == 'Не':
        await bot.send_message(message.from_user.id, 'Тоді в нас нічого не вийде 💔')
    elif message.text == '👋':
        await bot.send_message(message.from_user.id, 'Хаааай, тисни на вбудовані кнопки, нам обом це буде легше 😌')
    elif message.text == 'Слава Україні!' or message.text == 'Слава Україні' or message.text == 'слава Україні' or \
            message.text == 'слава Україні':
        await bot.send_message(message.from_user.id, 'Героям Слава! 🇺🇦')
    elif message.text == 'Украина' or message.text == 'Україна':
        await bot.send_message(message.from_user.id, 'Понад усе!')
    elif message.text == 'Лох' or message.text == 'лох':
        await bot.send_message(message.from_user.id, 'В твоєму віддзеркаленні!')
    else:
        if message.text == '⬅ Hазад':
            await bot.send_message(message.from_user.id, 'Що ти обереш, шукачу?', reply_markup=kb.greet_kb3)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
