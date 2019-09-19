# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        '''
        for i in range(len(array)):
            for j in range(len(array[i])):
                if target == array[i][j]:
                    return True
        return False
        '''

        row_count = len(array)
        column_count = len(array[0])

        i = 0
        j = column_count - 1

        while i < row_count and j >= 0:
            value = array[i][j]
            if target == value:
                return True
            elif target > value:
                i += 1
            else:
                j -= 1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.Find(20,array[3,5,6,7
                        10,12,14,16
                        18,19,20,23
                        25,27,28,30]))