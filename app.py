from flask import Flask, render_template, request, redirect, url_for
# import cv2
# import pandas as pd
# import time
# import os
# from datetime import datetime
# import face_recognition

app = Flask(__name__)

# # Function to capture image and return the file path
# def capture_image(customer_name):
#     cam = cv2.VideoCapture(0)
#     cv2.namedWindow("Capturing Image")

#     # Capture frame-by-frame
#     ret, frame = cam.read()
#     if not ret:
#         print("Failed to grab frame")
#         return None

#     img_name = f"static/captured_images/{customer_name}_{int(time.time())}.png"
#     cv2.imwrite(img_name, frame)
#     print(f"{img_name} written!")

#     cam.release()
#     cv2.destroyAllWindows()

#     return img_name

# # Function to store customer details in CSV
# def store_customer_details(customer_name, mobile_number, product_ordered, img_path, event, date_time):
#     data = {
#         "Customer Name": [customer_name],
#         "Mobile Number": [mobile_number],
#         "Product ordered": [product_ordered],
#         "Image Path": [img_path],
#         "Event": [event],
#         "Date and Time": [date_time]
#     }
    
#     df = pd.DataFrame(data)
    
#     # Append to CSV file or create if it doesn't exist
#     if not os.path.isfile('customer_details.csv'):
#         df.to_csv('customer_details.csv', index=False)
#     else:
#         df.to_csv('customer_details.csv', mode='a', header=False, index=False)

# # Function to check if user exists based on mobile number
# def user_exists(mobile_number):
#     if not os.path.isfile('customer_details.csv'):
#         return False
    
#     df = pd.read_csv('customer_details.csv')
#     return not df[df['Mobile Number'] == mobile_number].empty

# # Function to recognize faces
# def recognize_face(img_path):
#     known_face_encodings = []
#     known_face_metadata = []

#     if os.path.isfile('customer_details.csv'):
#         df = pd.read_csv('customer_details.csv')
#         for index, row in df.iterrows():
#             img = face_recognition.load_image_file(row['Image Path'])
#             encoding = face_recognition.face_encodings(img)
#             if encoding:
#                 known_face_encodings.append(encoding[0])
#                 known_face_metadata.append(row)

#     unknown_image = face_recognition.load_image_file(img_path)
#     unknown_face_encodings = face_recognition.face_encodings(unknown_image)

#     for unknown_face_encoding in unknown_face_encodings:
#         results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
#         if True in results:
#             match_index = results.index(True)
#             return known_face_metadata[match_index]

#     return None

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
        # date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # img_path = capture_image(customer_name)
        # if img_path is None:
        #     return "Failed to capture image. Please try again."

        # recognized_customer = recognize_face(img_path)

        # discount = False
        # if recognized_customer is not None:
        #     discount = True
        # elif user_exists(mobile_number):
        #     discount = True
        
        # store_customer_details(customer_name, mobile_number, product_ordered, img_path, event, date_time)

        return render_template('form.html', customer_name=customer_name, product_ordered=product_ordered, event=event)#, date_time=date_time, img_path=img_path, discount=discount)


