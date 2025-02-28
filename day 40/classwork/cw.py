def greet(name, surname, age, favourite_color, city):
    print(f"my name is {name} my surname is {surname} my age is {age} my favourite_color is {favourite_color}
    and my city is {city}")

    result = greet()
    print(result)


# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Reversed Strings
def solution(string):
    return string[::-1]

# Return Negative
def make_negative( number ):
    if number > 0:
        return number * -1
    else:
        return number

# Opposite number
def opposite(number):
    return number * -1

# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
