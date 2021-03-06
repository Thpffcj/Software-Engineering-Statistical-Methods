#encoding=utf-8
'''

'''

import numpy as np
import scipy.stats as stats

class Solution():
	def solve(self):
		age16 = [1672749
,992504
,5759327
,2810549
,1948123
,3713575
,2209254
,3000940
,2040875
,6482159
,4611756
,4211557
,2880394
,3242397
,7688407
,7124733
,4391940
,4920101
,7852679
,3301266
,640690
,2107266
,6598501
,2404526
,3438510
,195270
,3012481
,2077912
,411514
,467146
,1608023
]
		total = [1849475
,1127589
,7037620
,3477805
,2310941
,4252076
,2551123
,3465051
,2253525
,7577122
,5400348
,5312628
,3477491
,4251692
,9272503
,9224288
,5226904
,6096586
,9676589
,4362551
,826560
,2609882
,8161604
,3332265
,4467537
,265904
,3614887
,2623094
,535412
,611957
,2086576
]
		work = [977387
,550787
,4004477
,1729275
,1285021
,2345361
,1429001
,1868107
,1251461
,4486706
,3280387
,2897236
,1950006
,2251205
,5694220
,5006277
,3035863
,3389354
,5525078
,2447946
,426823
,1374581
,4688003
,1676240
,2668421
,147821
,1996061
,1414319
,290469
,327094
,1133002
]
		unwork = [43068
,31049
,90409
,72118
,35983
,92261
,51028
,71929
,57230
,104882
,105231
,65015
,55129
,54102
,109212
,147342
,90522
,109910
,215847
,82808
,23753
,49750
,113674
,46877
,41751
,1460
,62746
,48069
,6521
,7838
,30798
]
		wtotal = [1020455
,581836
,4094886
,1801393
,1321004
,2437622
,1480029
,1940036
,1308691
,4591588
,3385618
,2962251
,2005135
,2305307
,5803432
,5153619
,3126385
,3499264
,5740925
,2530754
,450576
,1424331
,4801677
,1723117
,2710172
,149281
,2058807
,1462388
,296990
,334932
,1163800
]

		lage16 = np.array(age16)
		ltotal = np.array(total)
		lage16 = lage16 * 100
		rate = []
		m = 0
		for i in lage16:
			rate.append(i/float(ltotal[m]))
			m = m + 1
		lrate = np.array(rate)
#		print lrate
		n = len(rate)
		m = lrate.mean()
		s = np.sqrt(lrate.var()*n/(n-1))
#		s = lrate.std()
		de = stats.t.ppf(0.95, n-1)
		low = m - s/np.sqrt(n)*de
		high = m + s / np.sqrt(n) * de

		lwork = np.array(work)
		lunwork = np.array(unwork)
		lwtotal = np.array(wtotal)
		wrate = []
		uwrate = []
		m = 0
		for i in lwork:
			wrate.append(i / float(lwtotal[m]))
			m = m + 1
		m = 0
		for i in lunwork:
			uwrate.append(i / float(lwtotal[m]))
			m = m + 1
		lwrate = np.array(wrate)
		luwrate = np.array(uwrate)
#		print lwrate
		s1 = lwrate.var()*n/(n-1)
		s2 = luwrate.var()*n/(n-1)
		f1 = stats.f.ppf(0.95, n-1, n-1)
		f2 = stats.f.ppf(0.05, n-1, n-1)
		slow = s1/s2/f1
		shigh = s1/s2/f2
		print [[low, high], [slow, shigh]]
		return [[low, high], [slow, shigh]]

if __name__ == '__main__':
	s = Solution()
	s.solve()