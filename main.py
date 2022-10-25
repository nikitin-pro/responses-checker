import io
import streamlit
from PIL import Image
import imagehash


def get_hash(img):
    hash = imagehash.average_hash(img)
    return hash


def load_image_correct():
    file = streamlit.file_uploader(label='Эталонный ответ:', key=0, type=['png','jpg'])
    if file is not None:
        image_data = file.getvalue()
        streamlit.image(image_data)
        img = Image.open(io.BytesIO(image_data))
        return get_hash(img)
        

def load_image():
    files = streamlit.file_uploader(label='Ответы студентов на проверку:', key=1, type=['png','jpg'], accept_multiple_files=True)
    if files is not None:
        with streamlit.container():
            counter = 0
            for file in files:
                image_data = file.getvalue()
                img = Image.open(io.BytesIO(image_data))
                hash = get_hash(img)
                delta = correct_hash - hash
                if delta<=5:
                    streamlit.subheader(file.name+' ПРАВИЛЬНЫЙ!')
                    counter += 1
            if counter == 0:
                streamlit.subheader('ПРАВИЛЬНЫХ ОТВЕТОВ НЕ НАЙДЕНО!')
    else:
        return None


streamlit.title('Проверка студенческих работ')
correct_hash = load_image_correct()
load_image()

