from flask import Flask, render_template, url_for, request
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

MODEL_PATH ='./models/arctic_animal_classification.h5'

model = load_model(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classifier')
def classifier():
    return render_template('indexClassifier.html')

@app.route('/predictAnimalClassifier', methods=['POST'])
def predict():
    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)

    # Make prediction
    img = image.load_img(file_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x=x/255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)


    # Decoding prediction

    labels = {0: 'Arctic Fox', 1: 'Arctic Hare', 2: 'Arctic Skua', 3: 'Arctic Tern', 4: 'Arctic Wolf', 5: 'Arctic Woolly Bear Moth', 6: 'Bald Eagle', 7: 'Bearded Seal', 8: 'Beluga Whale', 9: "Brunnich's Guillemots", 10: 'Canada Goose', 11: 'Caribou', 12: 'Dall Sheep', 13: 'Ermine', 14: 'Greenland Shark', 15: 'Harp Seal', 16: 'Hooded Seal', 17: 'Lemming', 18: 'Moose', 19: 'Musk Ox', 20: 'Narwhal', 21: 'Orca', 22: 'Polar Bear', 23: 'Ptarmigan', 24: 'Puffin', 25: 'Ribbon Seal', 26: 'Ringed Seal', 27: 'Sea Otter', 28: 'Snow Goose', 29: 'Snowshoe Hare', 30: 'Snowy Owl', 31: 'Spotted Seal', 32: 'Walrus', 33: 'Wolverine'}

    result = labels[preds[0]]

    return render_template('indexClassifier.html', predictionText = 'The animal is a : {}'.format(result))

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(debug=True)
