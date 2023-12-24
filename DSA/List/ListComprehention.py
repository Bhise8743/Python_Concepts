"""

@Author: Omkar Bhise

@Date: 2023-12-07 03:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 03:30:00

@Title :  List Comprehension in Python

"""
l = [1,2,3,4,5]
ls = list(map(int,l))
print(ls)

ls = list(filter(lambda i : i> 2, map(int,l)))
print(ls)

def time_two(i):
    return i*2

ls = [time_two(i) for i in l]
print(ls)

ls = list(map(time_two,l))
print(ls)
"""
num = [1, 2, 3, 4, 5, 6]
ls = [i for i in num if i > 2]
print(ls)

ls = [i for i in num if i > 2 and i % 3 == 0]
print(ls)

ls = [i for i in num if i > 2 if i % 3 == 0]
print(ls)

n = [10, 20, 30, 40, 50]
ls = [(i, j) for i in num if i > 2 if i == 3 for j in n]
print(ls)

ls = [(i, j) for i in num if i > 2 if i == 3 for j in n if j % 20 == 0]
print(ls)

"""
"""
result = [i for i in range(10)]
print(f"Numbers form 0 to 10 : {result}")

even_num = [i*2 for i in range(10)]
print(f"First 10 even numbers {even_num}")

full_name = "bhise omkar balaji"
res = [i.upper() for i in full_name]
res = "".join(res)
print(res)


def time_five(num):
    return num*5


num = [time_five(i) for i in range(10)]
print(num)

num1 = [time_five(i) for i in range(10) if i % 2 != 0]
print(f"Number is  5 times but not divisible by 2 {num1}")

print("Dict data stores and print the name ")
dicts = [{"name":"John"},{"name":"alok"},{"name":"Ravi"}]
name = [i["name"] for i in dicts]
print(f"names in the dictionary {name}")

print("------------------------------------------------------------------")

l = [1,2,3]
num = [i*5 if i == 3 else i for i in l]
print(num)
num1 = [i*5 for i in l if i == 3]
print(num1)

nums = [[i * j for i in range(10)] for j in range(10)]
print(nums)

"""

"""
l = [1,2,3,4]
new_list = list(map(lambda i:i*5 ,l))
print(new_list)
new_list = [i*5 for i in l if i % 2 == 0]
print(new_list)

new_list = tuple(map(lambda i:i*5 if i% 2 ==0 else i,l))
print(new_list)

new_list = list(map(lambda i:i*5 if i% 2 ==0 else i,l))
print(new_list)

new_list = [i*5 if i%2 == 0 and i>5  else i for i in l if i>5]
print(new_list)

ll = list(filter(lambda i:i>2, l))
print(ll)

new_list = list(map(lambda i:i*5 if i==3 else i ,filter(lambda i:i>2,l)))
print(new_list)
res = []
for i in l:
    if i>2:
        res.append(i*5)

print(res)
new_list = [i*5  for i in l if i>2]
print(new_list)
"""
