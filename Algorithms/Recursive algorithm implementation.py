def findMaxLength(nums: list[int]) -> int:
    first_seen = {0: -1} # diff between 0s and 1s / index

    def helper(index: int, prefix_sum: int, max_len: int) -> int:
        if index == len(nums):
            return max_len

        # Update prefix sum
        prefix_sum += 1 if nums[index] == 1 else -1

        if prefix_sum in first_seen:
            length = index - first_seen[prefix_sum]
            max_len = max(max_len, length)

        else: # adds to hashmap if first seen
            first_seen[prefix_sum] = index

        return helper(index + 1, prefix_sum, max_len) # increase index by 1 recursively

    return helper(0, 0, 0)

nums = [0, 1]
#nums = [0, 1, 0]
#nums = [0,0,1,0,1,1,0]
#nums = []
print(findMaxLength(nums))