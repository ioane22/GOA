#  1 დავალება
# სრული სახელის დაბეწდვა
print("იოანე ბოღრაშვილი")


# 2 დავალება
# საყვარელი ციტატის დაბეჭვდა
print("წრიპა ბიჭი")


# 3 დავალება
# ვარდი არის წითელი
print("Roses are red,")
# იისფერი არის ლურჯი
print("Violets are blue,")
# პიტონი გასაოცარია
print("Python is awesome too!")


# 4 დავალება
# ცვლადი რომელშიც ინახები რიცხვები
num1 = 5
num2 = 7
# ჯამი
print(num1 + num2)


# 5 დავალება
print("*")
print("***")
print("*****")
print("*******")


# 6 დავალება
num_str = "42"

# სტრინგის ინტეჯერად გადაქცევა
num_int = int(num_str)
print(num_int)


# 7 დავალება
float1 = 3.5
float2 = 2.5

# დაუმატეთ ფლაკონები ერთად
result = float1 + float2

# დაბეჭდეთ შედეგი
print(result)


# 8 დავალება
# სტრინგი
string = "Hello"
string_2 = "world"
# მათი  შეერთება
print(string + string_2)


# 9 დავალება
integer_var = 10
string_var = "Hello, world!"
float_var = 3.14

# მონაცემთა ტიპების დაბეჭდვა type() გამოყენებით
print(type(integer_var))  # <class 'int'>
print(type(string_var))   # <class 'str'>
print(type(float_var))    # <class 'float'>


# 10 დავალება  
age = input("Enter your age: ")

# შეყვანის გადაქცევა მთელ რიცხვად
age = int(age)

# დაამატეთ 1 ასაკს მომავალი წლის ასაკის მისაღებად
next_year_age = age + 1

# დავბეჭდოთ შემდეგი წლის ასაკი
print("Next year, you will be", next_year_age)


# 11 დავალება
# სახელის შეყვანა
name = input("enter your name: ")
print(f"გამარჯობა {name}!")



# 12 დავალება
# ასაკის შეყვანა
age = input("რამდენი წლის ხარ?: ")
# შეყვანილი ასაკის ინტეჯერად გადაქცევა
age = int(age)
# შემდეგი წლის ასაკის გაგება
next_year_age = age + 1
# შედეგი წლის ასაკი
print(next_year_age)


# 13 დავალება
# სთხოვეთ მომხმარებელს ორი რიცხვი
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# გადაიყვანე ეს რიცხვები ინტეჯერად
num1 = int(num1)
num2 = int(num2)

# ამ რიცხვების ჯამი
sum_result = num1 + num2

# დაბეჭდეთ შედეგი
print(f"The sum of {num1} and {num2} is {sum_result}.")


# 14 დავალება
# საყვარელი ფერის შეყვანა
favorite_color = input("enter your favorite color: ")
# შედეგის დაბეჭვდა
print(f"შენი საყვარელი ფერია {favorite_color}!")


# 15 დავალება
# შენი სიმაღლის შეყვანა
height = int(input("შეიყვანე შენი სიმაღლე (სმ)"))

# შემოწმება ამ სიმაღლის არის თუ არა 150-ზე მეტი
if height > 150:
# თუ შეყვანილი სიმაღლე იყო 150-ზე მეტი დაბეჭდვას ამას
    print("შენ ხარ მაღალი!")
# და თუ არ იყო 150-ზე მეტი მაშინ დაბეჭდავს ამას
else:
    print("შენ არ ხარ მაღალი!")


# 16 დავალება
# გადათვლა რიცხვების 1-დან 5-მდე
for x in range(1,5):
    print(x)


# 17 დავალება
my_string = "Python"

# გამოიყენეთ for loop სტრიქონის თითოეული ასო ახალ ხაზზე დასაბეჭდად
for x in my_string:
    print(x)