products = [
    {"id":"bn1","name": "Bday Balloons", "price": 60.00, "image": "bn1.jpg"},
    {"id":"bn2","name": "Bday Balloons", "price": 70.00, "image": "bn2.jpg"},
    {"id":"bn3","name": "Bday Balloons", "price": 50.00, "image": "bn3.jpeg"},
    {"id":"bn4","name": "Bday Balloons", "price": 110.00, "image": "bn4.jpg"},
    {"id":"bn5","name": "Valentine Balloons", "price": 70.00, "image": "bn5.jpg"},
    {"id":"bn6","name": "Anniversary Balloons", "price": 110.00, "image": "bn6.jpg"},
    {"id":"bn7","name": "Anniversary Balloons", "price": 115.00, "image": "bn7.jpg"},
    {"id":"bn8","name": "Anniversary Balloons", "price": 200.00, "image": "bn8.webp"},
    {"id":"bn9","name": "Retirement Balloons", "price": 70.00, "image": "bn9.jpg"},
    {"id":"bn10","name": "Retirement Balloons", "price": 110.00, "image": "bn10.jpg"},
    {"id":"bn11","name": "Ballons", "price": 20.00, "image": "bn11.jpg"},
    
    {"id":"card1","name": "Bday cards", "price": 100.00, "image": "card1.jpg"},
    {"id":"card2","name": "Bday cards", "price": 110.00, "image": "card2.jpg"},
    {"id":"card3","name": "Bday cards", "price": 50.00, "image": "card3.jpg"},
    {"id":"card4","name": "Valentines cards", "price": 80.00, "image": "card4.jpg"},
    {"id":"card5","name": "Anniversary cards", "price": 60.00, "image": "card5.jpg"},
    {"id":"card6","name": "Anniversary cards", "price": 150.00, "image": "card6.jpg"},
    {"id":"card7","name": "Retirement cards", "price": 65.00, "image": "card7.jpg"},
    {"id":"card8","name": "Wedding cards", "price": 100.00, "image": "card8.jpg"},
    {"id":"card9","name": "Wedding cards", "price": 90.00, "image": "card9.jpg"},
    
    {"id":"bc1","name": "Bday Cake", "price": 1000.00, "image": "bc1.jpg"},
    {"id":"bc2","name": "Bday Cake", "price": 1000.00, "image": "bc2.jpg"},
    {"id":"bc3","name": "Bday Cake", "price": 1050.00, "image": "bc3.jpg"},
    {"id":"c4","name": "Bday Cake", "price": 500.00, "image": "c4.png"},
    {"id":"c9","name": "Bday Cake", "price": 550.00, "image": "c9.png"},
    {"id":"box3","name": "Bday Cake", "price": 500.00, "image": "box3.jpg"},
    {"id":"box1","name": "Bday Cake", "price": 600.00, "image": "box1.jpg"},
    {"id":"cake","name": "Bday Cake", "price": 500.00, "image": "cake.jpeg"},
    {"id":"strawcake","name": "Bday Cake", "price": 700.00, "image": "strawcake.jpg"},
    {"id":"images","name": "Bday Cake", "price": 450.00, "image": "images.jpg"},
    {"id":"ac1","name": "Anniversary Cake", "price": 500.00, "image": "ac1.jpg"},
    {"id":"ac2","name": "Anniversary Cake", "price": 400.00, "image": "ac2.jpg"},
    {"id":"ac3","name": "Anniversary Cake", "price": 600.00, "image": "ac3.jpg"},
    {"id":"ac4","name": "Anniversary Cake", "price": 500.00, "image": "ac4.jpg"},
    {"id":"ec","name": "Engagement Cake", "price": 550.00, "image": "ec.jpg"},
    {"id":"ec1","name": "Engagement Cake", "price": 450.00, "image": "ec1.jpg"},
    {"id":"ec2","name": "Engagement Cake", "price": 600.00, "image": "ec2.jpg"},
    {"id":"rc","name": "Retirement Cake", "price": 500.00, "image": "rc.jpg"},
    {"id":"rc1","name": "Retirement Cake", "price": 700.00, "image": "rc1.jpg"},
    
    {"id":"cn1","name": "Number Candles", "price": 20.00 , "image": "cn1.jpg"},
    {"id":"cn2","name": "Candles", "price": 100.00, "image": "cn2.jpg"},
    {"id":"cn3","name": "Sparkle Candles", "price": 10.00 , "image": "cn3.jpg"},
    {"id":"cn4","name": "Candles", "price": 50.00, "image": "cn4.jpg"},
    {"id":"cn5","name": "Candles", "price": 70.00, "image": "cn5.png"},
    {"id":"cn7","name": "Letter Candles", "price": 110.00, "image": "cn7.jpg"},
    {"id":"cn8","name": "Valentine Candles", "price": 115.00, "image": "cn8.jpg"},
    {"id":"cn9","name": "Candles", "price": 150.00, "image": "cn9.jpg"},
    {"id":"cn10","name": "Candles", "price": 175.00, "image": "cn10.jpg"},
    {"id":"cn11","name": "Candles", "price": 175.00, "image": "cn11.jpg"},
    {"id":"cn11","name": "Candles", "price": 60.00, "image": "cn12.jpg"},
    
    {"id":"cr1","name": "Crowns", "price": 120.00, "image": "cr1.jpeg"},
    {"id":"cr2","name": "Crowns", "price": 100.00, "image": "cr2.jpg"},
    {"id":"cr3","name": "Crowns", "price": 150.00, "image": "cr3.jpg"},
    {"id":"cr4","name": "Crowns", "price": 250.00, "image": "cr4.jpg"},
    {"id":"cr5","name": "Crowns", "price": 270.00, "image": "cr5.jpg"},
    {"id":"cr6","name": "Crowns", "price": 110.00, "image": "cr6.jpg"},
    {"id":"cr7","name": "Crowns", "price": 115.00, "image": "cr7.jpeg"},
    {"id":"cr8","name": "Crowns", "price": 250.00, "image": "cr8.jpg"},
    {"id":"cr9","name": "Crowns", "price": 115.00, "image": "cr9.jpg"},
    {"id":"cr10","name": "Crowns", "price": 100.00, "image": "cr10.jpg"},
    {"id":"cr11","name": "Crowns", "price": 150.00, "image": "cr11.jpg"},
    {"id":"cr12","name": "Crowns", "price": 150.00, "image": "cr12.webp"},
    {"id":"crowns2","name": "Crowns", "price": 250.00, "image": "crowns2.jpg"},
    
    {"id":"s1","name": "Sash Design", "price": 150.00, "image": "s1.jpg"},
    {"id":"s2","name": "Sash Design", "price": 100.00, "image": "s2.jpg"},
    {"id":"s3","name": "Sash Design", "price": 50.00, "image": "s3jpg"},
    {"id":"s4","name": "Sash Design", "price": 70.00, "image": "s4.jpg"},
    {"id":"s5","name": "Sash Design", "price": 110.00, "image": "s5.jpg"},
    {"id":"s6","name": "Sash Design", "price": 115.00, "image": "s6.jpg"},
    {"id":"s7","name": "Sash Design", "price": 150.00, "image": "s7.jpg"},
    {"id":"s8","name": "Sash Design", "price": 115.00, "image": "s8.jpg"},
    {"id":"s9","name": "Sash Design", "price": 100.00, "image": "s9.jpg"},
    
]

@app.route('/balloons')
def balloons():
    return render_template('balloons.html', products=products[:11])

@app.route('/bdaycards')
def bdaycards():
    return render_template('bdaycards.html', products=products[11:20])

@app.route('/cakes')
def cakes():
    return render_template('cakes.html', products=products[20:39])

@app.route('/candles')
def candles():
    return render_template('candles.html', products=products[39:50])

@app.route('/crowns')
def crowns():
    return render_template('crowns.html', products=products[50:59])

@app.route('/sash')
def sash():
    return render_template('sash.html', products=products[59:])


@app.route('/checkout', methods=['POST'])
def checkout():
    product_id = request.form['product_id']
    selected_product = next((p for p in products if p['id'] == product_id), None)
    if selected_product:
        return render_template('checkout.html', product=selected_product)
    else:
        return "Product not found", 404

    return render_template('checkout.html', product=product)

if __name__ == "__main__":
    # if not os.path.exists('static/captured_images'):
    #     os.makedirs('static/captured_images')
    app.run(debug=True)
