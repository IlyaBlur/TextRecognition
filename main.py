# Устанавливаем библиотеки
import easyocr
from PIL import ImageDraw,Image
#from io import StringIO
import streamlit as st


# ---------------------Header---------------------

st.markdown('''<h2  >Распознавание текста на изображениях</h2>''',

            unsafe_allow_html=True)

img_ocr = Image.open("123.PNG")  #Функция для открытия картинки


st.image(img_ocr, use_column_width='auto')

# ---------------------Choosing language---------------------

languages = ['ar', 'az', 'be', 'bg', 'ch_tra', 'che', 'cs', 'de', 'en', 'es', 'fr', 'hi', 'hu', 'it', 'ja', 'la', 'pl',
            'ru', 'tr', 'uk', 'vi'] # Выбор языка

chose_lang = st.multiselect('Выберите язык для распознавания:', languages)

# ---------------------Функция отрисовки границ bounding-box-ов---------------------

def draw_boxes(image, bounds, color='yellow', width=2):

    image = Image.open(image) # чтобы загруженное img перевести в "путь" к нему (str)

    draw = ImageDraw.Draw(image)

    for bound in bounds:

        p0, p1, p2, p3 = bound[0]

        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)

    return st.image(image)


if st.button('Распознать текст с загруженного изображения'):
    if not chose_lang:
        st.write('_Обработка приостановлена: выберите язык для распознавания._') #Проверка выбран ли язык
    else:
        reader = easyocr.Reader(chose_lang)

        with open("123.PNG", "rb") as f:
            img = f.read()
        result = reader.readtext(img, detail=0, paragraph=False)

        with open("result.txt", "w") as f: #Сохраняем полученный вывод в файл
            for i in result:
                f.write(i)

            st.markdown('##### Распознанный текст:')

            for string in result:
                st.write(string)