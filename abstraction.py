# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import PIL

filename = ('tree.jpg')

img = plt.imread(filename)
old_img = plt.imread(filename)

height = len(img)
width = len(img[0])

#This changes the green leaves and the trunk of the tree to a magenta color.
for r in range(height):
    for c in range(width):
        if sum(img[r][c])<700: #If the sum of the RGB values is less than 700, do the following code. That way, none of the white background will be changed.
            if sum(img[r][c])>200: #If the sum of the RGB values are less than 750 but more than 200, the pixel is changed to a very bright magenta.
                img[r][c] = [250,0,225]
                
            elif sum(img[r][c])>150: #If the sum of the RGB values are less than 200 but more than 150, the pixel is changed to a bright reddish-magenta.
                img[r][c] = [250,0,125]
            
            elif sum(img[r][c])>125: #If the sum of the RGB values are less than 150 but more than 125, the pixel is changed to a reddish-magenta.
                img[r][c] = [200,0,150]
                
            elif sum(img[r][c])>100: #If the sum of the RGB values are less than 125 but more than 100, the pixel is changed to a less bright magenta.
                img[r][c] = [200,0,200]
            
            elif sum(img[r][c])>50: #If the sum of the RGB values are less than 100 but more than 50, the pixel is changed to a dimmer red-magenta.
                img[r][c] = [50,0,25]
            
            elif sum(img[r][c])>25: #If the sum of the RGB values are less than 100 but more than 50, the pixel is changed to a VERY DIM magenta.
                img[r][c] = [25,0,15]
            
            elif sum(img[r][c])>15:
                img[r][c] = [15,0,15]
                
            #The darkest values stay the same as they were.

#This changes part of the original white background to green.
for r in range(0,1110):
    for c in range(width):
        
        if sum(img[r][c])>=700: #If the sum of the RGB values is more than 700 (this'll be a white-ish color), the pixel is changed to green.
            img[r][c] = [0,150,0]

#This changes part of the original white background to blue.         
for r in range(1110,1270):
    for c in range(width):
        if sum(img[r][c])>=700: #If the sum of the RGB values is more than 700 (this'll be a white-ish color), the pixel is changed to blue.
            img[r][c] = [0,0,150]


height = len(img)
width = len(img[0])
    
# Create figure with two subplots.
fig, ax = plt.subplots(1, 2)

fig.show()


ax[0].imshow(img, interpolation='none') #Show the new image on the left
ax[1].imshow(old_img, interpolation='none') #Show the old image on the right

#save the altered image
new_tree = PIL.Image.fromarray(img)
new_tree.save('new-tree.jpg')
