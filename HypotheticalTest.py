#-*- coding:utf-8 -*-
from scipy import stats

if __name__ == '__main__':

	#单样本均值检验ttest
	#获取均值为5，标准差为10，样本容量为50的正态分布样本
	x1 = stats.norm.rvs(loc=5, scale=10, size=50)
	#做均值为5的t检验
	print stats.ttest_1samp(x1, 5.0)
	# 做均值为1的t检验
	print stats.ttest_1samp(x1, 1.0)

	#双样本均值检验ttest
	x2 = stats.norm.rvs(loc=5, scale=1, size=50)
	x3 = stats.norm.rvs(loc=2, scale=10, size=50)
	print stats.ttest_ind(x2, x3)
	#方差不相等
	print stats.ttest_ind(x2, x3, equal_var=False)

	#卡方拟合优度检验
	a = [16, 18, 16, 14, 12, 12]
	b = [16, 16, 16, 16, 16, 8]
	#默认做均匀分布检验
	print stats.chisquare(a)
	print stats.chisquare(a, f_exp=b)

	#秩和检验
	x = stats.norm.rvs(size=20)
	y = stats.norm.rvs(size=20)
	#指数分布
	z = stats.expon.rvs(size=20)
	print stats.ranksums(x, y)
	print stats.ranksums(y, z)

	#KS检验
	n1 = 200
	n2 = 300
	o = stats.norm.rvs(loc=0, scale=1, size=n1)
	p = stats.norm.rvs(loc=0.5, scale=1.5, size=n2)
	q = stats.norm.rvs(loc=0.01, scale=1, size=n2)
	print stats.ks_2samp(o, p)
	print stats.ks_2samp(o, q)

