"""
Ricardo Alfredo Calvo Perez
23/02/2025
Problem: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

import os
os.system('cls')


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the difference between the target and the current number
        # and the index of the current number
        saved_nums = {}
        # Iterate through the list of numbers
        for index, num in enumerate(nums):

            # Check for the difference between the target and the current number
            num_needed = target - num

            # If the difference is in the dictionary, return the index of the difference and the index of the current number
            if num_needed in saved_nums:
                return [saved_nums[num_needed], index]

            # If the difference is not in the dictionary, store the index and value of the current number
            saved_nums[num] = index
        return []

# Tests


test_cases = [
    # nums, target, expected
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 5, 3, 7], 8, [1, 2])
]

solution = Solution()

for i, (nums, target, expected) in enumerate(test_cases):
    result = solution.twoSum(nums, target)
    print(f"Test {i+1}: {'✅ Passed' if result == expected else '❌ Failed'} - Output: {result}, Expected: {expected}")
