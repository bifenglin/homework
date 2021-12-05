#coding=utf-8
import PIL.Image as Image
import matplotlib.pyplot as plt
import numpy as np

path_old = "test.jpg"
img = np.array(Image.open(path_old))
## 旋转参数
theta = 60 / 180 * np.pi
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
center_i = len(img) / 2
center_j = len(img[0]) / 2
imgr = np.zeros_like(img) #前向变换位置的结果
print (len(imgr))
print ('start 1')
for i in range(len(img)):
    for j in range(len(img[0])):
        yi = int(cos_theta * (i - center_i) - sin_theta * (j - center_j) + center_i)
        yj = int(sin_theta * (i - center_i) + cos_theta * (j - center_j) + center_j)
        if yi < 0 or yj < 0 or yi >= len(img) or yj >= len(img[0]):
            continue
        for k in range(3):
            imgr[yi][yj][k] = img[i][j][k]
fig1 = plt.figure()
ax = plt.subplot(111)
ax.imshow(imgr)
ax.axis('off')
plt.show()

imgR = np.zeros_like(img) #后向变换位置的结果
print('start 2')
for i in range(len(img)):
    for j in range(len(img[0])):
        xi = cos_theta * (i - center_i) + sin_theta * (j - center_j) + center_i
        xj = - sin_theta * (i - center_i) + cos_theta * (j - center_j) + center_j
        if xi < 0 or xj < 0 or xi >= len(img) or xj >= len(img[0]):
            continue
        for k in range(3):
            imgR[i][j][k] = img[xi][xj][k]
fig2 = plt.figure()
ax = plt.subplot(111)
ax.imshow(imgR)
ax.axis('off')
plt.show()

fig1.savefig('fig1.jpg')
fig2.savefig('fig2.jpg')
