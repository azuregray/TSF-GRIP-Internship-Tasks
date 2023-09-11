#TSF GRIP SEPTEMBER 2023 CV-IOT TASK 1
##Object detection:

First of all, you need to install OpenCV.

> OpenCV is an image processing library. It is designed sepcifically for use in Computer Vision Applications.

For Object Detection, specifies the location of multiple objects in the image

-classification
-localization

> Algorithm for object detection: SSD-MobileNetv3

> Dataset for object detection: COCO

###	WORKING FLOW
> 1 - Importing Transfer Learning model

> 2 - Import dnn_DetecctionModel

> 3 - Looping through the dataset

> 4 - Initializing Threshold

> 5 - Testing the model on Image

> 6 - Looping through the Labels

> 7 - Implementing on Video


We use the *File Handling* method in python to read the dataset set and loop through it.
The function *imread* loads an image from the specified file and returns it. 
Creates a *BLOB (Binary Large OBject)* and using the function blobFromImage
We specifically set the BLOB to be 320x320 pixels.
Keeping scale factor *1.0/127.5* along with the Mean.
These numbers are changeable for suiting the best appropriate results.

In order to classify the objects in the image, we have to define a particular threshold. 

So that if the value is more than that particular threshold, then the object will be classified into that particular class.

After initializing the threshold in order to classify the image, we have to loop through the labels and compare the object with a particular label.


