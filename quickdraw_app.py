from flask import Flask, render_template, request, jsonify
import base64
import numpy as np
import cv2
import time
import tensorflow as tf
app = Flask(__name__)

@app.route('/')
def index():
    # data = 'some data'
    # list = ["1", "2", "3"]

    return render_template('index.html')

@app.route('/recognize', methods = ['POST'])
def recognize():
    # theta = np.loadtxt(r'theta_all.txt')
    if request.method == 'POST':
        print('Receive image and start predicting')
        data = request.get_json()
        imageBase64 = data['image']
        imgBytes = base64.b64decode(imageBase64)

        with open('temp.jpg', 'wb') as temp:
            temp.write(imgBytes)

        time.sleep(1)

        # Load the image
        image = cv2.imread('temp.jpg')
        image = cv2.resize(image, (28,28), interpolation=cv2.INTER_AREA)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_predict = np.reshape(img_gray, (28,28,1))
        print(img_predict.shape)

        # Load trained model
        model = tf.keras.models.load_model('saved_model/quickdraw.h5')
        prediction = model.predict_classes(img_predict)

        print('Prediction: ',prediction)
        return jsonify({
                'prediction': str(prediction),
                'status': True,
        })

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=81)
    app.run(debug = True)