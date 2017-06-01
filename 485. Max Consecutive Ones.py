'''
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, tmp = 0, 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                if tmp > result:
                    result = tmp
                tmp = 0
        if tmp > result:
            result = tmp
        return result
