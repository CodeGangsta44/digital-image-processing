from PIL import Image

images_folder = '../images/'
output_folder = '../images/out/manipulation/'

image_name = 'r32.jpg'
resized_image_name = 'r32_resized.jpg'
cropped_image_name = 'r32_cropped.jpg'
rotated_image_name = 'r32_rotated.jpg'

image = Image.open(images_folder + image_name)

image.resize((200, 300)).save(output_folder + resized_image_name)
image.crop((50, 50, 300, 300)).save(output_folder + cropped_image_name)
image.rotate(90).save(output_folder + rotated_image_name)
