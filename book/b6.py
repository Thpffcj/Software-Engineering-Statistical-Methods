#encoding=utf-8

import numpy as np
import scipy.stats as stats

class Solution1():
	def solve(self):
		weight = [112.5,102.0,97.8,101.5,102.0,108.8,101.6,108.6,98.4,100.5,115.6,102.2,105.0,93.3,102.6,100.0,116.6,136.8,101.0,107.5,123.5,95.4,102.8,103.0,95.0]
		n = 25
		s2 = 10**2
		lst = np.array(weight)
		ave = lst.mean()
		z = stats.norm.ppf(0.975)
		print z
		high = ave + np.sqrt(s2)/np.sqrt(n)*z
		low = ave - np.sqrt(s2) / np.sqrt(n) * z
		print [low, high]
		return [low, high]

class Solution2():
	def solve(self):
		n = 16
		ave = 503.75
		s = 6.2022
		de = stats.t.ppf(0.975, 15)
		high = ave + s/np.sqrt(n)*de
		low = ave - s / np.sqrt(n) * de
		print [low, high]
		return [low, high]

class Solution3():
	def solve(self):
		weight = [112.5, 102.0, 97.8, 101.5, 102.0, 108.8, 101.6, 108.6, 98.4, 100.5, 115.6, 102.2, 105.0, 93.3, 102.6,
				  100.0, 116.6, 136.8, 101.0, 107.5, 123.5, 95.4, 102.8, 103.0, 95.0]
		n = 25
		lst = np.array(weight)
		m = lst.mean()

		s = 0.0
		for i in lst:
			s = s + (i - m)**2
		s = s/(n-1)
		s = np.sqrt(s)
#		print s

		s1 = lst.std()
		s1 = s1*s1*n/(n-1)
		s1 = np.sqrt(s1)
#		print s1

		de1 = stats.chi2.ppf(0.025, 24)
		de2 = stats.chi2.ppf(0.975, 24)
		print de1
		print de2
		low = (n-1)*s*s/de2
		high = (n-1)*s*s/de1
		print [low, high]
		return [low, high]

class Solution4():
	def solve(self):
		n1 = 10
		ave1 = 500
		s1 = 1.10
		n2 = 20
		ave2 = 496
		s2 = 1.20
		t = stats.t.ppf(0.975, 28)
		sw = np.sqrt(((n1-1)*s1*s1 + (n2-1)*s2*s2) / (n1+n2-2))
		print sw
		low = ave1 - ave2 - t*sw*np.sqrt(1.0/n1+1.0/n2)
		high = ave1 - ave2 + t * sw * np.sqrt(1.0 / n1 + 1.0 / n2)
		print np.sqrt(1.0/n1+1.0/n2)
		print [low, high]
		return [low, high]

class Solution5():
	def solve(self):
		n1 = 46
		ave1 = 86
		s1 = 5.8
		n2 = 33
		ave2 = 78
		s2 = 7.2
		s = np.sqrt(s1**2/n1 + s2**2/n2)
		z = stats.norm.ppf(0.975)
		low = ave1 - ave2 - z*s
		high = ave1 - ave2 + z*s
		print [low, high]
		return [low, high]

class Solution6():
	def solve(self):
		n1 = 18
		s12 = 0.34**2
		n2 = 13
		s22 = 0.29**2
		f1 = stats.f.ppf(0.95, n1-1, n2-1)
		print f1
		f2 = stats.f.ppf(0.05, n1 - 1, n2 - 1)
		print 1.0/2.38
		print f2
		low = s12/s22/f1
		high = s12 / s22 / f2
		print [low, high]
		return [low, high]

class Solution7():
	def solve(self):
		n = 100
		ave = 0.6
		z = stats.norm.ppf(0.975)
		a = n + z*z
		b = -(2.0*n*ave + z*z)
		c = n*ave*ave
		print a, b, c
		low = (-b - np.sqrt(b**2 - 4.0*a*c)) / (2.0*a)
		high = (-b + np.sqrt(b ** 2 - 4.0 * a * c)) / (2.0 * a)
		print [low, high]
		return [low, high]

if __name__ == '__main__':
	s = Solution7()
	s.solve()