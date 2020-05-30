from PIL import Image

image = Image.open('../images/s15.jpeg')

image.show()

output_folder = '../images/out/conversion/'
new_image = image.convert('L')

new_image.show()

new_image.save('../images/out/intro/s15_grayscale.jpeg')
