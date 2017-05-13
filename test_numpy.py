# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
from pylab import *

im = np.array(Image.open('./timg.jpeg').convert('L'))

figure()
gray()
imshow(im)

# 反相，注意numpy数组的操作方法
im2 = 255 - im

figure()
gray()
imshow(im2)
show()

# 从array构造Image对象
pil_im = Image.fromarray(im)
