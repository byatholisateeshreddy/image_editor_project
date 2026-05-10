import streamlit as st
from PIL import Image

from filters import (
    blur_image,
    sharpen_image,
    change_brightness,
    change_contrast,
    gray_image,
    edge_detect
)

from utils import (
    pil_to_cv,
    cv_to_pil,
    img_to_bytes,
    load_css
)

st.set_page_config(
    page_title="Image Editor",
    page_icon="🖼️",
    layout="wide"
)

load_css("styles.css")

if "blur" not in st.session_state:
    st.session_state["blur"] = 1

if "sharp" not in st.session_state:
    st.session_state["sharp"] = 1.0

if "bright" not in st.session_state:
    st.session_state["bright"] = 0

if "contrast" not in st.session_state:
    st.session_state["contrast"] = 1.0

if "gray" not in st.session_state:
    st.session_state["gray"] = False

if "edge" not in st.session_state:
    st.session_state["edge"] = False

if "t1" not in st.session_state:
    st.session_state["t1"] = 100

if "t2" not in st.session_state:
    st.session_state["t2"] = 200


def reset_values():

    st.session_state["blur"] = 1
    st.session_state["sharp"] = 1.0
    st.session_state["bright"] = 0
    st.session_state["contrast"] = 1.0
    st.session_state["gray"] = False
    st.session_state["edge"] = False
    st.session_state["t1"] = 100
    st.session_state["t2"] = 200


st.title("🖼️ Image Editor")
st.write("Edit images using OpenCV filters")

st.sidebar.header("Image Controls")

file = st.sidebar.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

blur = st.sidebar.slider(
    "Blur",
    1,
    31,
    step=2,
    key="blur"
)

sharp = st.sidebar.slider(
    "Sharpness",
    0.0,
    3.0,
    step=0.1,
    key="sharp"
)

bright = st.sidebar.slider(
    "Brightness",
    -100,
    100,
    key="bright"
)

contrast = st.sidebar.slider(
    "Contrast",
    0.5,
    3.0,
    step=0.1,
    key="contrast"
)

gray = st.sidebar.checkbox(
    "Convert to Grayscale",
    key="gray"
)

edge = st.sidebar.checkbox(
    "Edge Detection",
    key="edge"
)

t1 = st.sidebar.slider(
    "Threshold 1",
    0,
    255,
    key="t1"
)

t2 = st.sidebar.slider(
    "Threshold 2",
    0,
    255,
    key="t2"
)

st.sidebar.button(
    "Reset",
    on_click=reset_values
)

if file is not None:

    img = Image.open(file).convert("RGB")

    cv_img = pil_to_cv(img)

    out = cv_img.copy()

    if blur > 1:
        out = blur_image(out, blur)

    if sharp != 1.0:
        out = sharpen_image(out, sharp)

    if bright != 0:
        out = change_brightness(out, bright)

    if contrast != 1.0:
        out = change_contrast(out, contrast)

    if gray:
        out = gray_image(out)

    if edge:
        out = edge_detect(out, t1, t2)

    final_img = cv_to_pil(out)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img, use_container_width=True)

    with col2:
        st.subheader("Edited Image")
        st.image(final_img, use_container_width=True)

    st.markdown("---")

    download = img_to_bytes(out)

    st.download_button(
        "Download Image",
        data=download,
        file_name="edited.png",
        mime="image/png"
    )

else:

    st.markdown("""
    <div class="upload-box">
        <h2>Upload an image to start editing</h2>
        <p>Supported formats: JPG, JPEG, PNG</p>
    </div>
    """, unsafe_allow_html=True)