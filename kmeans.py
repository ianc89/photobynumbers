import cv2
import numpy as np

class kmeans(object):
	def __init__(self):
		self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
		self.attempts = 3
		self.nclusters = None
		self.image = None

	def set_clusters(self, clusters):
		self.nclusters = clusters

	def set_image(self, image):
		self.image = image

	def run(self):
		# Run kmeans (ret is an overall metric)
		ret,label,center = cv2.kmeans(self.image.original_data, self.nclusters, None, self.criteria, self.attempts, cv2.KMEANS_PP_CENTERS)
		# Center is the array of cluster colours
		center = np.uint8(center)
		# Label is the identifier for center colour per pixel
		res = center[label.flatten()]
		# Data in 1D array
		self.image.new_data = res
		# Data formatted for image shape
		self.image.new_img  = res.reshape((self.image.original_img.shape))
