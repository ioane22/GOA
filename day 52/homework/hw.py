# 1 დავალება
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

# 2 დავალება
# Transportation on vacation
def rental_car_cost(d):
    daily_rate = 40  
    discount_7_or_more = 50  
    discount_3_or_more = 20  
    
    total_cost = daily_rate * d

    
    if d >= 7:
        total_cost -= discount_7_or_more
    elif d >= 3:
        total_cost -= discount_3_or_more

    return total_cost

# Quarter of the year
def quarter_of(month):
    if 1 <= month <= 3:
        return 1 
    elif 4 <= month <= 6:
        return 2  
    elif 7 <= month <= 9:
        return 3  
    elif 10 <= month <= 12:
        return 4  


month = int(input("Enter a month number (1-12): "))
quarter = get_quarter(month)
print(f"Month {month} is in quarter {quarter}.")


# Remove exclamation marks
def remove_exclamation_marks(s):
    return s.replace('!', '')

# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# Total amount of points
def points(games):
    total_points = 0
    
    for match in games:
        x, y = map(int, games.split(":"))  
        
        if x > y:
            total_points += 3  

# Jenny's secret message
def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"


# Area or Perimeter
def area_or_perimeter(l , w):
    if length == width:
        return length * width
    else:
        return 2 * (length + width)

