# Beginner Series #2 Clock
def past(h, m, s):
    new_h = 3600
    new_m = 60
    res = (new_h + new_m + s) * 1000
    return res

# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

# Simple multiplication
def simple_multiplication(number):
    if number%2 == 0:
        return number*8
    return number*9

# Abbreviate a Two Word Name
def abbrev_name(name):
    return name[0].upper() + "." + name.split(" ")[1][0].upper()

# A Needle in the Haystack
def find_needle(haystack):
    res = haystack.index("needle")
    return "found the needle at position " + str(res)

# invert values
def invert(lst):
    res = []

    for i in lst:
        res.append(i*-1)

    return res

# Calculate average
def find_average(numbers):
    if len(numbers) == 0: return 0
    return sum(numbers) / len(numbers)


# Beginner - Reduce but Grow
def grow(arr):
    prod = 1
    for i in arr:
        prod = prod * i

    return prod

# 1 საკლასო
def hero(bullets, dragons):
    return bullets >= dragons * 2