#-*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''


class Solution():
    def solve(self, A):
        dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for src in A:
            for letter in src:
                dict[int(letter)] += 1
        print dict
        return dict

if __name__ == '__main__':
    s = Solution()
    s.solve(['12','34','567', '36','809','120'])