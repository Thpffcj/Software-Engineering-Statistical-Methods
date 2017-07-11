#encoding=utf-8
'''

'''

import numpy as np
import scipy.stats as stats

class Solution():
	def solve(self):
		year2010 = [6
,17.3
,104.3
,101
,120.4

,91.9
,30
,41.9

,23.9
,101.2
,67.7
,48.7
,39.9
,49
,136.6

,117.6
,52.7
,64.9
,101.3
,83.5
,2.1

,58.6
,94.6
,62.4
,41.8
,0.2

,74.2
,40.1
,12.7
,27.8
,51.5


]
		year2014 = [52041
,207793
,176469
,88880
,96190
,130672
,57246
,65987
,172867
,110665
,82021
,41483
,76043
,40756
,81118
,106123
,96222
,21173
,65589
,33045
,1798
,494415
,52040
,70603
,102842
,930
,69103
,72148
,71839
,92369
,74216

]
		n_y2010 = np.array(year2010)
		n_y2014 = np.array(year2014)
		n_y2010 = n_y2010 * 10000
#		print n_y2010
#		print n_y2014
		c = n_y2014 - n_y2010
#		c = c/1000.0
#		print c
		n = len(c)
#		print n
		d = c.mean()
		print d
		s = np.sqrt(c.var() * n / (n - 1))
#		s = c.std()
		print s
		t = d / s * np.sqrt(n)
		de = stats.t.ppf(0.95, n - 1)
		if t <=  -de:
			print [t, 'NO']
			return [t, 'NO']
		else:
			print [t, 'YES']
			return [t, 'YES']

if __name__ == '__main__':
	s = Solution()
	s.solve()