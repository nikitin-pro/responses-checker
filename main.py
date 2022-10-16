import io
import streamlit
from PIL import Image
import imagehash

def get_hash(img):
    hash = imagehash.average_hash(img)
    return hash


def load_image(lbl,multiple):
    uploaded_file = streamlit.file_uploader(label=lbl, key=lbl, type=['png','jpg'], accept_multiple_files=multiple)
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        streamlit.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None



streamlit.title('Get image hash')
img0 = load_image('Upload correct response',False)
img1 = load_image('Upload image to test',True)
result = streamlit.button('Check')
if result:
    hash0 = get_hash(img0)
    hash1 = get_hash(img1)
    delta = hash0 - hash1
    if delta <= 1:
        resu = 'PASSED!'
    else:
        resu = 'FAILED!'
    streamlit.write('**Verdict:**')
    streamlit.write(resu)
