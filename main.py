import io
import streamlit
from PIL import Image
import imagehash


def get_hash(img):
    hash = imagehash.average_hash(img)
    return hash


def load_image_correct():
    file = streamlit.file_uploader(label='Upload correct response', key=0, type=['png','jpg'])
    if file is not None:
        streamlit.image(file.getvalue())
        img = Image.open(io.BytesIO(file.getvalue()))
        return get_hash(img)
        

def load_image():
    files = streamlit.file_uploader(label='Upload images to test', key=1, type=['png','jpg'], accept_multiple_files=True)
    if files is not None:
        with streamlit.container():
            for file in files:
                image_data = file.getvalue()
                img = Image.open(io.BytesIO(file.getValue()))
                hash = get_hash(img)
                delta = correct_hash - hash
                if delta<=1:
                    streamlit.write(file.name+' is PASSED!')
    else:
        return None


streamlit.title('Get image hash')
correct_hash = load_image_correct()
load_image()

