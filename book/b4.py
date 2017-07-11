#encoding=utf-8

import numpy as np
import scipy.stats as stats

class Solution1():
	def solve(self):
		rv1 = stats.binom(20, 0.01)
		result1 = 1 - rv1.pmf(0) - rv1.pmf(1)
		print result1
		rv2 = stats.binom(80, 0.01)
		result2 = 1 - rv2.pmf(0) - rv2.pmf(1) - rv2.pmf(2) - rv2.pmf(3)
		print result2

class Solution2():
	def solve(self):
		rv = stats.binom(400, 0.02)
		result = 1 - rv.pmf(0) - rv.pmf(1)
		print result

class Solution3():
	def solve(self):
		rv = stats.poisson(4.5)
		result1 = 1 - rv.pmf(0) - rv.pmf(1)
		print result1
		result2 = rv.pmf(2) / result1
		print result2

if __name__ == '__main__':
	s = Solution3()
	s.solve()