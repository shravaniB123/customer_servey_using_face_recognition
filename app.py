from flask import Flask, render_template, request, redirect, url_for
import cv2
import pandas as pd
import time
import os
from datetime import datetime
import face_recognition

app = Flask(__name__)

# Function to capture image and return the file path
def capture_image(customer_name):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capturing Image")

    # Capture frame-by-frame for 5 seconds
    start_time = time.time()
    ret, frame = cam.read()
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
def store_customer_details(customer_name, mobile_number, product_ordered, img_path, event, date_time):
    data = {
        "Customer Name": [customer_name],
        "Mobile Number": [mobile_number],
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

# Function to check if user exists based on mobile number
def user_exists(mobile_number):
    if not os.path.isfile('customer_details.csv'):
        return False
    
    df = pd.read_csv('customer_details.csv')
    return not df[df['Mobile Number'] == mobile_number].empty

# Function to recognize faces
def recognize_face(img_path):
    known_face_encodings = []
    known_face_metadata = []

    if os.path.isfile('customer_details.csv'):
        df = pd.read_csv('customer_details.csv')
        for index, row in df.iterrows():
            img = face_recognition.load_image_file(row['Image Path'])
            encoding = face_recognition.face_encodings(img)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_metadata.append(row)

    unknown_image = face_recognition.load_image_file(img_path)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)

    for unknown_face_encoding in unknown_face_encodings:
        results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
        if True in results:
            match_index = results.index(True)
            return known_face_metadata[match_index]

    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        mobile_number = request.form['mobile_number']
        product_ordered = request.form['products_ordered']
        event = request.form['event']
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        img_path = capture_image(customer_name)
        recognized_customer = recognize_face(img_path)

        discount = False
        if recognized_customer is not None:
            discount = True
        elif user_exists(mobile_number):
            discount = True
        else:
            store_customer_details(customer_name, mobile_number, product_ordered, img_path, event, date_time)

        return render_template('form.html', customer_name=customer_name, product_ordered=product_ordered, event=event, date_time=date_time, img_path=img_path, discount=discount)

if __name__ == "__main__":
    if not os.path.exists('static/captured_images'):
        os.makedirs('static/captured_images')
    app.run(debug=True)
