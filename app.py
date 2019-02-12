import base64

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    with open('download.jpeg', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return render_template('test.html', img_data=encoded_string)
