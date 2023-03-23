from typing import List
def maxSubArray(nums: List[int], subarray: List[int]) -> int:
    max_sum = -float('inf')
    n = len(nums)
    if n == 1:
        return nums[0]
    i, j = 0, 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += nums[k]
            if sum > max_sum:
                subarray.clear()
                max_sum = sum
                subarray.append(i)
                subarray.append(j)
    return max_sum




if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    subarray = []
    lon = maxSubArray(arr, subarray)
    print("The longest subarray with maximum sum is", lon)
    print("The subarray is")
    for i in range(subarray[0], subarray[1] + 1):
        print(arr[i], end=" ")
    print()