
# pirveli davaleba
def calcurator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)

calcurator(56, 78, "+")
calcurator(78, 48, "-")
calcurator(34, 22, "/")

# meore davaleba

def find_minimum(user_list):
    minimum = user_list[0]

    for i in user_list:
        if i > minimum:
            minimum = i

    print(minimum)

find_minimum([54, 765, 5, 78])
find_minimum([54, 765, 5, 78])
find_minimum([54, 765, 5, 78])
find_minimum([54, 765, 5, 78])
find_minimum([54, 765, 5, 78])


# mesame davaleba

def manual_capitlaieze(user_str):
    print(user_str[0].upper() + user_str[1:].lower())

user_info = input("enter string: ")
manual_capitlaieze(user_info)