#-*- coding:utf-8 -*-
'''
Does being part of a support group affect the ability of people to quit smoking? A country health department enrolled 300 smokers in a randomized experiment. 150
participants were assigned to a group that used a nicotine patch and met weekly with a support group; the other 150 received the patch and did not meet with a support
roup. At the end of the study, 40 of the participants in the patch plus support group had quit smoking while only 30 smokers had quit in the other group.
(1) Create a two-way table presenting the results of this study.
(2) Answer each of the following questions under the null hypothesis that being part of a support group does not affect the ability of people to quit smoking, and indicate
 whether the expected values are higher or lower than the observed values.
     * How many subjects in the "patch+support" group would you expect to quit?  coding this part
     * How many subjects in the "patch only" group would you expect to not quit?
作为支持小组的一部分是否影响人们戒烟的能力？ 一个国家卫生部门在一个随机实验中招募了300名吸烟者。150参与者被分配到使用尼古丁补丁并且每周与支持组会议的组别; 另外150人收到补丁
，并没有得到支持。 在研究结束时，补丁加支持小组的40名参加者戒烟，而另外一组只有30名吸烟者戒烟。
（1）创建一个双向表，介绍本研究的结果。
（2）在作为支持小组一部分的零假设下，回答以下每个问题不影响人们戒烟的能力，并指出
  预期值是否高于或低于观测值。
 *您希望退出“补丁+支持”组中有多少科目？ 编码这部分
 *您希望不要退出“仅补丁”组中的几个科目？
'''

#(1)with a support group?   Yes     No      Total
#       Quit                40      30      70
#       Not Quit            110     120     230
#       Total               150     150     300


class Solution():
    def solve(self):
        return 70*150/300

