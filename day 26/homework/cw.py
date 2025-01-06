# elif - არის პირობითი განცხადება და მას ვიყენეთ როდესაც გვინდა ერთზე მეტი პირობის შემოწმება







num1 = float(input("შემოიტანე რიცხვი"))
num2 = float(input("შემოიტანე რიცხვი"))
operator = input("აირჩიე ოპერატორი +,-,*,/")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("0-ზე გაყოფა არ შეიძლება")
else:
    print("არასწორი ოპერატორი")