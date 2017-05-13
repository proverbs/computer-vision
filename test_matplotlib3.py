# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *


im = array(Image.open('./timg.jpeg'))
imshow(im)
print('Please click 3 points')

# 获取鼠标在图片中的点击坐标
x = ginput(3)
print('you clicked:', x)
show()