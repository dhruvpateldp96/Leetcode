class Solution:
#     def subsets(self, nums):
#         res = []
#         self.dfs(sorted(nums), 0, [], res)
#         return res
    
#     def dfs(self, nums, index, path, res):
#         res.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, i+1, path+[nums[i]], res)
           
    def subsets(self, nums):
        subsets = [[]]
        for n in nums:
            subsets += [subset + [n] for subset in subsets]
        return subsets
#     def subsets(self, nums):
#         return reduce(lambda subsets, n: subsets + [s+[n] for s in subsets], nums, [[]])
