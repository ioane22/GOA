# 1 დავალება
def print():
    print("hello world!")

# 2 დავალება
def sum_x_y(x, y):
    return x + y

total = sum_x_y(43, 54)
print(total)


# 3 დავალება
def numbers(num):
    return (num * 10)
result = numbers(11)
print(result)


# 4 დავალება
def hw_4(name):
    return "გამარჯობა", name




# 5 დავალება
def hw_5(x):
    def hw_5_2():
        return "hello", x
    return hw_5_2()

# 6 დავალება
def hw_6(user_str):
    for i in user_str:
        if i %2 == 0:
            print("ლუწი")
        else:
            print("კენტი")

# 7 დავალება
def find_maximum(user_list):
    maximum = user_list[0]

    for i in user_list:
        if i > maximum:
            maximum = i

    print(maximum)

find_maximum([12 ,4, 53, 76, 23])
find_maximum([43 ,7, 1, 22, 23])

# 8 დავალება
def hw_8(user_hw):
    n = []
    for i in user_hw:
        if i > 0:
            n.append(i)
    return n

# 9 დავალება
def hw_9(n, a):
    x = 0
    for i in range(n, a+1):
        if i %3 == 0:
            x += i
    return x






