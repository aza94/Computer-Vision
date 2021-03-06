import numpy
import cv2
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
# Coment 1: List of formats supported by im.read taken from http://docs.opencv.org/master/modules/imgcodecs/doc/reading_and_writing_images.html because 
# i needed it to read only images and not other type of files. '''
formats_supported=['.bmp','.jpeg','.jpg','.jpe','.jp2','.png','.webp','.pbm','pgm','ppm','.sr','.ras','.tiff','.tif'];
# End of Coment 1
while True:
# Coment 2: Took it from http://stackoverflow.com/questions/3579568/choosing-a-file-in-python-simple-gui because I didn't want to leave the static path 
# of the file so i used a file explorer'''
	Tk().withdraw();
	file_name = askopenfilename();
	fileName, fileExtension = os.path.splitext(file_name);
	# End of comment 2
	if fileExtension in formats_supported:
		break
	else:
		print "The file you chose is not an image, please select another file\nPress Intro to continue.";
		raw_input()
img=cv2.imread(file_name);
height, width, depth = img.shape;
cv2.imshow('Original Image',img);
for pixY in xrange(0,height):
	for pixX in xrange(0,width):
		blue=img[pixY][pixX][0];
		green=img[pixY][pixX][1];
		red=img[pixY][pixX][2];
		img[pixY][pixX]=[255,green,red];
cv2.imshow('Image with blue filter',img);
cv2.waitKey();
