import base64
import tempfile

import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request

app = Flask(__name__)
model = tf.keras.models.load_model('mnist.model')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        temp_file = tempfile.NamedTemporaryFile()
        with open(temp_file.name, 'wb') as file:
            file.write(base64.standard_b64decode(request.form.get('canvas-data', '')))

        image = cv2.imread(temp_file.name, cv2.IMREAD_UNCHANGED)

        # Adapted from: https://stackoverflow.com/a/46275857
        # Crop the image to a bounding box containing only the non transparent pixels
        # Get all nonzero alpha(Alpha is channel 3) coordinates
        y, x = image[:, :, 3].nonzero()
        min_x, min_y = np.min(x), np.min(y)
        max_x, max_y = np.max(x), np.max(y)

        image = image[min_y:max_y, min_x:max_x]

        transparency_mask = image[:, :, 3] == 0

        # Replace areas of transparency with white and not transparent
        image[transparency_mask] = [255, 0, 0, 0]

        greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        greyscale_mask = cv2.compare(greyscale_image, 5, cv2.CMP_LT)

        # Turn every non-black(grey) pixel into white. Allows image to be drawn as black on transparent and converted to
        # better match the actual MNIST model
        image[greyscale_mask > 0] = 255
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]

        # Blurring the image makes the image easier to detect
        image = cv2.GaussianBlur(image, (0, 0), cv2.BORDER_DEFAULT)
        image = cv2.resize(image, (20, 20))

        # Creates a black image of size 28x28
        processed_image = np.zeros((28, 28), np.uint8)
        processed_image[4:4 + image.shape[0], 4:4 + image.shape[1]] = image

        # Reshape, and normalise before passing to model
        data = model.predict(processed_image.reshape(1, 784).astype('float32') / 255.0)[0]

        return render_template('index.html', result=np.argmax(data), data=dict(enumerate(data.tolist())))

    return render_template('index.html')


if __name__ == "__main__":
    app.run()
