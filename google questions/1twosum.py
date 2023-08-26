
#question link - https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        ans = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                elif nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)

        return ans
