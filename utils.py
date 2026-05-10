import cv2
import numpy as np
from PIL import Image
import streamlit as st


def pil_to_cv(img):

    return cv2.cvtColor(
        np.array(img),
        cv2.COLOR_RGB2BGR
    )


def cv_to_pil(img):

    rgb = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    return Image.fromarray(rgb)


def img_to_bytes(img):

    success, buffer = cv2.imencode(
        ".png",
        img
    )

    if success:
        return buffer.tobytes()

    return None


def load_css(file):

    with open(file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )