# 1 დავალება
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

# 2 დავალება
# How good are you really?
def better_than_average(class_points, your_points):
    average_score = sum(class_points) / len(class_points)
    
    return your_points > average_score

# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    
    count_positives = 0
    sum_negatives = 0

    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]


arr = [1, 2, 3, -4, -5, 0]
result = count_positives_sum_negatives(arr)
print(result)  

# DNA to RNA Conversion 
def dna_to_rna(dna):
    return dna.replace('T', 'U')

dna_string = "GCAT"
rna_string = dna_to_rna(dna_string)
print(rna_string) 

# Will you make it?
def can_reach_pump(distance, miles_per_gallon, gallons_left):
    
    max_distance = miles_per_gallon * gallons_left
    
    
    return max_distance >= distance


distance_to_pump = 50
miles_per_gallon = 25
gallons_left = 2

result = can_reach_pump(distance_to_pump, miles_per_gallon, gallons_left)
print(result)

# Calculate BMI
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"







