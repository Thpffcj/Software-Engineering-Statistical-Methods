#encoding=utf-8

import numpy as np
import scipy.stats as stats

class Solution1():
	def solve(self):
		i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
		ni = [1, 5, 16, 17, 26, 11, 9, 9, 2, 1, 2, 1, 0]
		n = 100.0
		l_i = np.array(i)
		l_ni = np.array(ni)
		sum = l_i * l_ni
#		print sum
		m = sum.sum()/n
#		print m
#		print np.math.factorial(3)
		p = []
#		print np.math.exp(1)
#		print np.math.pow(2,3)
		for number in i:
			p.append(np.math.pow(4.2, number)*np.math.pow(np.math.e, -4.2) / np.math.factorial(number))
#		print p
		result = []
		loc = 0
		for number in ni:
			result.append(number**2 /n /p[loc])
			loc = loc + 1
		l_result = np.array(result)
		ka = l_result.sum() - n
#		print ka
		de = stats.chi2.ppf(0.95, 6)
		if ka >= de:
			print [ka, False]
			return [ka, False]
		else:
			print [ka, True]
			return [ka, True]

class Solution3():
	def solve(self):
		table = [[186, 38, 35, 259], [227, 54, 45, 326], [219, 78, 78, 375], [355, 112, 140, 607], [653, 285, 259, 1197], [1640, 567, 557, 2764]]
		lst = np.array(table)
#		print lst
		m = len(table)
#		print m
		n = len(table[0])
#		print n
		num1 = []
		for number in table:
			num1.append(float(number[3]))
#		print num1
		num2 = table[-1]
#		print num2
		the = np.ndarray((5, 3))
		for i in range(m-1):
			for j in range(n-1):
				the[i][j] = num1[i] * num2[j] / num1[-1]
#		print the
		result = 0.0
		for i in range(m-1):
			for j in range(n-1):
				result = result + (lst[i][j]-the[i][j])**2/the[i][j]
		print result
		de = stats.chi2.ppf(0.99, 8)
		print de
		if result >= de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution4():
	def solve(self):
		de = stats.ksone.isf(0.1, 10)
#		de1 = stats.kstwobign.isf(0.1, 10)
		print de

if __name__ == '__main__':
	s = Solution4()
	s.solve()