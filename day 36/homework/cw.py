
# find
# 1 დავალება

print("stringfloatpython".find("python"))

# 2 დავალება
print("ioane".find("an"))

# 3 დავალება
print("boghrashvili".find("ra"))

# count
# 1 დავალება
print("teyfdthevdthegdthe".count("the"))

# 2 დავალება
num = input("enter sentence: ")
print(num.count("b"))

# 3 დავალება 
input_sentence = input("enter sentence: ")
print(input_sentence.count("io"))

# index
# 1 დავალება
print("ფბჯდგამარჯობისჰს".index("გამარჯობის"))

# 2 დავალება
hw_2_index = input("enter sentence: ")
print(hw_2_index.index("iobo"))

# islower
# 1 დავალება
print("Ioane".islower())

# 2 დავალება
def hw_islower(user_lower):
    if user_lower.lower():
        print("True")
    else: print("False")

text = input("enter sentence: ")
hw_islower(text)

# 3 დავალება
hw_3_lvl_36 = input("enter sentence")
print(hw_3_lvl_36.islower())


# isupper
# 1 დავალება
hw_1_isupper = input("enter sentence: ")
print(hw_1_isupper.isupper())

# 2 დავალება
def hw_2_isupper(x):
    return x.isupper()

# 3 დავალება
hw_3_isupper = input("enter sentence: ")
print(hw_3_isupper.issuper())
