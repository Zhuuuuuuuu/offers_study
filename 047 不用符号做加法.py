# -*- coding:utf-8 -*-
# 方法一：此方法为书上P311方法，但代码无法通过（时间复杂度大）
class Solution:
    def Add(self, num1, num2):
#         # write code here
#         sum = 0
#         carry = 0
#
#         while num2 != 0:
#             sum = num1 ^ num2
#             carry = (num1 & num2) << 1
#             num1 = sum
#             num2 = carry
#
#         return num1

#方法二：
    #return sum1 + sum2


#方法三：
        xor_num = num1 ^ num2
        and_num = (num1 & num2)<< 1

        while and_num != 0:
            tempxor = xor_num ^ and_num
            tempand = (xor_num & and_num) << 1
            tempxor = tempxor & 0xFFFFFFFF     #对于负数的操作
            xor_num = tempxor
            and_num = tempand

        return xor_num if xor_num <= 0x7FFFFFFF else ~ (xor_num ^ 0xFFFFFFFF)
    #~ (xor_num ^ 0xFFFFFFFF)
    #例如 ：如果是 ~x = -(x+1)




if __name__ == '__main__':
    s = Solution()
    print(s.Add(5,18))