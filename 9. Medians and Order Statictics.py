from typing import List
import random


# rSelect, expect time n, worst n^2
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


def rSelect(nums: List[int], k):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    p = randomizedPartition(nums, 0, len(nums) - 1)
    if k == p:
        return nums[p]
    elif k < p:
        return rSelect(nums[:p], k)
    else:
        return rSelect(nums[p + 1:], k - p - 1)


# rSelect from 1~23, sorted(nums)[10] is 11
print(rSelect([5, 3, 1, 4, 2, 8, 7, 10, 9, 6, 15, 17, 13, 19, 12, 11, 14, 16, 18, 20, 21, 22, 23], 10))


# dSelect
def dPartition(nums, l, r) -> int:
    # select median of median as flag
    median_nums = [sorted(nums[i*5:(i+1)*5])[2] for i in range(len(nums)//5)]
    if len(nums) % 5 > 0:
        median_nums.append(sorted(nums[-(len(nums) % 5):])[len(nums) % 5 // 2])
    median_of_median = sorted(median_nums)[len(median_nums)//2]
    flag_idx = nums.index(median_of_median)
    nums[flag_idx], nums[r] = nums[r], nums[flag_idx]
    flag = nums[r]

    # partition by flag
    i = l - 1
    j = l
    while j < r + 1:
        if nums[j] <= flag:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    return i


def dSelect(nums, k):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    p = dPartition(nums, 0, len(nums) - 1)
    if k == p:
        return nums[p]
    elif k < p:
        return dSelect(nums[:p], k)
    else:
        return dSelect(nums[p + 1:], k - p - 1)


# dSelect from 1~23, sorted(nums)[10] is 11
print(dSelect([5, 3, 1, 4, 2, 8, 7, 10, 9, 6, 15, 17, 13, 19, 12, 11, 14, 16, 18, 20, 21, 22, 23], 10))
