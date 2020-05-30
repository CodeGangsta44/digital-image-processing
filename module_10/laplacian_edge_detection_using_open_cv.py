import cv2
from matplotlib import pyplot as pp

images_folder = '../images/'
image_name = 'r32.jpg'

output_folder = '../images/out/edge-detection/'

laplacian_image_name = 'r32_laplacian_open_cv.jpeg'

image = cv2.imread(images_folder + image_name)

laplacian_image = cv2.Laplacian(image, -1)

cv2.imwrite(output_folder + laplacian_image_name, laplacian_image)

pp.imshow(laplacian_image)
pp.show();
