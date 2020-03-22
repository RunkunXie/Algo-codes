from typing import List
import random


# counting Sort, time O(n+k) = O(n) when k=O(n)
# countingSort - text book implementation
def countingSort(nums: List[int]) -> List[int]:
    min_num, max_num = min(nums), max(nums)
    aux = [0] * (max_num - min_num + 1)
    ans = [0] * len(nums)

    for num in nums:
        aux[num - min_num] += 1

    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]

    for num in reversed(nums):
        ans[aux[num - min_num] - 1] = num
        aux[num - min_num] -= 1

    return ans


print(countingSort([2, 5, 3, -1, 2, -1, 0, 3]))


# countingSort2 - easier, cannot sort key:value
def countingSort2(nums: List[int]) -> List[int]:
    min_num, max_num = min(nums), max(nums)
    aux = [0] * (max_num - min_num + 1)
    ans = []

    for num in nums:
        aux[num - min_num] += 1

    for i, freq in enumerate(aux):
        while freq > 0:
            ans.append(i + min_num)
            freq -= 1
    return ans


print(countingSort2([2, 5, 3, -1, 2, -1, 0, 3]))


# countingSort for radixSort
def contingSort_radix(keys, nums):
    min_key, max_key = min(keys), max(keys)
    aux = [0] * (max_key - min_key + 1)
    ans = [0] * len(keys)

    for key in keys:
        aux[key - min_key] += 1

    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]

    for i in range(len(keys) - 1, -1, -1):
        ans[aux[keys[i] - min_key] - 1] = nums[i]
        aux[keys[i] - min_key] -= 1

    return ans


# radixSort, time O(d * (n+k)) = O(n) when d is const, k = O(n)
# assume nums has the same numbers of digits
def radixSort(nums: List[int], num_digit: int) -> List[int]:
    for d in range(num_digit):
        keys = [num // 10 ** d % 10 for num in nums]
        nums = contingSort_radix(keys, nums)

    return nums


print(radixSort([123, 543, 672, 124, 685, 124], num_digit=3))


# bucketSort, time O(n)
# assume nums draw from uniform distribution
def bucketSort(nums: List[int], n_bucket: int = 10) -> List[int]:
    aux = {_: [] for _ in range(n_bucket)}
    ans = []

    for num in nums:
        aux[int(num * n_bucket)].append(num)

    for v in aux.values():
        ans += sorted(v)

    return ans


nums_uniform = [random.random() for _ in range(10)]
print(bucketSort(nums_uniform))
