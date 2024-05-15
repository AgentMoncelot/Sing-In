#import
import streamlit as st

asd = False
reemail = [

    '$',
    '%',
    '#',
    '*',
    '^',
    '(',
    ')'
    '!',
    '{',
    '}',
    ']',
    '[',
    '<',
    '>'
    '?',
    "'",
    '"',
    '=',
    '+',
    '|',
    '/',
    '^',
    '№',
    ';',
    '~',
    '?',
    ',',
    ':',
]
repass = [

    '$',
    '%',
    '#',
    '*',
    '^',
    '(',
    ')'
    '!',
    '{',
    '}',
    ']',
    '[',
    '<',
    '>'
    '?',
    "'",
    '"',
    '=',
    '+',
    '|',
    '/',
    '^',
    '№',
    ';',
    '~',
    '?',
    ',',
    ':',
    '@'
]

null_input = False


error = False
st.title("Регистрация")
#Name
Name = st.text_input('Введите ваше **Имя**', placeholder='Name')
for i in repass:
    if str(i) in Name:
        with st.empty():
            error = True
            ss = "Пожалуйста, убедитесь, что в поле 'Имя' не используются запрещенные символы."


#Email
email = st.text_input('Введите **Почту**', placeholder='Email')
for i in reemail:
    if str(i) in email:
        with st.empty():
            error = True
            ss = "Пожалуйста, убедитесь, что в поле 'Пароль' не используются запрещенные символы."

    if '@' not in email and len(email) > 2:
        error = True
        ss = 'Пожалуйста, проверьте правильность написания адреса электронной почты, так как символ @ отсутствует.'
    if len(email) > 30 or (len(email) < 3 and len(email) > 1):
        error = True
        ss = "Пожалуйста, убедитесь, что в поле 'Почта' содержится от 3 до 30 символов."




#Password
password = st.text_input('Введите **Пароль**', placeholder='Password', type='password')
for i in repass:
    if str(i) in password:


        error = True
        ss = "Пожалуйста, убедитесь, что в поле 'Пароль' не используются запрещенные символы."

    if len(password) > 30 or (len(password) < 3 and len(password) > 1):
        error = True
        ss = "Пожалуйста, убедитесь, что в поле 'Пароль' содержится от 3 до 30 символов."



if len(password) < 1 and len(Name) < 1 and len(email) < 1:



    null_input = True

#st.form_submit_button('Войти')

#Button



if error == False:
    with st.empty():

        reg = st.button('**Регистрация**', key='login')
        if reg:
            st.warning("Пожалуйста, убедитесь, что все поля заполнены корректно.", icon='⚠')



else:
    st.warning(ss, icon='⚠')
    if null_input == True:

        asd = True



button = st.link_button('**Регистрация**', url="log.py")
if button:
    st.markdown("<script>window.close();</script>", unsafe_allow_html=True)




#st.link_button('Войти', url="#")




button = st.link_button('**Войти**', url="https://mysitelogi.streamlit.app/")
from telebot import types
import telebot
streamlit.write('hello')
user1 = 0

bot = telebot.TeleBot('7066747596:AAGQUM5hCjfxvKs5SE2fPwfuzQjA6n7bJBU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, 'https://bytepix.ru/ib/Op7aJZSqyR.png')
    bot.send_message(message.chat.id,
                     'Приветствуем вас в нашем игровом клубе, в данном боте вы можете оставить заявку на бронирование коппьютеров, или ознакомится с нашими тарифами.')
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Продолжить', callback_data='yes')
    markup_inline.add(item_yes)
    bot.send_message(message.chat.id, 'Нажимая продолжить вы принимаете условия пользования',
                     reply_markup=markup_inline)

    bot.register_message_handler(message, callback_message)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):



    if callback.data == 'U':
            markup_inline = types.InlineKeyboardMarkup()
            sum1 = types.InlineKeyboardButton(text='100', callback_data='pay100')
            sum3 = types.InlineKeyboardButton(text='300', callback_data='pay300')
            sum2 = types.InlineKeyboardButton(text='500', callback_data='pay500')
            lock = types.InlineKeyboardButton(text='Отмена', callback_data='No')
            markup_inline.add(lock, sum1, sum3, sum2)
            bot.edit_message_text('Пополнить счет 💳\n Для пополнения боланса нажмите на кнопку с суммой для оплаты',callback.message.chat.id, callback.message.message_id,  reply_markup=markup_inline)
            print(callback.data)

    if callback.data == "No":
        def menus(callback):
            markup_inline = types.InlineKeyboardMarkup()
            item_1 = types.InlineKeyboardButton(text='Пополнить счет 💳', callback_data='U')
            item_2 = types.InlineKeyboardButton(text='Показать боланс 💰', callback_data='S')
            item_3 = types.InlineKeyboardButton(text='Оплатить игру 🚀', callback_data='P')
            markup_inline.add(item_3)
            markup_inline.add(item_1, item_2)
            bot.send_message(callback.message.chat.id, 'Menu', reply_markup=markup_inline)
        menus(callback)


    if callback.data == 'yes':
            print(callback.data)
            bot.edit_message_text('Добро пожаловать' + " " + callback.from_user.first_name + '\n Для выхода в главное меню напишите /menu',callback.message.chat.id, callback.message.message_id)
            bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
            bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)



@bot.message_handler(commands=['menu'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_1 = types.InlineKeyboardButton(text='Пополнить счет 💳', callback_data='U')
    item_2 = types.InlineKeyboardButton(text='Показать боланс 💰', callback_data='S')
    item_3 = types.InlineKeyboardButton(text='Оплатить игру 🚀', callback_data='P')

    markup_inline.add(item_3)
    markup_inline.add(item_1, item_2)
    bot.send_message(message.chat.id, 'Menu', reply_markup=markup_inline)
    bot.register_message_handler(message, callback_message)



bot.polling(none_stop=True)

