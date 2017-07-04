#encoding=utf-8
import numpy as np
from numpy.linalg import *

def main():
    lst = [[1,3,5],[2,4,6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
#    np_lst = np.array(lst, type=np.float)
    #行数列数
    print(np_lst.shape)
    #维度
    print(np_lst.ndim)
    print(np_lst.dtype)
    #每个元素的大小
    print(np_lst.itemsize)
    #大小
    print(np_lst.size)

    #2Some Arrays
    print(np.zeros([2, 4]))
    print(np.ones([3, 5]))

    print(np.random.rand(2, 4))
    print(np.random.rand())

    print(np.random.randint(1, 10, 3))

    #标准正态随机数
    print(np.random.randn())

    print(np.random.choice([10, 20, 30]))

    #贝塔分布
    print(np.random.beta(1, 10, 100))

    #Arrays Opes
    #等差数列
    lst = (np.arange(1, 11).reshape(2, 5))
    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))

    lst = np.array([[[1, 2, 3, 4],
                     [4, 5, 6, 7]],
                    [[7, 8, 9, 10],
                     [10, 11, 12, 13]],
                    [[14, 15, 16, 17],
                     [18, 19, 20, 21]]
                   ])
    print(lst.sum(axis=0))
    print(lst.sum(axis=1))
    print(lst.sum(axis=2))
    print(lst.max())

    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print(lst1+lst2)
    print(lst1**2)

    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))

    print(np.concatenate((lst1, lst2), axis=0))
    print(np.vstack((lst1, lst2)))
    print(np.hstack((lst1, lst2)))
    print(np.split(lst1, 4))

    #4 liner
    print(np.eye(3))
    lst = np.array([[1,2],
                    [3,4]])
    print(inv(lst))
    print(lst.transpose())
    print(det(lst))
    print(eig(lst))
    y = np.array([[5.], [7.]])
    print(solve(lst, y))

if __name__ == '__main__':
    main()