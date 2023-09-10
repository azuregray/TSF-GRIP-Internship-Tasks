'''

Hi, This is DARSHAN S.
Intern under GRIP Internship Programme @ The Sparks Foundation.

Here is my first TASK DETAILS:
Title: OBJECT RECOGNITION MODEL (ORM)
Description: Implement an object detection model which identifies different classes of objects in an image or video.

Here is my code for the same:
'''

# Author: Darshan S
# LinkedIn ID: linkedin.com/in/arcticblue/
# Do check out my GitHub Repository: github.com/azuregray/


# Firstly, Lets start with importing required libraries.

import cv2
import matplotlib.pyplot as plt

# Linking the required file, dataset and getting on with the object recognition engine.

config_file = r"D:\Darshan\Downloads\TSF_GRIP\Task1\Assets\RecognitionPrerequisite.pbtxt"
frozen_model = r"D:\Darshan\Downloads\TSF_GRIP\Task1\Assets\FrozenInferenceGraph.pb"
model = cv2.dnn_DetectionModel(frozen_model, config_file)
classLabels = []
file_name = r"D:\Darshan\Downloads\TSF_GRIP\Task1\Assets\RecognizedClassNames.names"
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

print(classLabels)
print(len(classLabels))
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# IMAGE OBJECT RECOGNITION HEAD STARTS HERE:

img = cv2.imread(r"D:\Darshan\Downloads\TSF_GRIP\Task1\Assets\BusyStreet.jpg")
plt.imshow(img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
print(ClassIndex)
font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN
for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    cv2.rectangle(img, boxes, (255, 0, 0), 2)
    cv2.putText(img, str(round(conf * 100, 2)) + "%", (boxes[0] + 161, boxes[1] + 30), font, 1, (0, 0, 255), 2)
    cv2.putText(img, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=font_scale, color=(0, 255, 0), thickness=3)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# VIDEO OBJECT RECOGNITION HEAD STARTS HERE:

cap = cv2.VideoCapture(r"D:\Darshan\Downloads\TSF_GRIP\Task1\Assets\TestVideo.mp4")
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Video Path Error!")

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, frame = cap.read()

    ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)

    print(ClassIndex)
    if (len(ClassIndex) != 0):
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            if (ClassInd <= 80):
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font,
                            fontScale=font_scale, color=(0, 255, 0), thickness=3)

        cv2.namedWindow('Object Detection Demonstration', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Object Detection Demonstration', 960, 540)
        cv2.imshow('Object Detection Demonstration', frame)
     
    if cv2.getWindowProperty('Object Detection Demonstration', cv2.WND_PROP_VISIBLE) < 1:
        break
     
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# END OF CODE