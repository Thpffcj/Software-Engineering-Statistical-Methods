#-*- coding:utf-8 -*-
'''
Input Example
['123', '232', '4556554', '12123', '3443','1314131']
Input Description
一个包含一系列数字字符串的列表

Output Example
['232', '4556554', '3443','1314131']
Output Description
仅包含回文串的列表
'''

class Solution():
	def solve(self, A):
		list = []
		for src in A:
			if(self.isPalindrome(src)):
				list.append(src)
		print(list)
		return list

	def isPalindrome(self,x):
		index = 0;
		for letter in x:
			if(x[index] != x[-index-1]):
				return False
		return True


s = Solution()
list1 = ['123', '232', '4556554', '12123', '3443','1314131']
s.solve(list1)