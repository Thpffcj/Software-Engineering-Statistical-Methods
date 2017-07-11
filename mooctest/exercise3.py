#-*- coding:utf-8 -*-
'''
Input Example
np.array([1.0, 2.0, 1.0])
Input Description
多项式g(x)的一维数组表示
Output Example
np.poly1d([2.0,4.0,1.0,-1.0,1.0,1.0])
Output Description
f(x)*g(x)的poly1d对象
'''

import numpy as np
class Solution():
	def solve(self, A):
		f = np.array([2.0, 0.0, -1.0, 1.0])
		x1 = np.poly1d(f)
		x2 = np.poly1d(A)
		x3 = x1*x2
		print x3


if __name__ == '__main__':
    s = Solution()
    s.solve(np.array([1.0, 2.0, 1.0]))