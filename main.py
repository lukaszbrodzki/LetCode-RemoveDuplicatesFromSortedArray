class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        k = len(nums)
        i = 2
        while i < len(nums):
            if nums[i] != '_' and nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.remove(nums[i])
                nums.append('_')
                i -= 1
                k -= 1
            i += 1
        return k


if __name__ == '__main__':
    s = Solution()
    test = [1,1,1,2,2,3]
    print(s.removeDuplicates(test))
