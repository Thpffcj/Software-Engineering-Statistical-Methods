#-*- coding:utf-8 -*-
'''
Input Example
['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]
Input Description
一个纪录了水果出售纪录的列表
Output Example
{'pear':1, 'banana':2, 'cherry':2, 'peach':2, 'pineapple':1, 'apple':1}
Output Description
水果出售次数统计结果
'''

class Solution():
	def solve(self, A):
		dict = {}
		for fruit in A:
			if(dict.has_key(fruit)):
				dict[fruit] += 1
			else:
				dict[fruit] = 1
		print dict
		return dict

s = Solution()
s.solve(['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ])