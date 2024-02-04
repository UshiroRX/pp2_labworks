def spy_game(nums):
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        elif zero_count >= 2 and num == 7:
            return True
    return False

print(spy_game([1,7,2,0,4,5,0])) #as example => False