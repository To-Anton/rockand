from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

kb = KeyboardButton
button_hi = KeyboardButton('Привіт! 👋')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

# play.insert()


button4 = KeyboardButton('🎲 Рандомні операції', callback_data='a4')
button5 = KeyboardButton('✊✌✋', callback_data='a5')
button6 = KeyboardButton('💯 допомога', callback_data='a6')  # допомога
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button4, button5, button6)
button7 = KeyboardButton('⬅ Назад', callback_data='a6')
greet_kb_back = ReplyKeyboardMarkup(resize_keyboard=True).add(button7)
button8 = KeyboardButton('А що таке рандом?', callback_data='a7')
button9 = KeyboardButton('Як грати в цу-є-фа?', callback_data='a8')
button10 = KeyboardButton('😱 Що ти таке?', callback_data='a7')
greet_kb3 = ReplyKeyboardMarkup(resize_keyboard=True).add(button7, button8, button9, button10)
button12 = KeyboardButton('https://uk.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BC%D1%96%D0%BD%D1%8C-%D0%BD%D0%BE%D0%B6%D0%B8\
                                                                                              %D1%86%D1%96-%D0%BF%D0%B0%D0%BF%D1%96%D1%80#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0_%D0%B3%D1%80%D0%B8',
                          callback_data='a19')
greet_kb4 = ReplyKeyboardMarkup(resize_keyboard=True).add(button12)

button13 = KeyboardButton(text='Вікісилка',
                          url='https://uk.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_%D0%BF%D1%81%D0%B5%D0%B2%D0%B4%D0%BE%D0%B2%D0%B8%D0%BF%D0%B0%D0%B4%D0%BA%D0%BE%D0%B2%D0%B8%D1%85_%D1%87%D0%B8%D1%81%D0%B5%D0%BB',
                          callback_data='a18')

greet_kb5 = ReplyKeyboardMarkup(resize_keyboard=True).add(button13)

button1 = KeyboardButton('✊', callback_data='a1')  # камінь
button2 = KeyboardButton('✌', callback_data='a2')  # ножиці
button3 = KeyboardButton('✋', callback_data='a3')  # папір
button14 = KeyboardButton('📊 Рахунок', callback_data='b9')

greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2, button3, button7)  # ,button14) рахунок
button_back = KeyboardButton('⬅ Hазад', callback_data='b1')
greet_kb_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)

button20 = KeyboardButton('Від 0 до 100', callback_data='a1')
button21 = KeyboardButton('Від 0 до 1000', callback_data='a1')
button22 = KeyboardButton('Гральний кубик 🎲', calback_data='a1')
button24 = KeyboardButton('Гральні кубики 🎲🎲', calback_data='a1')
button23 = KeyboardButton('⬅ Нaзад', calback_data='a1')
greet_kb_20 = ReplyKeyboardMarkup(resize_keyboard=True).add(button23, button20, button21, button22, button24)
