#encoding=utf-8
'''

'''

import numpy as np
import scipy.stats as stats

class Solution():
	def solve(self, x, y):
		lx = np.array(x)
		ly = np.array(y)
		if len(lx) == 0:
			return [None,None]
		mx = lx.mean()
		my = ly.mean()
		dx = lx.std()
		dy = ly.std()
		n = 0
		result = 0.0
		for x in lx:
			result = result + (x-mx)*(ly[n]-my)
			n = n + 1
		number = len(lx)
		result = result / len(lx)
		r = result / dx / dy
		print r
		t = r * np.sqrt((number-2.0)/(1.0-r*r))
		print [round(r,6), round(t, 6)]
		return [r, t]


if __name__ == '__main__':
	s = Solution()
	s.solve([1, 2, 3], [1, 3, 3])