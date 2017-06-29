#-*- coding:utf-8 -*-
'''
 A group of researchers are interested in the possible effects of distracting stimuli during eating, such as an increase or decrease in the amount of food consumption.
 To test this hypothesis, they monitored food intake for a group of 44 patients who were randomised into two equal groups. The treatment group ate lunch while playing
 solitaire, and the control group ate lunch without any added distractions. Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of 45.1
 grams, and patients in the control group ate 27.1 grams of biscuits with a standard deviation of 26.4 grams. Do these data provide convincing evidence that the average
 food intake is different for the patients in the treatment group? Assume the conditions for inference are satisfied.

Null hypothesis is H0: u_t - u_c = 0, alpha is 0.05
一组研究人员对进食期间分心刺激的可能影响感兴趣，例如食物消耗量的增加或减少。 为了测试这个假设，他们监测了一组44名随机分入两组的患者的食物摄入量。 治疗组在玩纸牌时吃午饭，
对照组吃午饭时没有任何分心。 治疗组患者食用了52.1克饼干，标准偏差为45.1克，对照组患者吃了27.1克饼干，标准偏差为26.4克。 这些数据是否提供令人信服的证据表明治疗组患者的平均
食物摄取量不同？ 假设满足推理条件。

空假设为H0：u_t - u_c = 0，alpha为0.05
'''

from scipy.stats import t
import numpy as np

class Solution():
	def solve(self):
		de = t.ppf(0.05, 42)
		s = np.sqrt(21*45.1+21*26.4)/42
		values = (52.1-45.1)/(np.sqrt(s)*np.sqrt(1/22+1/22))
		if(values>de or values<-de):
			return [[round(42,2),round(values,2),False]]
		else:
			return [round(50, 2), round(values, 2), True]


if __name__ == '__main__':
    s = Solution()
    s.solve()
