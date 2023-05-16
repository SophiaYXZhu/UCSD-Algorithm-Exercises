def partition(nums, n, subset_sizes, set1, set2, set3):
    if n < 0:
        return False
    if set1 == 0 and set2 == 0 and set3 == 0:
        return True
    key = (set1, set2, set3)
    if key not in list(subset_sizes.keys()):
        set1_found = False
        if set1 - nums[n-1] >= 0:
            set1_found = partition(nums, n-1, subset_sizes, set1 - nums[n-1], set2, set3)
        set2_found = False
        if not set1_found and set2 - nums[n-1] >= 0:
            set2_found = partition(nums, n-1, subset_sizes, set1, set2 - nums[n-1], set3)
        set3_found = False
        if not set1_found and not set2_found and set3 - nums[n-1] >= 0:
            set3_found = partition(nums, n-1, subset_sizes, set1, set2, set3 - nums[n-1])
        subset_sizes[key] = set1_found or set2_found or set3_found
    return subset_sizes[key]

def can_partition3(nums):
    target_sum = sum(nums)//3
    subset_sizes = {}
    return partition(nums, len(nums), subset_sizes, target_sum, target_sum, target_sum, )

n = int(input())
items = [int(i) for i in input().split()]
if n < 3 or sum(items) % 3 != 0:
    print(0)
else:
    print(1 if can_partition3(items) else 0)

# The following can_partition algorithm fails as it cannot take into account of the cases
# when the remaining array nums having removed all elements in subset 1 does not contain a
# subset 2 with sum sum(nums)//3.
# For example, the backtrace algorithm finds the elements [1, 2, 4] from the input 
# nums = [3, 2, 6, 4, 3, 1, 2]. The remaining elements [3, 2, 6, 3] cannot form another subset
# of sum 7.
def can_partition(nums):
    total_sum = sum(nums)
    target_sum = total_sum // 3
    n = len(nums)
    table = [[0] * (n+1) for i in range(target_sum+1)]
    for i in range(1, n+1):
        for w in range(1, target_sum+1):
            table[w][i] = table[w][i-1]
            if nums[i-1] <= w:
                weight = table[w - nums[i-1]][i-1] + nums[i-1]
                if table[w][i] < weight:
                    table[w][i] = weight
    if table[target_sum][n] != target_sum:
        return 0
    # backtrace
    column_idx = n
    row_idx = target_sum
    used_items = [0] * n
    while row_idx >= 0 and column_idx >= 0:
        weight = nums[column_idx-1]
        new_row_idx = row_idx - weight
        if table[new_row_idx][column_idx-1] + weight == table[row_idx][column_idx]:
            row_idx = new_row_idx
            used_items[column_idx-1] = 1
        column_idx -= 1
    i = len(nums)-1
    while i >= 0:
        if used_items[i] == 1:
            nums.pop(i)
        i -= 1
    if len(nums) < 2 or sum(nums) % 2 != 0:
        print(len(nums), sum(nums), nums)
        return 0
    # find subset again
    n = len(nums)
    table = [[0] * (n+1) for i in range(target_sum+1)]
    for i in range(1, n+1):
        for w in range(1, target_sum+1):
            table[w][i] = table[w][i-1]
            if nums[i-1] <= w:
                weight = table[w - nums[i-1]][i-1] + nums[i-1]
                if table[w][i] < weight:
                    table[w][i] = weight
    if table[target_sum][n] != target_sum:
        return 0
    # backtrace again
    column_idx = n
    row_idx = target_sum
    used_items = [0] * n
    while row_idx >= 0 and column_idx >= 0:
        weight = nums[column_idx-1]
        new_row_idx = row_idx - weight
        if table[new_row_idx][column_idx-1] + weight == table[row_idx][column_idx]:
            row_idx = new_row_idx
            used_items[column_idx-1] = 1
        column_idx -= 1
    i = len(nums)-1
    while i >= 0:
        if used_items[i] == 1:
            nums.pop(i)
        i -= 1
    if len(nums) < 1:
        return 0
    return 1