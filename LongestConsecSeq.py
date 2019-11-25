class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for num in nums:
            # print(num)
            if num - 1 not in nums:
                # print("nahi hai")
                y = num + 1
                while y in nums:
                    y += 1
                best = max(best, y - num)
        return best