
 #二分查找法

def Binarysearch(array,target):

    left = 0
    right = len(array) - 1


    while left <= right :
        mid = (right - left)//2
        if target == array[mid]:
             return mid
        elif target > array[mid] :
             left = mid + 1
        else:
             right = mid -1

    return None

if __name__ == '__main__':
    ret = Binarysearch([1,2,3,4,5,6,7,8],8)
    print(ret)
