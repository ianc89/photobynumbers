import cv2
import numpy as np
import matplotlib.pyplot as plt

class image(object):
	def __init__(self):
		self.original = None
		self.original_img = None
		self.original_data = None
		self.new_data = None
		self.new_img = None

	def set_original(self, name):
		self.original = name

	def decode(self):
		# Decode image into array
		if self.original == None:
			print ("Original image not defined")
			return

		# Open the image
		rgb_img = cv2.imread(self.original)
		hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB)
		self.original_img = hsv_img
		self.original_data = hsv_img.reshape((-1,3))
		self.original_data = self.original_data.astype('float32')
		print (self.original_data.shape)
		print (self.original_data)

	def save(self):
		figure_size = 15
		plt.figure(figsize=(figure_size,figure_size))
		plt.subplot(2,1,1),plt.imshow(self.original_img)
		plt.title('Original Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(2,1,2),plt.imshow(self.new_img)
		plt.title('Segmented Image'), plt.xticks([]), plt.yticks([])
		plt.savefig("comparison.jpg")

