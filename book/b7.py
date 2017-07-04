#encoding=utf-8

import numpy as np
import scipy.stats as stats

class Solution1():
	def solve(self):
		value = [1.26, 1.19, 1.31, 0.97, 1.81, 1.13, 0.96, 1.06, 1.00, 0.94, 0.98, 1.10, 1.12, 1.03, 1.16, 1.12, 1.12, 0.95, 1.02, 1.13, 1.23, 0.74, 1.50, 0.50, 0.59, 0.99,
				 1.45, 1.24, 1.01, 2.03, 1.98, 1.97, 0.91, 1.22, 1.06, 1.11, 1.54, 1.08, 1.10, 1.64, 1.70, 2.37, 1.38, 1.60, 1.26, 1.17, 1.12, 1.23, 0.82, 0.86]
		u = 1.35
		#H0 误差上升u>=u0
		lst = np.array(value)
		m = lst.mean()
#		m = 1.3152
		print m
		n = len(value)
		print n
		s = np.sqrt(lst.std()**2*n/(n-1))
		print s
		result = (m-u)/s*np.sqrt(n)
		print result
		de = stats.norm.ppf(0.99)
		if result <= -de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution2():
	def solve(self):
		old = [78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3]
		new = [79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1]
		s12 = 3.0
		s22 = 2.0
		#H0 没有提高 u1-u2>0
		n1 = len(old)
		n2 = len(new)
		lold = np.array(old)
		lnew = np.array(new)
		mo = lold.mean()
		mn = lnew.mean()
		result = (mo-mn) / np.sqrt(s12/n1 + s22/n2)
		print result
		de = stats.norm.ppf(0.95)
		if result <= -de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution3():
	def solve(self):
		c2 = 5000.0
		n = 26.0
		s2 = 9200.0
		result = (n-1)*s2/c2
		de1 = stats.chi2.ppf(0.01, n-1)
		de2 = stats.chi2.ppf(0.99, n-1)
		print de1, de2
		if result <= de1 or result >= de2:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution4():
	def solve(self):
		time = [159, 280, 101, 212, 224, 379, 179, 264, 222, 362, 168, 250, 149, 260, 485, 170]
		n = 16.0
		lst = np.array(time)
		m = lst.mean()
		print m
		s = np.sqrt(lst.std()**2*n/(n-1))
		print s
		result = (m-225)/s*np.sqrt(n)
		de = stats.t.ppf(0.95, 15)
		print de
		if result >= de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution5():
	def solve(self):
		old = [78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3]
		new = [79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1]
		n1 = 10.0
		n2 = 10.0
		lold = np.array(old)
		lnew = np.array(new)
		m1 = lold.mean()
		m2 = lnew.mean()
		s12 = lold.std()**2*n1/(n1-1)
		s22 = lnew.std()**2*n2/(n2-1)
		print s12, s22
		sw = np.sqrt(((n1-1)*s12 + (n2-1)*s22) / (n1+n2-2))
		print sw
		result = (m1-m2)/sw/np.sqrt(1.0/n1+1.0/n2)
		de = stats.t.ppf(0.95, 18)
		if result >= de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution6():
	def solve(self):
		old = [78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3]
		new = [79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1]
		n1 = 10.0
		n2 = 10.0
		lold = np.array(old)
		lnew = np.array(new)
		d = lnew - lold
		print d
		m = d.mean()
		print m
		s = np.sqrt(d.var()*n1/(n1-1))
		print s
		result = m/s*np.sqrt(n1)
		de = stats.t.ppf(0.95, 9)
		if result >= de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

class Solution7():
	def solve(self):
		old = [78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3]
		new = [79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1]
		n1 = 10.0
		n2 = 10.0
		lold = np.array(old)
		lnew = np.array(new)
		s12 = lold.var()*n1/(n1-1)
		s22 = lnew.var()*n2/(n2-1)
		result = s12/s22
		de = stats.f.ppf(0.95, n1-1, n2-1)
		if result >= de:
			print [result, False]
			return [result, False]
		else:
			print [result, True]
			return [result, True]

if __name__ == '__main__':
	s = Solution7()
	s.solve()