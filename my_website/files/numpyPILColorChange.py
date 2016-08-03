import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL

def open_file(filename):
    #open the directory
    directory = os.path.dirname(os.path.abspath(__file__))
    #get the path to the file
    filepath = os.path.join(directory, filename)
    #open image
    img = plt.imread(filepath)
    return img

def color_change(image):
    height = len(image)
    width = len(image[0])
    centerR=height/2
    centerW=width/2
    for r in range(height):
        for c in range(width):
            #save original colors
            red=image[r][c][0]
            green=image[r][c][1]
            blue=image[r][c][2]
            #invert colors
            image[r][c][0]=255-blue
            image[r][c][1]=255-red
            image[r][c][2]=255-green

fileName='beyondce.jpg'
orig_image = open_file(fileName)
image_change1=open_file(fileName)
fig, ax = plt.subplots(1, 3)
ax[0].imshow(orig_image, interpolation='none')

color_change(image_change1)
ax[1].imshow(image_change1, interpolation='none')

temp_image = PIL.Image.fromarray(image_change1)
temp_image.save('/Users/nlmstaff/Desktop/1.4.2 Files/change1_'+fileName)
image_change2=temp_image.rotate(180)
image_change2.save('/Users/nlmstaff/Desktop/1.4.2 Files/change2'+fileName)
ax[2].imshow(image_change2, interpolation='none')
fig.show()