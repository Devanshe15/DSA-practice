def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    ans = 1
    prev = nums[0]
    cur = 1
    for i in range(1, len(nums)):
        if nums[i] == prev + 1:
            cur += 1
        elif nums[i] != prev:
            cur = 1
        prev = nums[i]
        ans = max(ans, cur)
    return ans


if __name__ == "__main__":
    arr = [100, 200, 1, 2, 3, 4]
    lon = longestConsecutive(arr)
    print("The longest consecutive sequence is", lon)