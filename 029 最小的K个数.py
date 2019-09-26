class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == None:
            return None

        n = len(tinput)
        if k > n:
            return []

        tinput = sorted(tinput)
        return tinput[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.GetLeastNumbers_Solution([12,3,4,6,4,3,2,6],6))