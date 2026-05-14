def findMaxLength(nums):
    dict = {0: -1} # diff between 0s and 1s / index
    answer = 0
    diff = 0 # difference between 0s and 1s where positive means 1s more than 0s

    for i in range(len(nums)):
        print(i)
        if nums[i] == 1:
            diff = diff + 1
        elif nums[i] == 0:
            diff = diff - 1
        if diff in dict:
            answer = max(answer, i - dict[diff])
        else:
            dict[diff] = i  # saves the index to the count

    return answer

nums = [0, 1]
#nums = [0, 1, 0]
#nums = [0,0,1,0,1,1,0]
#nums = []
print(findMaxLength(nums))