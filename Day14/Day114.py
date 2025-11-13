# Decorators

#Hàm decorators bình thường 
def greeting ():
    return 'Well come to Python decorators'
def uppercase_decorator (function):
    def wrapper ():
        func = function ()
        make_uppercase = func.upper ()
        return make_uppercase 
    return wrapper 
g = uppercase_decorator (greeting)
print (g()) # 'WELL COME TO PYTHON DECORATORS'

# Cũng là decorators
def uppercase_decorator (function): 
    def wrapper ():
        func = function ()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Thay vì gán biến bạn chỉ cần ghi tất bằng dấu @ kèm tên của hàm decorators function phía trên function đang được decorate

@uppercase_decorator
def greeting ():
    return 'Well come to Python decorators'
print (greeting()) # 'WELL COME TO PYTHON DECORATORS'

# Decorator đầu tiên 
def uppercase_decorator (function):
    def wrapper():
        func = function ()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Decorator thứ 2. 

def split_string_decorator(function):
    def wrapper (): 
        func = function ()
        splitted_string = func.split()
        return splitted_string 
    return wrapper

# Thứ tự decorator cũng rất quan trọng, mình để split ở trên uppercase thì hàm upper() không hoạt động với list
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Well come to Python decorators'
print (greeting()) # ['WELL', 'COME', 'TO', 'PYTHON', 'DECORATORS']

# Hàm map 

# Cú pháp 
map (function, iterable)

# ví dụ 1
numbers = [1,2,3,4,5] #iterable
def square (x) : 
    return x ** 2
number_squared = map(square, numbers)
print (list(number_squared)) # [1,  4, 9, 16, 25]
# Áp dụng với hàm lambda 
numbers_squared = map (lambda x : x ** 2, numbers)
print (list(numbers_squared)) # [1, 4, 9, 16, 25]

# ví dụ 2 : in hoa các phần tử 

names = ['arnold', 'phạm', 'john', 'doe']
def change_to_uppercase (name):
    return name.upper()
names_uppercase = map (change_to_uppercase, names)
print (list (names_uppercase)) # ['ARNOLD', 'PHẠM', 'JOHN', 'DOE']
# Áp dụng với hàm lambda
names_uppercase = map (lambda name : name.upper(), names)
print (list (names_uppercase)) # ['ARNOLD', 'PHẠM', 'JOHN', 'DOE']  

# Cú pháp 
filter(function, iterable)

# ví dụ 1 : lọc các số chẵn 
numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even (num):
    if num % 2 == 0 :
        return True
    return False

event_number = filter (is_even, numbers)
print (list (event_number)) # [2, 4, 6, 8, 10]
# Áp dụng với hàm lambda
even_number = filter (lambda num : num % 2 == 0, numbers)
print (list (even_number)) # [2, 4, 6, 8, 10]

# ví dụ 2 : lọc tên dài ( nhiều hơn 4 ký tự)
names = ['arnold', 'phạm', 'john', 'doe', 'christina', 'eva']
def is_name_long (name):
    if len (name) > 4 :
        return True
    return False
long_names = filter (is_name_long, names)
print (list (long_names)) # ['arnold', 'christina']
# Áp dụng với hàm lambda
long_names = filter (lambda name : len(name) > 4, names)
print (list (long_names)) # ['arnold', 'christina']

