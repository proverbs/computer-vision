from scipy.ndimage import measurements, morphology
from PIL import Image
from pylab import *
import numpy as np

im = np.array(Image.open('./timg.jpeg').convert('L'))
im = 1 * (im < 128)

# labels为标记图像，num为分类数目
labels, num = measurements.label(im)
print('number of objects:', num)

figure(1)
subplot(221)
imshow(im)
gray()

subplot(222)
imshow(labels)
gray()

subplot(223)
# 开操作是对0区域进行的
im_open = morphology.binary_opening(im, np.ones((9, 5)), iterations=3)
label_open, num_open = measurements.label(im_open)
imshow(im_open)
gray()

subplot(224)
imshow(label_open)
gray()


show()

