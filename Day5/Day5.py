#ví dụ 1
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
lts = fruits
first_fruit, second_fruint, third_fruit, *rest = lts 
print(first_fruit) # banana
print(second_fruint) # orange
print(third_fruit) # mango
print(rest) # ['lemon', 'apple', 'lime']

#ví dụ 2
first, second, third, *rest, tech = [1,2,3,4,5,6,7,8,9,10]
print (first) # 1
print (second) # 2
print (third) # 3
print (rest) # [4, 5, 6, 7, 8
print (tech) # 10

#ví dụ 3

countries = ['VietNam', 'Thailand', 'Indonesia', 'Malaysia', 'Singapore', 'Brunei']
vi, la , kh, cn, *scandic , es = countries
print (vi) # VietNam
print (la) # Thailand
print (kh) # Indonesia
print (cn) # Malaysia
print (scandic) # ['Singapore']
print (es) # Brunei

fruits = ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime', 'watermelon']

all_fruits = fruits[0:4] # Trả về tất cả các phần tử
all_fruits = fruits [0:] # Nếu bạn không chỉ định index kết thúc thì nó sẽ lấy từ vị trí bất đầu đến hết lits 

orange_and_mango = fruits[1:3] # Lấy từ vị trí 1 đến vị trí 3 (không bao gồm vị trí 3)
orange_mango_lemon = fruits[1:] # Lấy từ vị trí 1 đến hết 
orange_mango_lemon = fruits[::2] # Lấy từ vị trí 0 đến hết và nhảy 2 vị trí

all_fruits = fruits[-4:] # Lấy 4 phần tử cuối cùng
orange_and_mango = fruits[-3:-1] # Lấy từ vị trí thứ 3 từ cuối đến vị trí cuối cùng (không bao gồm vị trí cuối cùng)
orange_mango_lemon = fruits[-3:] # Lấy từ vị trí thứ 3 từ cuối đến hết
reverse_fruits = fruits[::-1] # Đảo ngược lits 


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits [0] = 'avocado' # Thay đổi giá trị của phần tử đầu tiên
print (fruits) # ['avocado', 'orange', 'mango', 'le]
fruits [1] = 'kiwi' # Thay đổi giá trị của phần tử thứ hai
print (fruits) # ['avocado', 'kiwi', 'mango', 'lemon']
last_index = len(fruits) - 1 # Lấy vị trí index cuối cùng
fruits [last_index] = 'apple' # Thay đổi giá trị của phần tử cuối cùng
print (fruits) # ['avocado', 'kiwi', 'mango', 'apple']


fruits = ['banana', 'orange', 'mango', 'lemon']
dose_exits = 'banana' in fruits # Kiểm tra phần tử có tồn tại trong lits hay không
print (dose_exits) # True
dose_exits = 'line' in fruits # Kiểm tra phần tử có tồn tại trong lits hay không
print (dose_exits) # False

# cú pháp 

lst = ['item1', 'item2', 'item3' ]

lst.insert('index', 'item') # Chèn một phần tử vào vị trí index
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

# Cú pháp toán tử + 
list1 = ['item1', 'item2']
list2 = ['item3', 'item4']
list3 = list1 + list2
positive_numbers = [1,2,3]
zero = [0]
negative_numbers = [-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print (integers) # [-3, -2, -1, 0,

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print (fruits_and_vegetables) # ['banana', 'orange', 'mango]

# Cú pháp 
lst = ['item1', 'item2', 'item3' ]
lst.sort() # Sắp xếp lits theo thứ tự tăng dần
lst.sort(reverse=True) # Sắp xếp lits theo thứ tự giảm dần

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort() # Sắp xếp lits theo thứ tự tăng dần
print (fruits) # ['banana', 'lemon', 'mango', 'orange

fruits.sort(reverse=True) # Sắp xếp lits theo thứ tự giảm dần
print (fruits) # ['orange', 'mango', 'lemon', 'banana

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort() # Sắp xếp lits theo thứ tự tăng dần
print (ages) # [19, 22, 24, 24, 24

ages.sort(reverse=True) # Sắp xếp lits theo thứ tự giảm dần
print (ages) # [26, 25, 25, 24, 24, 24, 22, 19]










