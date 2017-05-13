from PIL import Image
import numpy as np
from pylab import *
import os

# 图像列表加载
def get_im_list(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpeg')]

# 图像缩放
def im_resize(im, sz):
    pil_im = Image.fromarry(np.uint8(im))
    return np.array(pil_im.resize(sz))

# 直方图均衡化？？？
def hist_equ(im, n=256):
    imhist, m = np.histogram(im.flatten(), n, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = np.interp(im.flatten(), m[:-1], cdf)
    return im2.reshape(im.shape), cdf


if __name__ == '__main__':
    im = np.array(Image.open('./timg.jpeg').convert('L'))
    imx, cdf = hist_equ(im)
    figure(1)
    subplot(121)
    imshow(im)
    gray()
    subplot(122)
    imshow(imx)
    gray()

    figure(2)
    # 累计分布函数
    plot(list(range(256)), cdf, 'r-')
    show()