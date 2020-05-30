from matplotlib import pyplot as pp
from matplotlib import cm
import numpy as np
from skimage import data
from pylab import *

img = data.page()

thres = np.zeros(shape(img)).astype('uint8')
threshold = 127;
thres[img >= threshold] = 255

pp.imshow(thres, cm.gray)
pp.show()
