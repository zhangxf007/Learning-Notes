'''
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
'''

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat = sum(nums, [])
        result = []
        if len(nums) * len(nums[0]) != r * c:
            return nums
        for i in range(0, len(flat), c):
            result.append(flat[i: i+c])
        return result
