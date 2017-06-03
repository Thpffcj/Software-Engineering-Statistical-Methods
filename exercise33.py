#-*- coding:utf-8 -*-
'''
Is there strong evidence of global warming? Let's consider a small scale example, comparing how temperatures have changed is the US from 1968 to 2008.
The daily high temperature reading on January 1 was collected in 1968 and 2008 for 51 randomly selected locations in the continental US. Then the difference
between the two readings (temperature in 2008 - temperature in 1968) was calculated for each of the 51 values was 1.1 degree with a standard deviation of 4.9
degrees. We are interested in determining whether these data provide strong evidence of temperature warming in the continental US.

(1) Is there a relationship between the observations collected in 1968 and 2008? Or are the observations in the two groups independent? Explain
(2) What's the hypothesis for this research?
(3) Check the conditions required to complete this test.
(4) Calculate the freedom, test statistical value and give the conclusion. alpha is 0.05, coding this part
(5) What type of error might we have made?
(6) Based on the results of this hypothesis test, would you expect a confidence interval for the average difference between the temperature measurements from
1968 and 2008 to include 0? Explain | none

有全球变暖的强有力证据吗？我们考虑一个小规模的例子，比较温度如何变化是美国从1968年到2008年1月1日的每日高温读数在1968年和2008年收集在美国大陆51个随机选择的地点。
然后计算两个读数（2008年的温度 - 1968年的温度）之间的差异，其中51个值中的每一个为1.1度，标准偏差为4.9度。我们有兴趣确定这些数据是否提供了美国大陆温度升温的有力证据。

（1）1968年至2008年收集的意见之间是否有关系？还是两组观察中独立的？说明
（2）这项研究的假设是什么？
（3）检查完成本测试所需的条件。
（4）计算自由度，检验统计值，得出结论。 alpha为0.05，编码这部分
（5）我们可能会犯什么类型的错误？
（6）根据这个假设检验的结果，你会期望1968年和2008年的温度测量值之间的平均差异的置信区间为0？解释|没有
[degree-of-freedom-of-distribution, statistical values, conclusion]
'''
from scipy import stats
import math

class Solution():
	def solve(self):
		z = stats.norm()
		average = 1.1
		s = 4.9
		distribution = -round(-z.ppf(0.05), 2)
		values = round((average - 0) / (s / math.sqrt(51)), 2)
		if values<=distribution:
			flag = False
		else:
			flag = True
		list = [distribution, values, flag]
		print list
		return list

if __name__ == '__main__':
	s = Solution()
	s.solve()