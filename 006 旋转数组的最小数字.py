# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        left = 0
        right = len(rotateArray) - 1

        while left <= right:
            mid = (left + right) // 2
            if rotateArray[mid] < rotateArray[mid - 1]:
                return rotateArray[mid]
            elif rotateArray[mid] < rotateArray[right]:
                right = mid - 1
            else:
                left = mid + 1

        return 0