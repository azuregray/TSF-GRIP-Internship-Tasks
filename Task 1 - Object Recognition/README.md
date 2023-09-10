# GRIP23-COMPUTER-VISION-IOT-Task-1
Object detection-
First of all, you need to install OpenCV,OpenCV is an image processing library. It is designed to solve computer vision problems.
For Object Detection, specifies the location of multiple objects in the image

-classification
-localization
Algorithm for object detection:
-SSD-MobileNetv3
dataset for object detection:
-COCO
	WORKING FLOW
1-Importing Transfer Learning model 
2-Import dnn_DetecctionModel
3-Looping through the coco dataset
4-Initializing Threshold 
5-Testing the model on Image
6-Looping through the Labels
7-Implementing on Video

We use the "file handling" method in python to read the coco data set and loop through it.
The function imread loads an image from the specified file and returns it. 
create a blob or (Binary large object) and using the function blobFromImage
we give it a 320 by 320 pixel blob
with scale factor 1.0/127.5 and the mean.
you can play with these numbers and see yourself which gives you the best results.

In order to classify the objects in the image, we have to define a particular threshold. 

So that if the value is more than that particular threshold, then the object will be classified into that particular class.

After initializing the threshold in order to classify the image, we have to loop through the labels and compare the object with a particular label.


