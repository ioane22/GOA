# 1 ვარიანტი
def find_maximum(arr):
    return max(arr)

print(find_maximum([2, 4, 5, 3, 43, 43232]))

# 2 ვარიანტი
def find_maximum(user_list):
    maximum = user_list[0]

    for i in user_list:
        if i > maximum:
            maximum = i

    print(maximum)

find_maximum([12 ,4, 53, 76, 23])


def sum_x_y(x, y):
    return x + y