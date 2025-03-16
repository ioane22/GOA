# 1 დავალება
tuple1 = (1, True, 39.6, 3, False)
tuple2,tuple3,tuple4 = tuple1[1], tuple1[-1], tuple1[1:4]
print(tuple2,tuple3,tuple4)

# 2 დავალება
tuple2 = (1, 2, 3)
tuple2[0] = 10 
tuple2[3] = 30

# 3 დავალება
tuple3 = (10, 20, 30, 40, 50)
a, b, c, d, e = tuple3
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)

# 4 დავალება
tuple4 = (10, 20, 30, 10, 40, 10, 50)
count_10 = tuple4.count(10)
index_10 = tuple4.index(10)
print(count_10)
print(index_10)

# 5 დავალება
my_set = {10, 20, 30, 40, 50}
my_set.add(60)
my_set.remove(20)

# 6 დავალება
my_list = [10, 20, 20, 30, 40, 10, 50]
my_set = list(set(my_list))