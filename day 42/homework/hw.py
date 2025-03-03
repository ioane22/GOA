
# 1 დავალება
def sum_even(x, y):
    return x + y

# აუცილებლად ლუწი რიცხვები დაწერე!
total = sum_even(4, 4)
print(total)


# 2 დავალება
def sum_odd(d, b):
    return d + b

# აუცილებლად კენტი რიცხვები დაწერე!
d_b_sum = sum_odd(7, 9)
print(d_b_sum)

# 3 დავალება

def greet(even_arr):
    x = []
    y = []
    for i in even_arr:
        if i %2 == 0:
            x.append(i) 
        else:
            y.append(i)
    num = sum(x)
    num1 = sum(y)
    num2 = num1 * num2
    return num2



# 4 დავალება
# ჰეიჩტიემელის დავალება

# 5 დავალება
# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

# 6 დავალება
# Remove String Spaces
def no_space(x):    
    return x.replace(" ", "")

# 7 დავალება
# Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"
