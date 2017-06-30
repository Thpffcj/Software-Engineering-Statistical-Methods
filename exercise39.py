#-*- coding:utf-8 -*-
'''
 Rock-paper-scissors is a hand game played by two or more people where players choose to sign either rock, paper or scissors with their hands. For your statistics class
 project, you want to evaluate whether players choose between these three options randomly, or if certain options are favoured above others. You ask two friends to play
 rock-paper-scissors and count the time each option is played. The following table summaries the data:

Rock	Paper	Scissors
43	     21	       35

Use these data to evaluate whether players choose between these three options randomly, or if certain options are favored above others. alpha is 0.05.
摇滚纸剪刀是由两个或更多的人玩的手游戏，玩家们用手来选择摇滚，纸张或剪刀。 对于您的统计类项目，您想评估玩家是否随机选择这三个选项，或者某些选项是否高于其他选项。
你要两个朋友玩摇滚剪刀，并计算每个选项的播放时间。 下表汇总了数据：
'''

from scipy.stats import chi2
import numpy as np

class Solution():
	def solve(self):
		count = [43, 21, 35]
		averge = 0
		for i in count:
			averge = averge+i
		averge = averge/3
		x = 0.0
		for i in range(3):
			x += ((count[i]) ** 2) * 1.0 / (99.0/3)
		x = x - 99
		de = chi2.ppf(0.95, 2)
		print x
		print de
		if x >= de:
			print([round(2, 2), round(x, 2), False])
			#测试用例给的答案统计量是7.51
			return [round(2, 2), round(x, 2), False]
		else:
			print([round(2, 2), round(x, 2), True])
			return [round(2, 2), round(x, 2), True]

if __name__ == '__main__':
    s = Solution()
    s.solve()