from typing import List
import random


class Solution:

    def quickSort(self, nums: List[int]) -> List[int]:

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        p = self.partition(nums, 0, len(nums) - 1)

        return self.quickSort(nums[:p]) + [nums[p]] + self.quickSort(nums[p + 1:])

    @staticmethod
    def partition(nums, l, r) -> int:
        # select last element as flag
        flag = nums[r]

        # partition by flag
        i = l - 1
        j = l
        while j < r:
            if nums[j] <= flag:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

        nums[i + 1], nums[j] = nums[j], nums[i + 1]

        return i + 1

    def quickSortExtraSpace(self, nums):

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        flag = nums[-1]
        less = []
        greater = []
        for num in nums[:-1]:
            if num <= flag:
                less.append(num)
            else:
                greater.append(num)

        return self.quickSortExtraSpace(less) + [flag] + self.quickSortExtraSpace(greater)

    def randomizedQuickSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        p = self.randomizedPartition(nums, 0, len(nums) - 1)

        return self.randomizedQuickSort(nums[:p]) + [nums[p]] + self.randomizedQuickSort(nums[p + 1:])

    @staticmethod
    def randomizedPartition(nums, l, r) -> int:
        # select flag randomly
        flag_idx = random.randrange(l, r + 1)
        nums[flag_idx], nums[r] = nums[r], nums[flag_idx]
        flag = nums[r]

        # partition by flag
        i = l - 1
        j = l
        while j < r:
            if nums[j] <= flag:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

        nums[i + 1], nums[j] = nums[j], nums[i + 1]

        return i + 1


print(Solution().randomizedQuickSort([5, 1, 1, 2, 0, 0]))
