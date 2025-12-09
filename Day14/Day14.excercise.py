#Level 1:
# 1. Giải thích sự khác biệt giữa map, filter và reduce.
#    - map: Hàm map áp dụng một hàm cho mỗi phần tử trong một iterable (như danh sách, tuple) và trả về một iterable mới chứa kết quả. Ví dụ, nếu bạn muốn nhân mỗi số trong danh sách với 2, bạn có thể sử dụng map.
#    - filter: Hàm filter lọc các phần tử trong một iterable dựa trên một hàm điều kiện. Nó trả về một iterable mới chỉ chứa các phần tử mà hàm điều kiện trả về True. Ví dụ, nếu bạn muốn lấy tất cả các số chẵn từ một danh sách, bạn có thể sử dụng filter.
#    - reduce: Hàm reduce áp dụng một hàm cho các phần tử trong một iterable và trả về một giá trị duy nhất. Hàm này thường được sử dụng để tính toán tổng, tích hoặc các phép toán tổng quát khác. Ví dụ, nếu bạn muốn tính tổng của tất cả các số trong một danh sách, bạn có thể sử dụng reduce.

# 2. Giải thích sự khác biệt giữa hàm bậc cao, hàm lồng nhau và decorator.
#    - Hàm bậc cao (Higher-order function): Là hàm nhận một hoặc nhiều hàm làm đối số hoặc trả về một hàm làm kết quả. Ví dụ, map, filter và reduce là các hàm bậc cao vì chúng nhận các hàm khác làm đối số.
#    - Hàm lồng nhau (Nested function): Là hàm được định nghĩa bên trong một hàm khác. Hàm lồng nhau có thể truy cập các biến từ hàm bao quanh nó. Ví dụ:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
#    - Decorator: Là một hàm bậc cao được sử dụng để mở rộng chức năng của một hàm mà không thay đổi mã nguồn gốc của nó. Decorator nhận một hàm làm đối số và trả về một hàm mới. Ví dụ:
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper      
# Level 2:
# 1. Tạo một hàm trả về một từ điển, trong đó các khóa là chữ cái bắt đầu của các quốc gia và giá trị là số tên quốc gia bắt đầu bằng chữ cái đó.
def contry_count(contries): 
    country_dict = {}
    for country in contries:
        first_letter = country[0].upper()
        if first_letter in country_dict:
            country_dict[first_letter] += 1
        else:
            country_dict[first_letter] = 1
    return country_dict
# 2. Sử dụng filter để lọc các quốc gia có từ 'land'.
def filter_countries_with_land(countries):
    return list(filter(lambda country: 'land' in country.lower(), countries))
#3. Sử dụng map để thay đổi từng tên thành chữ hoa trong danh sách names.
def capitalize_countries(countries):
    return list(map(lambda country: country.upper(), countries))
# 4. Sử dụng reduce để tính tổng tất cả các số trong danh sách numbers.
from functools import reduce
def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)
