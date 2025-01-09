

num1 = int(input("შემოიტანე რიცხვი"))
if num1 > 0:
    print("Biggger than 0")
elif num1 == 0:
    print("0")
else:
    print("smaller than 0")


num1 = int(input("enter number"))
num2 = int(input("enter number"))
if num1 > num2: range1 = range(num2, num1 + 1)
elif num2 > num1: range1 = range(num1, num2 + 1)
else: print("numbers are equal")

for i in range1:  print(i)


score = int(input("enter your score"))

if score >= 90 and score <= 100: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C")
elif score >= 60: print("D")
else: print("F")


num1 = int(input("enter your number"))
num1 = int(input("enter your number"))
if num1 > num2: range1 = range(num2, num1 + 1)
elif num2 >num1: range1 = range(num1, num2 + 1)
else: print("numbers are equal")