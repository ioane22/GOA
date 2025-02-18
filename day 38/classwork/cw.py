
# 1 საკალსო
def remove_one_element (goa, gr54):
    goa.pop(gr54)
    print(goa)

remove_one_element([1, 2, 3,], 2)
remove_one_element([1, 2, 3, 4, 5, 6], 2)

# 2 საკალსო
def spuare(user_num):
    return user_num * user_num
result  =  spuare(3)
print(result * 2)

# 3 საკალსო
def rectangle_info(side1, side2):
    perimeter = side1 + side2
    area = side1 * side2
    return perimeter,area
peri,area = rectangle_info(2, 354)
print(peri)
print(area)