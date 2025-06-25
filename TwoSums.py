class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in d1:
                return [d1[complement],index]
            d1[num] = index



# Here I solved a easy leetcode problem from Grind 75 Challenge

# Problem: Two Sum
# Topics based on: Arrays and Hashmap
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# ==> The solution I wrote uses hashmaps hence has a time complexity of O(n) which is less than O(n2) as we only iterate through the array only ones.

