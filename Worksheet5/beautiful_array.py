# Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's
# in over his head! Can you help George understand Lily's homework so she can hang out with him? Consider an array of n
# distinct integers, arr = [a[0], a[1] ..., a[n - 1]. George can swap any two elements of the array any number of times.
# An array is beautiful if the sum of  among  *|arr[i] - arr[i - 1|*  among 0 < i < n is minimal. Given the array *arr*,
# determine and return the minimum number of swaps that should be performed in order to make the array beautiful.
#
# Example
# arr = [7, 15, 12, 3]
# one minimal array is [3, 7, 12, 15]. To get there George performed the following steps:
# Swap Result
#
#      [7, 15, 12, 3]
#
#  3 7 [3, 15, 12, 7]
#
#  7 15 [3, 7, 12, 15]
# It took  swaps to make the array beautiful. This is minimal among the choices of beautiful arrays possible.
arr = [2, 5, 3, 1]


def lilysHomework(arr):
    beautifulArray = []
    count = 0
    for i in range(len(arr)):
        if arr.index(getSmallestNumber(arr)) != 0:
            count += 1
        beautifulArray.append((getSmallestNumber(arr)))
        arr.remove(getSmallestNumber(arr))
    print(beautifulArray)
    return count


def getSmallestNumber(arr):
    smallestNumber = None
    for i in range(len(arr)):
        for n in range(len(arr)):
            if arr[n] < arr[i]:
                break
            else:
                if n == len(arr) - 1:
                    smallestNumber = arr[i]
                continue
    return smallestNumber


print(lilysHomework(arr))
