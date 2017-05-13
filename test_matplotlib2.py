# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

im = array(Image.open('./timg.jpeg').convert('L'))

# 创建缓冲区
figure()
# gray以黑白方式显示
gray()
imshow(im)

figure()
gray()

contour(im, origin='image')

axis('equal')
axis('off')

figure()
# hist绘制直方图
# 需要传入一位数组，图片用flatten函数压缩成一维
# 128表示区间数
hist(im.flatten(), 128)
show()