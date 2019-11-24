class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        l,r = 0, len(nums)-1
        curr = 0 
        # print(nums)
        # while curr <= r and curr<=len(nums)-1:
            if nums[curr] == 0 :
                nums[l],nums[curr] = nums[curr],nums[l]
                # nums[curr] = 0
                l+=1
                curr+=1
            elif nums[curr] == 2 :
                nums[r],nums[curr] = nums[curr],nums[r]
                 # = 0
                r-=1
            else:
                curr+=1
            # print(nums,l,r,curr)