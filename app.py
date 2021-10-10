import streamlit as st
import German
import AncientRus
import Interlacer

'''
# Задание 1. Немецкие цифры.
**Описание задачи**: по введенному числу на *немецком* языке записать его с помощью *арабских* цифр и затем представить его *старорусскими* цифрами (а-1 в-2 и-8 л-30 р-100 ф-500)
'''

name = st.text_input("Введите число немецкими словами")

if not name:
    st.warning("необходимо ввести число")
else:
    try:
        st.warning("Немецкий: " + name.replace(" ",""))
        st.warning("Арабский: " + str(German.convert(name)))
        st.warning("Древнерусский: "+ AncientRus.convert(German.convert(name)))
    except Exception as e:
        st.warning(e)

'''
Работу выполнил Кривко Иван БИСО-03-19
'''

'''
# Задание 2. Тасовка строк друг в друга.
**Описание задачи**: По 2 введённым строкам сформировать новую путём тасовки слов друг в друга, начиная с конца
'''

str1 = st.text_input("Первая строка")
str2 = st.text_input("Вторая строка")

if not str1 or not str2:
    st.warning("необходимо ввести обе строки")
else:
    st.warning(Interlacer.reverse_interlace(str1,str2))


'''
Работу выполнил Кривко Иван БИСО-03-19
'''