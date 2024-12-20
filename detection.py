import cv2
import glob
import numpy as np
import os
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pickle


# Step 1: Data Collection
# Collect images of regular and non-regular customers and save them in separate directories
img_dir="C:/Users/spbha/OneDrive/Desktop/Project5-main/Project5-main/static/captured_images"

# Step 2: Data Preprocessing

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_gray = cv2.resize(gray, (100, 100))  # Resize image to a fixed size
    return resized_gray

# Step 3: Feature Extraction
def extract_features(image_path):
    resized_gray = preprocess_image(image_path)

    if not isinstance(resized_gray, np.ndarray):
        raise TypeError("Preprocessed image is not a numpy array")
    # For simplicity, use the flattened pixel values as features
    features = resized_gray.flatten()
    return features

# Step 4: Model Training
def train_model():
    X = []
    y = []
    for image_path in glob.glob(os.path.join(img_dir, "*.png")):
        features = extract_features(image_path)
        X.append(features)
        y.append(1)  # Label for regular customers

    '''for image_path in glob.glob(non_regular_dir):
        features = extract_features(image_path)
        X.append(features)
        y.append(0)  # Label for non-regular customers'''

    # Train a k-Nearest Neighbors (k-NN) classifier using the extracted features and labels
    #model = KNeighborsClassifier(n_neighbors=3)  # Example: Using k=3
    model = SVC(kernel='linear', C=1)
    model.fit(X, y)
    #Save the trained model using pickle
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model

# Step 5: Model Evaluation (Optional)
def evaluate_model(model):
    # Evaluate the trained model using a separate validation set (if available)
    pass

# Step 6: Customer Feedback Survey
def recognize_customer(model):
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture frame from camera")
            break

        # Preprocess the frame and extract features
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(gray, (100, 100))
        features = resized_gray.flatten()

        # Use the trained model to predict whether the person is a regular customer or not
        prediction = model.predict([features])

        # Display the prediction result on the frame
        if prediction == 1:
            cv2.putText(frame, "Regular Customer", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Non-Regular Customer", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Customer Feedback Survey", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''else:
            print("Error: Failed to read frame from camera")'''
    camera.release()
    cv2.destroyAllWindows(5)

# Main function
if __name__ == "__main__":
    # Train the model
    model = train_model()

    # Evaluate the model (optional)
    evaluate_model(model)

    # Perform customer feedback survey using the trained model
    recognize_customer(model)
