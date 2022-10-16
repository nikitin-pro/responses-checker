import io
import streamlit
from PIL import Image
import imagehash

correct_hash = ''

def get_hash(img):
    hash = imagehash.average_hash(img)
    return hash


def load_image_correct():
    uploaded_file = streamlit.file_uploader(label='Upload correct response', key=0, type=['png','jpg'])
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        streamlit.image(image_data)
        img = Image.open(io.BytesIO(image_data))
        correct_hash = get_hash(img)
        

def load_image():
    uploaded_files = streamlit.file_uploader(label='Upload images to test', key=1, type=['png','jpg'], accept_multiple_files=True)
    if uploaded_files is not None:
        with streamlit.container():
            for file in uploaded_files:
                image_data = file.getvalue()
                img = Image.open(io.BytesIO(image_data))
                hash = get_hash(img)
                delta = correct_hash - hash
                resu = 'PASSED!' if delta <= 1 else 'FAILED!'
                streamlit.write(resu)
    else:
        return None


streamlit.title('Get image hash')
load_image_correct()
load_image()

