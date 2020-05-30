from PIL import Image
from pylab import *

images_folder = '../images/'
image_name = 'r32.jpg'

image = Image.open(images_folder + image_name)
imshow(image)

title("Please, click on stop-lights")
input = ginput(4)
print("Thank you!")

show()
