# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or len(pushV) != len(popV):
            return None

        stack = []
        index = 0

        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1

        ''''if stack == []:
            return True
        else:
            return False
        '''
        return True if stack == [] else False



if __name__ == '__main__':
    s = Solution()
    print(s.IsPopOrder([1,2,3,4,5],[5,4,3,2,1]))
