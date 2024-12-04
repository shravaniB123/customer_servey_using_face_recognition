from flask import Flask, render_template, request, redirect, url_for
import cv2
import pandas as pd
import time
import os
from datetime import datetime

app = Flask(__name__)

# Function to capture image and return the file path
def capture_image(customer_name):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capturing Image")

    # Capture frame-by-frame for 5 seconds
    start_time = time.time()
    while int(time.time() - start_time) < 5:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Capturing Image", frame)
        cv2.waitKey(1)

    # Save the captured image
    img_name = f"static/captured_images/{customer_name}_{int(time.time())}.png"
    cv2.imwrite(img_name, frame)
    print(f"{img_name} written!")

    cam.release()
    cv2.destroyAllWindows()

    return img_name

# Function to store customer details in CSV
def store_customer_details(customer_name, product_ordered, img_path, event, date_time):
    data = {
        "Customer Name": [customer_name],
        "Product ordered": [product_ordered],
        "Image Path": [img_path],
        "Event": [event],
        "Date and Time": [date_time]
    }
    
    df = pd.DataFrame(data)
    
    # Append to CSV file or create if it doesn't exist
    if not os.path.isfile('customer_details.csv'):
        df.to_csv('customer_details.csv', index=False)
    else:
        df.to_csv('customer_details.csv', mode='a', header=False, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        product_ordered = request.form['products_ordered']
        event = request.form['event']
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        img_path = capture_image(customer_name)
        store_customer_details(customer_name, product_ordered, img_path, event, date_time)

        return render_template('form.html', customer_name=customer_name, product_ordered=product_ordered, event=event, date_time=date_time, img_path=img_path)

if __name__ == "__main__":
    if not os.path.exists('static/captured_images'):
        os.makedirs('static/captured_images')
    app.run(debug=True)










'''from flask import Flask, render_template, Response, request
import cv2
import numpy as np
import pandas as pd
import time

app = Flask(__name__)

# Initialize OpenCV's face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize pandas DataFrame to store customer details
customer_df = pd.DataFrame(columns=['Name', 'Age', 'Gender', 'Image_Path'])

# Function to capture real-time video and perform face recognition
def recognize_faces():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    
    while True:
        ret, frame = cap.read()
        
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Capture the face and save it to a CSV file along with customer details
                if time.time() - start_time < 5:
                    cv2.imwrite('captured_image.png', frame)
                    name = request.form.get('name')
                    age = request.form.get('age')
                    gender = request.form.get('gender')
                    customer_df.loc[len(customer_df)] = [name, age, gender, 'captured_image.png']
            
            # Display the frame
            cv2.imshow('Face Recognition', frame)
        
        if time.time() - start_time > 5:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Route to the webpage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    recognize_faces()
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)'''

'''from flask import Flask, render_template, request
import cv2
import numpy as np
from sklearn.svm import SVC
import pickle


# Load the pre-trained model (assuming it's saved as 'model.pkl')
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    # Get the uploaded image from the form
    image_file = request.files['image']
    
    # Check if an image is uploaded
    if image_file:
        image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Preprocess the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(gray, (100, 100))
        features = resized_gray.flatten()
        
        # Use the trained model to predict
        prediction = model.predict([features])
        
        if prediction == 1:
            result = "Regular Customer"
        else:
            result = "Non-Regular Customer"
        
        return render_template('result.html', prediction=result)
    
    else:
        return render_template('index.html', error="Please upload an image")
    
@app.route('/balloons')
def balloons():
    return render_template('balloons.html')

@app.route('/bdaycart')
def bdaycart():
    return render_template('bdaycart.html')

@app.route('/candles')
def candles():
    return render_template('candles.html')

@app.route('/sash')
def sash():
    return render_template('sash.html')

@app.route('/crowns')
def crowns():
    return render_template('crowns.html')

@app.route('/Cakes')
def cakes():
    return render_template('Cakes.html')

@app.route('/cart')
def addtocart():
    return render_template('cart.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5501)'''