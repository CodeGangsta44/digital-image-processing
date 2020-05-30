import cv2
from matplotlib import pyplot as pp

images_folder = '../images/'
image_name = 'r32.jpg'

output_folder = '../images/out/edge-detection/'

sobel_x_image_name = 'r32_sobel_x_open_cv.jpeg'
sobel_y_image_name = 'r32_sobel_y_open_cv.jpeg'

image = cv2.imread(images_folder + image_name)

sobel_x_image = cv2.Sobel(image, -1, 1, 0, 5)
sobel_y_image = cv2.Sobel(image, -1, 0, 1, 5)

cv2.imwrite(output_folder + sobel_x_image_name, sobel_x_image)
cv2.imwrite(output_folder + sobel_y_image_name, sobel_y_image)
