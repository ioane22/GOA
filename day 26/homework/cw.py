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

password = "Goa best"
num1 = 0
while True:
    num2 = input("enter your password")

    if num2 == password:
        print("ყოჩაღ შენ გგამოიცანი პაროლი")
        break
    else:
        num1 += 1
        print("არასწორი პაროლი")
        
num3 = input("enter number: ")
num4 = input("enter number: ")
num5 = input("enter number: ")
num6 = max(num3,num4,num5)
print(num6)