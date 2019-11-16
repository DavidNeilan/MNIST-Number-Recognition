import base64
import tempfile

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        with open('img.png', 'wb') as file:
            file.write(base64.standard_b64decode(request.form.get('canvas-data', '')))

        return render_template('index.html')

    return render_template('index.html')


if __name__ == "__main__":
    app.run()
