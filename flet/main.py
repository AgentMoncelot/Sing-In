#import
import streamlit as st
import pandas as pd
import numpy as np

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






#st.form_submit_button('Войти')

#Button
if error == False:
    with st.empty():
        st.button('**Регистрация**', key='login')
else:

    st.warning(ss, icon='⚠')

button = st.button('**Войти**')



#st.link_button('Войти', url="#")







