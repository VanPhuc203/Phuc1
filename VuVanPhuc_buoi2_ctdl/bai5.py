# Array/List Interview Questions – 2
def two_sum(nums,target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement],i]
        num_indices[num] = i

    nums1= [2,7.11.15]
target1 = 9
result1 = two_sum(nums1, target1)
print(f"Example 1: {result1}")