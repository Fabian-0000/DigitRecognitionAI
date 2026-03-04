from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.preprocessing import image as tfimage
import tensorflow as tf

def get_rect(image: Image):
    pixels = image.load()
    w, h = image.size

    rx1, ry1, rx2, ry2 = w, h, 0, 0

    # Find bounding box of non-white pixels
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            if (r, g, b) != (255, 255, 255):
                rx1 = min(rx1, x)
                ry1 = min(ry1, y)
                rx2 = max(rx2, x)
                ry2 = max(ry2, y)

    # Compute width and height
    nw, nh = rx2 - rx1 + 1, ry2 - ry1 + 1

    # Make square by expanding the smaller dimension
    if nw > nh:
        diff = nw - nh
        ry1 -= diff // 2
        ry2 += diff - diff // 2
    else:
        diff = nh - nw
        rx1 -= diff // 2
        rx2 += diff - diff // 2

    # Clamp to image boundaries
    rx1 = max(0, rx1)
    ry1 = max(0, ry1)
    rx2 = min(w - 1, rx2)
    ry2 = min(h - 1, ry2)

    return rx1, ry1, rx2, ry2

def evaluate(image: Image):
    rect = get_rect(image)
    cropped_img = image.convert("L").crop(rect)
    scaled_img = cropped_img.resize((28, 28), Image.Resampling.LANCZOS)

    model = tf.keras.models.load_model("digit_model.keras")

    img_array = tfimage.img_to_array(scaled_img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    return prediction