## Bài tập
## level 1
# 1. Viết hàm tính diện tích hình tròn: diện tích = π xrx r.
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

# 2. Viết hàm chuyển °C thành °F: °F = (°C x 9/5) + 32.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 3. Viết hàm tính phương trình bậc hai: ax² + bx + c = 0.
import math

def calculate_quadratic(a, b, c):
    if a == 0 : 
        if b == 0: 
            if c == 0: 
                return "Phương trình vô số nghiệm"
            else:  
                return "Phương trình vô nghiệm"
        else:
            return f"Phương trình có một nghiệm: x = {-c/b}"
    delta = b**2 - 4*a*c
    if delta < 0 : 
        return "Phương trình vô nghiệm"
    elif delta == 0 :
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
    else: 
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    
# 4. Viết hàm reverse_list dùng để đảo ngược mảng (sử dụng vòng lặp)
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# level 2
# 1.Viết hàm is_prime để kiểm tra xem một số có phải là số nguyên tố hay không.
def is_prime (n):
    if n <= 1 : 
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return False
    return True

# 2. Viết một hàm kiểm tra xem tất cả các phần tử có phải là duy nhất trong list hay không.
def item_unique (lst):
    return len(lst) == len(set(lst))

# 3. Viết hàm kiểm tra xem biến được cung cấp có phải là biến python hợp lệ không
import keyword
def is_value_variable (var):
    if not isinstance(var, str):
        return False
    if var in keyword.kwlist:
        return False
    if not var.isidentifier():
        return False
    return True
