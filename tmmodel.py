import cv2
import numpy as np
import time
from keras.models import load_model

# This program detects if the user is looking at their phone.
# it takes an image every so often, then issues a warning if a phone is detected
# spam press the esc key to close the program (since the escapeing code is in
# the loop that has a delay you relly have to spam it)

# The probability threshold to determine that there is a phone onscreen
# if the model thinks there is above this probability that it sees a phone,
# then it will issue a warning
PROBABILITY_THRESHOLD = 0.8

# Delay time between checks in seconds
DELAY = 0.01

# warning function that is called when the conditions to issue a warning are met
# change to whatever you want
def warning():
    print("GET OFF YOUR PHONE")


# Load the model
# Loading model 1
# model = load_model("tmmodel1/keras_model.h5")
# Loading model 2
model = load_model("keras_model2.h5")


# CAMERA can be 0 or 1 based on default camera of your computer.
camera = cv2.VideoCapture(0)

# Grab the labels from the labels.txt file. This will be used later.
# Labels for model 1
# labels = open("tmmodel1/labels.txt", "r").readlines()
# Labels for model 2
labels = open("labels.txt", "r").readlines()

# truth_queue = np.repeat(False, NUM_SECONDS_STORED / DELAY).tolist()
# print(len(truth_queue))

while True:
    # wait one second
    time.sleep(DELAY)
    # Grab the webcameras image.
    ret, image = camera.read()
    # Resize the raw image into (224-height,224-width) pixels.
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    # Show the image in a window
    cv2.imshow("Webcam Image", image)
    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    # Normalize the image array
    image = (image / 127.5) - 1
    # Have the model predict what the current image is. Model.predict
    # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
    # it is the first label and 80% sure its the second label.
    probabilities = model.predict(image)

    # Detect if the probability of a phone onscreen is greater than the
    # given threshold
    # DETECTS BETTER WHEN PHONE IS ON
    if probabilities[0][0] > PROBABILITY_THRESHOLD:
        print(probabilities[0])
        warning()

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)
    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
