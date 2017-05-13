# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

# PIL转数组
im = array(Image.open('./timg.jpeg'))

# 显示图片
imshow(im)

# 添加标题
title('Plotting: timg.jpeg')

# 关闭坐标
axis('off')

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 绘制点
plot(x, y, 'r*')

#绘制折线
plot(x[:2], y[:2])


# 最终调用，显示窗口
show()