from PIL import Image
import numpy as np
from scipy.ndimage import filters
from pylab import *

im = np.array(Image.open('./timg.jpeg').convert('L'))

# 高斯卷积核
im2 = filters.gaussian_filter(im, 5)

figure(1)
subplot(121)
imshow(im)
gray()

subplot(122)
imshow(im2)
gray()


# sobel滤波器，不可以调整滤波器尺寸
imx = np.zeros(im.shape)
imy = np.zeros(im.shape)

filters.sobel(im, 1, imx)
filters.sobel(im, 0, imy)

figure(2)
subplot(221)
imshow(im)
gray()

subplot(222)
imshow(255 - imx) # 为了让梯度大的地方显示黑色，所以这里作反相操作
gray()

subplot(223)
imshow(255 - imy)
gray()

subplot(224)
imshow(255 - np.uint8(np.sqrt(imx ** 2 + imy ** 2)))
gray()

# 高斯导数滤波器，可以调整滤波器尺寸
imxx = np.zeros(im.shape)
imyy = np.zeros(im.shape)

sigma = 3 # 标准差
filters.gaussian_filter(im, (sigma, sigma), (0, 1), imxx)
filters.gaussian_filter(im, (sigma, sigma), (1, 0), imyy)

figure(3)
subplot(221)
imshow(im)
gray()

subplot(222)
imshow(255 - imxx)
gray()

subplot(223)
imshow(255 - imyy)
gray()

subplot(224)
imshow(255 - np.uint8(np.sqrt(imxx ** 2 + imyy ** 2)))
gray()

show()