# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
import os
import copy

# 打开图片，是PIL格式的图片
pil_im = Image.open('./timg.jpeg')
print(pil_im)

# PIL图片转灰度PIL图像
pil_hd = pil_im.convert('L')
print(pil_hd)

out_file = os.path.join(os.path.curdir + '/new.png')
print(out_file)
# PIL图像持久化，根据文件名智能选择图片编码
pil_hd.save(out_file)

# PIL对象拷贝需要深拷贝
pil_sl = copy.deepcopy(pil_im)
# 从PIL转换为PIL缩略图
pil_sl.thumbnail((128, 128))

# PIL生成裁剪区域
box = (400, 400, 800, 800)
pil_reg = pil_im.crop(box)

# PIL变换尺寸
pil_rs = pil_im.resize((800, 500))

# PIL旋转
pil_rot = pil_im.rotate((45))


pil_rot.show()
