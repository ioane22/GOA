# 1 საკლასო
def check_lowercase(user_str):
    print(user_str == user_str.lower())

text = input("enter sentence: ")
check_lowercase(text)


# 2 საკლასო
def iscapitelized(user_str):
    print(user_str[0].isupper() and user_str[1:].islower())

text = input("enter sentence: ")
iscapitelized(text)


# 3 საკლასო

def manual_isdigit(user_str):
    if user_str.lower():
        print("პატარა შრიფთშია მთლიანად")
    else: print("არ არის მთლიანად პატარა შრიფთში")

text_2 = input("enter sentence: ")
manual_isdigit(text_2)