# Use command line interface options
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image",   type=str, default='none.png')
parser.add_argument("-n", "--number",  type=int, default=10)
args = parser.parse_args()
print(args)

# Image
from image import image
i = image()
i.set_original(args.image)
i.decode()

# Kmeans
from kmeans import kmeans
k = kmeans()
k.set_clusters(args.number)
k.set_image(i)
k.run()

# Save
i.save()