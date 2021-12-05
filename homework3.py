# coding=utf-8
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 读取Image
img = np.array(Image.open('homework3_test.jpg'))
row_len = 2 * len(img)
col_len = 2 * len(img[0])
img1 = np.zeros((row_len, col_len, 3), dtype=np.uint8)
for i in range(row_len):
    for j in range(col_len):
        yi = len(img[0]) - i - 1
        yj = int(j - 0.5 * i)
        if (yi <0 or yj <0 or yi>= len(img) or yj >= len(img[0])):
            continue
        else:
            img1[i][j] = img[yi][yj]

# 输出
fig1 = plt.figure()
ax = plt.subplot(111)
ax.imshow(img1)
ax.axis('off')
plt.show()

fig1.savefig('homework3_result.jpg')

