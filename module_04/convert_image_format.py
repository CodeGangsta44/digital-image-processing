from PIL import Image
import os

images_folder = '../images/'
output_folder = '../images/out/conversion/'
target_format = 'gif'

images_list = ['s15.jpeg', 'r32.jpg']

for image in images_list:
    result_image = os.path.splitext(image)[0] + '.' + target_format
    Image.open(images_folder + image).save(output_folder + result_image)
