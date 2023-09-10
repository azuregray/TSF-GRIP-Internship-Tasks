import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import imutils

clusters = 5
image = cv2.imread(r"D:\Darshan\Downloads\TSF_GRIP\Task2\Assets\Colors.jpg")

originalImage = image.copy()
img = imutils.resize(image,height=200)
flatImage = np.reshape(image,(-1,3))
kmeans = KMeans(n_clusters=clusters,random_state=0)
kmeans.fit(flatImage)
dominant_colors = np.array(kmeans.cluster_centers_,dtype='uint')
percentages = (np.unique(kmeans.labels_,return_counts=True)[1])/flatImage.shape[0]
p_and_c = zip(percentages,dominant_colors)
p_and_c = sorted(p_and_c,reverse=True)

block = np.ones((50, 50, 3),dtype='uint')
plt.figure(figsize=(12, 8))
for i in range(clusters):
    plt.subplot(1, clusters, i+1)
    # we have done this to convert bgr(opencv) to rgb(matplotlib)
    block[:] = p_and_c[i][1][::-1]
    plt.imshow(block)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(str(round(p_and_c[i][0]*100,2))+'%')

bar = np.ones((50,500,3),dtype='uint')
start = 0
i = 1

for p,c in p_and_c:
    end = start+int(p*bar.shape[1])
    if i==clusters:
        bar[:,start:] = c[::-1]
    else:
        bar[:,start:end] = c[::-1]
    start = end
    i+=1


rows = 1000
cols = int((originalImage.shape[0]/originalImage.shape[1])*rows)
img = cv2.resize(originalImage,dsize=(rows,cols),interpolation=cv2.INTER_LINEAR)
copy = image.copy()
cv2.rectangle(copy,(rows//2-250,cols//2-90),(rows//2+250,cols//2+110),(255,255,255),-1)

final = cv2.addWeighted(image,0.1,copy,0.9,0)
cv2.putText(final,'Most Dominant Colors in the Image',(rows//2-230,cols//2-40),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,0),1,cv2.LINE_AA)

start = rows//2-220
for i in range(5):
    end = start+70
    final[cols//2:cols//2+70,start:end] = p_and_c[i][1]
    cv2.putText(final,str(i+1),(start+25,cols//2+45),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1,cv2.LINE_AA)
    start = end+20

plt.show()

cv2.imshow('image',final)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output.png',final)