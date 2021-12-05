# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

# 数据集
p = [[1, 0.3, 2, 1],
     [2, 0.3, 1, 1]]
n = [[1.5, 1.7, 2, 1.5],
     [2, 1.5, 2, 2.5]]
p = np.array(p)
n = np.array(n)


def divide(dist, k, X, Y):
    ans_p = [np.sort(dist(p[0] - X[i], p[1] - Y[i])) for i in range(len(X))]
    ans_n = [np.sort(dist(n[0] - X[i], n[1] - Y[i])) for i in range(len(X))]
    t = [ans_p[i][int((k - 1) / 2)] > ans_n[i][int((k - 1) / 2)] for i in range(len(ans_p))]
    return np.array(t)


def dist1(x, y):  # x为数据点横坐标，y为数据点的纵坐标 欧式距离
    return np.sqrt(np.sum(np.square(x-y)))


def dist2(x, y):
    return sum(map(lambda i, j: abs(i-j), x, y))


def example_dist(x, y):
    return np.max([np.abs(x), np.abs(y)], axis=0)


def plot(dist, k, ax):  # 画图
    N = 200  # 在平面上生成N x N个点
    X = np.linspace(-0, 3, N)  # 生成横坐标
    Y = X  # 生成纵坐标
    X, Y = np.meshgrid(X, Y)  # 生成 N x N个点
    X = X.reshape(1, N * N)[0]  # 将纵坐标化为向量形式
    Y = Y.reshape(1, N * N)[0]  # 将纵坐标化为向量形式
    predict = divide(dist, k, X, Y)  # todo
    ax.contourf(X.reshape(N, N), Y.reshape(N, N), predict.reshape(N, N), cmap=plt.cm.spec, alpha=0.3)
    ax.plot(p[0], p[1], 'rx')
    ax.plot(n[0], n[1], 'bo')
    plt.text(0.5, 2.5, "k="+str(k))

if __name__ == '__main__':
    ax = plt.subplot(111)
    plot(example_dist, 3, ax)
    plt.show()
