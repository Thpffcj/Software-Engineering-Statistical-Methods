#encoding=utf-8
'''
假定一块蛋糕上的葡萄干粒数服从泊松分布，如果想让每块蛋糕上至少有一粒葡萄干的概率大于等于0.98，蛋糕上葡萄干的平均粒数应该是多少？
'''

import sys
import numpy as np
from math import log
from math import e
from scipy.stats import poisson as Pie

class Solution():
	def solve(self):
		x = -round(log(0.02), 0)
		print x
		return x

if __name__ == '__main__':
	s = Solution()
	s.solve()
