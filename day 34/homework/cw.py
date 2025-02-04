
# upper
# პირველი დავალება
num1 = "level34"
num1_lowercase = num1.upper()
print(num1_lowercase)


# მეორე დავალება
name = input("enter your name: ")
name_lowercase = name.upper()
print(name_lowercase)

# მესამე დავალება
def print_uppercase(strings):
    for string in strings:
        print(string.upper())

strings = ["asda", "rasda"]
print_uppercase(strings)


# lower
# პირველი დავალება
lower_1 = "HOMEWORK"
lower_2 = lower_1.lower()
print(lower_2)


# მეორე დავალება
email_lower = input("enter your email")
email_lower_1 = email_lower.lower()
print(email_lower_1)

# მესამე დავალება
def print_lower(strings):
    for string in strings:
        print(string.lower())

strings = ["CARS", "TOMATO"]
print_lower(strings)



# Capitalize
# პირველი დავალება
word = input("enter word: ")
word_Capitalize = word.Capitalize()
print(word_Capitalize)


# მეორე დავალება
def print_Capitalize(strings):
    for string in strings:
        print(string.Capitalize())

strings = ["cARS", "tOMATO"]
print_Capitalize(strings)