# 18 დავალება
# ცვლადი რომელშიც ინახება 0
result = 0
# 1-დან 10-ამდე რიცხვების გადათვლა
for i in range(1,11):
# მისი ჯამის იმ ცვლადში შენახვა სადაც ინახებოდა 0
    result += i
# შედეგის დაბეჭვდა
print(result)


# 19 დავალება
# განსაზღვრეთ რიცხვი გამრავლების ცხრილისთვის
number = 2

# გამოიყენეთ for loop 2 რიცხვის გამრავლების ცხრილის დასაბეჭდად
for i in range(1, 6):
    print(f"{number} x {i} = {number * i}")


# 20 დავალება
# 2-დან 21-ის ჩათვლით ლუწი რიცხვების გადათვლა
for i in range(2, 21, 2):
# შედეგის დაბეჭვდა
    print(i)

# 21 დავალება
i = 1

# გამოიყენეთ while მარყუჟი 1-დან 5-მდე რიცხვების დასაბეჭდად
while i <= 5:
    print(i)
    i += 1 


# 22 დავალება
# ცვლადები რომელშიც ინახება რიცხვები
total_sum = 0
i = 1
# გამოიყენეთ while მარყუჟი 1-დან 5-მდე რიცხვების ჯამის გამოსათვლელად
while i <= 5:
    total_sum += i
    i += 1
# შედეგის დაბეჭვდა
print(total_sum)


# 23 დავალება
# ცვლადi რომელშიც ინახება რიცხვi
i = 10
# 10-დან 1-მდე რიცხვების თვლა
while i >= 1:
    i -= 1
# შედეგის დაბეჭვდა
print(i)
    

# 24 დავალება
# დაწყების ნომრის ინიცირება
i = 1

# გამოიყენეთ while მარყუჟი ყველა უცნაური რიცხვის დასაბეჭდად 1-დან 10-მდე
while i <= 10:
    if i % 2 != 0:  # შეამოწმეთ არის თუ არა რიცხვი კენტი
        print(i)
    i += 1  # გაზარდეთ რიცხვი 1-ით


# 25 დავალება
# გამოიყენეთ while ციკლი, რათა გააგრძელოთ მომხმარებლის
# შეყვანის მოთხოვნა, სანამ არ აკრიფებენ "გამოსვლას"
while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        print("Exiting the program.")


# 26 დავალება
# 3 ელემენტიანი სია
car = ["mersedes", "bmw", "audi"]
# ამ სიისთვის ფორ ციკლით გადასვლა
for i in car():
# შედეგის დაბეჭვდა
    print(i)


# 27 დავალება
# სია ჩმს შესახებ
my_info = ["ioane", "boghrashvili", "age 10"]
# ამ სიის სიგრძის გაგება
print(my_info(len(my_info)))


# 28 დავალება
# რიცხვების სია
numbers_list = [1, 2, 3, 4, 5]
# პირველ ინდექსე მყოფი ელემენტის დაბეჭვდა
print(number_list[1])


# 29 დავალება
# 3 ელემენტის სია
num = [True, False, "Goa is best"]
# სიაში ელემენტის დამატება
print(num.append(1))


# 30 დავალება
# რიცხვების სია
num_2 = [1, 2, 3, 4, 5, 7]
# სიიდან ელემენტის ამოშლა
print(num.remove(7))


# 31 დავალება
# გამოიყენეთ სიის გააზრება კვადრატების სიის შესაქმნელად
squares = [x**2 for x in range(1, 6)]
# ამობეჭდეთ კვადრატების სია
print(squares)


# 32 დავალება
# სიის გააზრება
print(i for i in range(2, 11) if i %2 == 0)


# 33 დავალება
# რიცხვების სია
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# მხოლოდ კენტების სია
odd_numbers = [i for i in numbers if i %2 != 0 ]
# სედეგის დაბეჭვდა
print(odd_numbers)


