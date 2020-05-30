from PIL import Image
from pylab import *

images_folder = '../images/'
image_name = 's15.jpeg'

image = Image.open(images_folder + image_name)

center = [image.height / 2, image.width / 2]
radius = min(image.height, image.width) / 2
start_point = [image.height / 2, image.width]
step = 30

for angle in range(0, 360, step):
    start_point = [start_point[0] * cos(angle), start_point[1] * sin(angle)]
    plot(center, start_point)

title("S15 Plotting")
imshow(image)
show()
