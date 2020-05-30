import numpy as np
from matplotlib import pyplot as pp

images_folder = '../images/'
image_name = 's15.jpeg'

image = pp.imread(images_folder + image_name)

print(np.shape(image))
print(type(image))
print(image.dtype)

pp.imshow(image)
pp.show();