# 34 დავალება
strings = ["hello", "world", "python", "is", "great"]
# გამოიყენეთ სიის გააზრება, რომ გადაიყვანოთ
# თითოეული სტრიქონი დიდზე
uppercase_strings = [s.upper() for s in strings]
# მობეჭდეთ დიდი ასოების სია
print(uppercase_strings)


# 35 დავალება
# მოცემულია ნომრების სია
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# გამოიყენეთ სიის გააზრება 2-ზე გაყოფილი რიცხვების კვადრატში
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]

# ამობეჭდეთ კვადრატული ლუწი რიცხვების სია
print(squared_even_numbers)


# 36 დავალება
# მომხმარებლის სახელის შეყვანა
your_name = input("enter your name: ")
print(f"გამარჯობა {your_name}!")


# 37 დავალება
def info(user_list, user_string):
    result = user_list + user_string
    return result


# 38 დავალება
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    


# 39 დავალება
# უნქცია მართკუთხედის ფართობის გამოსათვლელად
def calculate_area(length, width):
    return length * width


# 40 დავალება
def reverse_string(s):
    return s[::-1]


# 41 დავალება
# tuple
my_tuple = (2.5, "hello", 178)
# tuple-ს დაბეჭვდა
print(my_tuple)


# 42 დავალება
# ხილის tuple
fruit_tuple = ("bannana", "apple", "mango", "orange")
print(fruit_tuple[1])


# 43 დავალება
footballer_tuple = ("messi", "ronaldo", "neymar")
print(footballer_tuple.len())


# 44 დავალება
# tuple ფეხბურთელებზე
tuple_1 = ("messi", "ronaldo", "neymar")
# tuple ხილებზე
tuple_2 = ("bannana", "apple", "mango", "orange")
# მათი ჯამის დაბეჭვდაა
print(tuple_1 + tuple_2)


# 45 დავალება
# შექმენით ტიპი რამდენიმე ნივთით
my_tuple = (10, "apple", 3.14, True, "banana")

# შეამოწმეთ, არის თუ არა კონკრეტული ნივთი ტოპში
item_to_check = "apple"

if item_to_check in my_tuple:
    print("Found")
else:
    print("Not found")


# 46 დავალება
my_set = {1, "apple", 78.6}
print(my_set)


# 47 დავალება
# შექმენით სეტი რამდენიმე ელემენტით
my_set = {1, "apple", 3.14, "banana"}

# ელემენტი შესამოწმებლად
element_to_check = "apple"

# ეამოწმეთ არის თუ არა ელემენტი სეტში
if element_to_check in my_set:
    print("Yes")
else:
    print("No")


# 48 დავალება
set_2 = {1, 2, 3, 4, 5, 6}
print(set_2.add(7))


# 49 დავალება
# შექმენით სეტი რამდენიმე ელემენტით
my_set = {1, "apple", 3.14, "banana"}

# მოიღეთ ელემენტი (მაგ., „ვაშლი“) ნაკრებიდან
my_set.remove("apple")

# დაბეჭდეთ განახლებული ნაკრები
print("Updated set:", my_set)


# 50 დავალება
# შექმენით ორი სეტი
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# იპოვეთ ორი სიმრავლის კავშირი |-ის გამოყენებით ოპერატორი
union_set = set1 | set2

# დაბეჭდეთ შედეგი
print(union_set)


# 51 დავალება
my_dict = {
    "name": "იოანე",
    "age": 10
}

# ლექსიკონის ამობეჭდვა
print(my_dict)


# 52 დავალება
dict_2 = {
    "name":"ioane",
    "surname":"boghrashvili"
}

print(dict_2.values())


# 53 დავალება
# შექმენით ლექსიკონი საწყისი გასაღები-მნიშვნელობის წყვილებით
my_dict_2 = {
    "name": "Alice",
    "age": 25
}

# დაამატეთ ახალი გასაღები-მნიშვნელობის წყვილი ლექსიკონში
my_dict_2["city"] = "New York"

# დაბეჭდეთ განახლებული ლექსიკონი
print(my_dict_2)
