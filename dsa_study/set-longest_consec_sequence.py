def longest_consecutive_sequence(arr):
    arr = sorted(list(set(arr)))
    consecutive_nums = 1
    longest = 0
    for ind, num in enumerate(arr[1:]):
        if num == arr[ind] + 1:
            consecutive_nums += 1
        else:
            longest = max(longest, consecutive_nums)
            consecutive_nums = 1
    longest = max(longest, consecutive_nums)
    return longest



print( longest_consecutive_sequence([1, 2, 3, 4, 5]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""