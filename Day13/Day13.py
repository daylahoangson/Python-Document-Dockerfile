# cách 1 
language = 'Python'
lst = list (language) # chuyển chuỗi thành list 
print (type(lst))
print (lst) # ['P', 'y', 't', 'h', 'o', 'n']

# cách 2 sử dụng list comprehension
language = 'Python'
lst = [i for i in language]
print (type(lst))
print (lst) # ['P', 'y', 't', 'h', 'o', 'n']

# Tạo số chẵn 
even_number = [i for i in range(21) if i % 2 == 0]
print (even_number) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Lọ các số dương chẵn từ list mới 
number = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
positive_even_number = [i for i in range(21) if i % 2 == 0 and i > 0]
print (positive_even_number) # [2, 4, 6, 8, 10]  

# Cú pháp 
x = lambda param1, param2, param3: param1 +param2 + param2 
print (x(arg1, arg2, arg3))

# Hàm bình thường 
def add_two_nums (a, b):
    return a + b    
print (add_two_nums (5, 10))

# chức năng tương tự nhưng sử dụng lambda 
add_two_nums = lambda a, b:a+b 
print (add_two_nums (5, 10))

square = lambda x : x ** 2
print (square (5) )
cube = lambda x : x ** 3
print (cube (5) )
power = lambda x, n : x ** n
print (power (5, 3) )

