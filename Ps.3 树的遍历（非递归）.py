class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
#非递归实现树的遍历
# 暂时不浪费时间学习,在视频中可以继续学习(树的遍历)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t1.left = t2
    t1.right= t3
    t2.left = t4
    t2.right= t5
    t3.left = t6
    t3.right= t7
    t6.right= t8