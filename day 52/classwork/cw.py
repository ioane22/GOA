def better_than_average(class_points, your_points):
    mean = sum(class_points) / len(class_points)
    
    if your_points > mean: return True
    return False


def count_positives_sum_negatives(arr):
    if arr == [] or arr == None: return []
    
    count_of_pos = 0
    sum_of_neg = 0
    
    for i in arr:
        if i > 0: count_of_pos += 1
        else: sum_of_neg += i
    
    return [count_of_pos, sum_of_neg]


def dna_to_rna(dna):
    return dna.replace("T", "U")


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump: return True
    return False


def bmi(weight, height):
    res = weight / height ** 2
    
    if res <= 18.5: return "Underweight"
    elif res <= 25.0: return "Normal"
    elif res <= 30.0: return "Overweight"
    return "Obese"


# Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# fake binary
def fake_bin(x):
    num = ""
    
    for i in x:
        new = int(i)
        
        if new < 5:
            num += "0"
        else:
            num += "1"
    
    return num



#  You only need one - Beginner
def check(seq, elem):
    return elem in seq



# Convert a string to an array
def string_to_array(s):
    return s.split(" ")


# count by x
def count_by(x, n):
    res = []
    
    for i in range(1, n+1):
        res.append(x*i)
    
    return res

# Reversed sequence
def reverse_seq(n):
    res = []
    
    for i in range(n, 0, -1):
        res.append(i)
    
    return res

# კარგი მიდგომა
def reverse_seq(n):
    return list(range(n, 0, -1))


# Rock Paper Scissors!
def rps(p1, p2):
    if p1 == p2: return "Draw!"

    if p1 == "scissors":
        if p2 == "rock": return "Player 2 won!"
        else: return "Player 1 won!"
    elif p1 == "rock":
        if p2 == "scissors": return "Player 1 won!"
        else: return "Player 2 won!"
    else:
        if p2 == "scissors": return "Player 2 won!"
        else: return "Player 1 won!"

# If you can't sleep, just count sheep!!
def count_sheep(n):
    res = ""
    for i in range(1,n+1):
        res += f"{i} sheep..."
    return res

# Is n divisible by x and y?
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

# Grasshopper - Grade book
def get_grade(s1, s2, s3):
    number = (s1+s2+s3) / 3
    
    if number >= 90: return 'A'
    elif number >= 80: return 'B'
    elif number >= 70: return 'C'
    elif number >= 60: return 'D'
    return 'F'

# 1 საკლასო
def greet(name, owner):
    if name == owner:
        return "Hello Boss"
    else:
        return "Hello guest"
