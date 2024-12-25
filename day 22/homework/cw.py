# while მუშაობს - ჯერ შემოწმდება პირობა და თუ ის არის True-ს ტოლი მაშინ გაეშვება ციკლის კოდის ბლოკი. როდესაც კოდის ბლოკის გაშვება მორჩბა, დაიწყებს  ისევე პირობის შმოწმებას. როცა პირობა არის False-ს ტოლი აღარ გაეშვება ციკლის კოდის ბლოკი და ციკლი შეწყდება
# while და for - განსხვავდება იმით რომ for ციკლით უფრო ადვილი დასაწერია ხოლო while უფრო ძნელი

num1 = 0
while num1 < 50:
     print("GOA BEST!!!")
     num1 = num1 + 1

for i in range(50):
     print("GOA BEST!!!")

num2 = 0
while num2 < 10:
     print(num2)
     num2 = num2 + 1

num3 = 2
while num3 < 20:
     print(num3)
     num3 = num3 + 2

num4 = 10
while num4 > 1:
    print(num4)
    num4 = num4 - 1
print("blast off")

num5 = 10
while num5 < 1:
     print(num5)
     num5 = num5 - 1



























