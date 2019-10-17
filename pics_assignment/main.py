import numpy as np
from PIL import Image
import os
from resizeimage import resizeimage

imageSize = (200, 200)
picsDir = os.listdir('./photos')
rootDir = './photos/'


# THE FILES FINDER FUNCTION
# It takes path of the Photos folder
# it will return the number of pics in it and the list of all available pics.
def filesfinder(directory):
    files_list = []

    for pic in directory:
        im = Image.open(rootDir + pic)

        files_list.append(im)

    length_of_list = len(files_list)

    return length_of_list, files_list


# THE RESIZING FUNCTION
# It takes the image size
# It will return the list of resized images
def resizing(image_size):
    resized_images = []
    for img in picsDir:
        image = Image.open(rootDir + img)
        image = resizeimage.resize_crop(image, image_size)
        # image.thumbnail(image_size)
        resized_images.append(image)

    return resized_images


# THE CONVERT TO NUMPY ARRAY FUNCTION
# It takes list of resized images
# It will return numpy array contain all 20 images
def converttonumpyarray(list_of_resized_images):
    for image in list_of_resized_images:
        array1 = np.array(image).reshape(200, 200, 3)
        for img in list_of_resized_images:
            array2 = np.array(image).reshape(200, 200, 3)
            array1 = np.concatenate((array1, array2))
        break

    return array1

#THE MAIN FUNCTION
#It runs all the local funtions
#it returns the numpy array of shape(200,200,3) containing all the images
def main():
    # Finding files
    num_of_files, list_of_pics = filesfinder(picsDir)
    print('Number of files are : ', num_of_files)

    # Resizing pictures
    resized_images = resizing(imageSize)
    print("Resized images are: ")
    print(resized_images)

    # Converting to numpy array
    nparray = converttonumpyarray(resized_images)
    print("Numpy array of 20 images are:")
    print(nparray)

    return nparray


if __name__ == "__main__":
    main()
