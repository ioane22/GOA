# 1 codewars
# Sum of positive
def positive_sum(arr):
    result = 0
    
    for number in arr:
        if number > 0:
            result += number
        
    return result

# 2 codewars
# String repeat
def repeat_str(repeat, string):
    return repeat * string

# 3 codewars
# Remove First and Last Character
def remove_char(s):
    return s[1 : -1]


# 4 codewars
# Square(n) Sum
def square_sum(numbers):
    
    result = 0
    
    for number in numbers:
        result += number ** 2
        
    return result


# 5 codewars
# Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)
