from flask import Flask, render_template, request, jsonify
import base64
import numpy as np
import cv2
import time
import tensorflow as tf
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/recognize', methods = ['POST'])
def recognize():

    if request.method == 'POST':
        print('Receive image and start predicting')
        data = request.get_json()
        imageBase64 = data['image']
        imgBytes = base64.b64decode(imageBase64)

        with open('predict_img.jpg', 'wb') as temp:
            temp.write(imgBytes)

        time.sleep(1)

        # Load the image
        image = cv2.imread('predict_img.jpg')
        image = cv2.resize(image, (28,28), interpolation=cv2.INTER_AREA)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        img_predict = (255 - img_gray.reshape(1, 28, 28).astype('float32'))/255.
        print(img_predict.shape)
        print(img_predict)

        # Load trained model
        classes_name = ['The Eiffel Tower', 'Axe', 'Bicycle', 'Golf Club', 'Pizza']
        model = tf.keras.models.load_model('saved_model/quickdraw.h5')
        print(model.summary())
        prediction = int(np.argmax(model.predict(img_predict)))
        print('Model predict: ',model.predict(img_predict))
        predict_class = classes_name[prediction]

        print('Prediction: ',predict_class)
        return jsonify({
                'prediction': str(predict_class),
                'status': True,
        })

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=81)
    app.run(debug = True)