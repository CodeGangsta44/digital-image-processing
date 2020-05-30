from PIL import Image
from PIL import ImageFilter
from pylab import *

images_folder = '../images/'
image_name = 's15.jpeg'

output_folder = '../images/out/filtering/'

contour_image_name = 's15_contour.jpeg'
detail_image_name = 's15_detail.jpeg'
edge_enhance_image_name = 's15_edge_enhance.jpeg'
edge_enhance_more_image_name = 's15_edge_enhance_more.jpeg'
emboss_image_name = 's15_emboss.jpeg'
find_edges_image_name = 's15_find_edges.jpeg'
find_edges_more_image_name = 's15_find_edges_more.jpeg'
smooth_image_name = 's15_smooth.jpeg'
smooth_more_image_name = 's15_smooth_more.jpeg'
sharpen_image_name = 's15_sharpen.jpeg'
custom_one_image_name = 's15_custom_one.jpeg'
custom_two_image_name = 's15_custom_two.jpeg'

im0  = Image.open(images_folder + image_name)
figure(figsize =(15,15))

subplot(3, 4, 1)
plt.imshow(im0)
plt.title('ORIGINAL')

subplot(3, 4, 2)
im2 =  im0.filter(ImageFilter.CONTOUR)
im2.save(output_folder + contour_image_name)
plt.imshow(im2)
plt.title('CONTOUR')

subplot(3, 4, 3)
im3 =  im0.filter(ImageFilter.DETAIL)
im3.save(output_folder + detail_image_name)
plt.imshow(im3)
plt.title('DETAIL')

subplot(3, 4, 4)
im4  = im0.filter(ImageFilter.EDGE_ENHANCE)
im4.save(output_folder + edge_enhance_image_name)
plt.imshow(im4)
plt.title('EDGE ENHANCE')

subplot(3, 4, 5)
im5 = im0.filter(ImageFilter.EDGE_ENHANCE_MORE)
im5.save(output_folder + edge_enhance_more_image_name)
plt.imshow(im5)
plt.title('EDGE ENHANCE MORE')

subplot(3, 4, 6)
im6 = im0.filter(ImageFilter.EMBOSS)
im6.save(output_folder + emboss_image_name)
plt.imshow(im6)
plt.title('EMBOSS')

subplot(3, 4, 7)
im7 =  im0.filter(ImageFilter.FIND_EDGES)
im7.save(output_folder + find_edges_image_name)
plt.imshow(im7)
plt.title('FIND EDGES')

subplot(3, 4, 8)
im8 =  im0.filter(ImageFilter.SMOOTH)
im8.save(output_folder + smooth_image_name)
plt.imshow(im8)
plt.title('SMOOTH')

subplot(3, 4, 9)
im9 =  im0.filter(ImageFilter.SMOOTH_MORE)
im9.save(output_folder + smooth_more_image_name)
plt.imshow(im9)
plt.title('SMOOTH MORE')

subplot(3, 4, 10)
im10 = im0.filter(ImageFilter.SHARPEN)
im10.save(output_folder + sharpen_image_name)
plt.imshow(im10)
plt.title('SHARPEN')


#Custom kernels


size = (3, 3)
kernel1  = [1, 1, 1, 1, -1, 1, -1, -1, -1]
ker1 =  ImageFilter.Kernel(size, kernel1, None, offset =0)
subplot(3, 4, 11)
im11  =  im0.filter(ker1)
im11.save(output_folder + custom_one_image_name)
plt.imshow(im11)
plt.title('CUSTOM #1')


kernel2 = [1, 0, -1, 1, 0, -1, 0, 0, -1]
ker2 = ImageFilter.Kernel(size, kernel2, None, offset=0)
subplot(3, 5, 12)
im12 =  im0.filter(ker2)
im12.save(output_folder + custom_two_image_name)
plt.imshow(im12)
plt.title('CUSTOM #2')

plt.show()
