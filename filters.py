import cv2
import numpy as np


def blur_image(img, k):

    if k % 2 == 0:
        k += 1

    return cv2.GaussianBlur(
        img,
        (k, k),
        0
    )


def sharpen_image(img, value):

    kernel = np.array([
        [0, -1, 0],
        [-1, 5 + value, -1],
        [0, -1, 0]
    ])

    return cv2.filter2D(
        img,
        -1,
        kernel
    )


def change_brightness(img, value):

    return cv2.convertScaleAbs(
        img,
        alpha=1,
        beta=value
    )


def change_contrast(img, value):

    return cv2.convertScaleAbs(
        img,
        alpha=value,
        beta=0
    )


def gray_image(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    return cv2.cvtColor(
        gray,
        cv2.COLOR_GRAY2BGR
    )


def edge_detect(img, t1, t2):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        t1,
        t2
    )

    return cv2.cvtColor(
        edges,
        cv2.COLOR_GRAY2BGR
    )