# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # if sequence == []:
        #     return False  # 这里应该为True 因为空树也能是二叉搜索树
        #
        # rootNum = sequence[-1]
        # del sequence[-1]  # 这里将根节点删除
        #
        # index = None
        # for i in range(len(sequence)):
        #     if index == None and sequence[i] > rootNum:
        #         index = i
        #     if index != None and sequence[i] < rootNum:
        #         return False
        #
        #     if sequence[:index] == []:
        #         leftRet = True
        #     else:
        #         leftRet = self.VerifySquenceOfBST(sequence[:index])
        #
        #     if sequence[index:] == []:
        #         rightRet = True
        #     else:
        #         rightRet = self.VerifySquenceOfBST(sequence[index:])
        #
        #     return rightRet and leftRet

        if not sequence:
            return False
        root_i = len(sequence)-1
        while root_i:
            i = 0
            while(sequence[i] < sequence[root_i]):
                i += 1
            while(sequence[i] > sequence[root_i]):
                i += 1
            if i != root_i:
                return False
            root_i -= 1 #这里的作用是退出while循环
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.VerifySquenceOfBST([4,8,6,12,16,14,10]))