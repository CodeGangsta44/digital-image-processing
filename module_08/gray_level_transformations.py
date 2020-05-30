from PIL import Image
from pylab import *

images_folder = '../images/'
image_name = 'rx7.jpg'

output_folder = '../images/out/grey-level-transformations/'
negative_image_name = 'rx7_negative.jpg'
clamped_image_name = 'rx7_clamped.jpg'
darked_image_name = 'rx7_darked.jpg'

image_array = array(Image.open(images_folder + image_name).convert('L'))

negative_image_array = 255 - image_array
Image.fromarray(negative_image_array).save(output_folder + negative_image_name)

clamped_image_array = (100.0 / 255.0) * image_array + 100
Image.fromarray(clamped_image_array).convert('L').save(output_folder + clamped_image_name)

darked_image_array = 255.0 * (image_array / 255.0) ** 2
Image.fromarray(darked_image_array).convert('L').save(output_folder + darked_image_name)
