## Bài tập tuple 

## 1. Tạo tuple trống 
empty_tuple = ()
print (empty_tuple) # ()

## 2. Tạo tuple chứa tên của anh chị em bạn
sibling_tuple = ('Trung', 'Hoa', 'Vân')
print (sibling_tuple) # ('Trung', 'Hoa', 'Vân')

## 3. Nối tuple anh chị em và tuple cô dì chú bác 
family_tuple = ('Trung', 'Hoa', 'Vân') + ('Nam', 'Lan', 'Linh')
print (family_tuple) # ('Trung', 'Hoa', 'Vân', 'Nam, 'Lan', 'Linh')

## 4. Đếm tuple anh chị em?
count_sibling = len(sibling_tuple)
print (count_sibling) # 3

## 5. Sửa đổi tuple anh chị em, và thêm tên cha mẹ của bạn và nối vào family_members
sibling_tuple1 = sibling_tuple[:1] + sibling_tuple[2:] # Loại bỏ phần tử thứ hai trong tuple
print (sibling_tuple1) # ('Trung', 'Vân')
family_tuple = sibling_tuple1 + ('Nam', 'Lan', 'Linh') + ('Minh', 'Thủy')
print (family_tuple) # ('Trung', 'Vân', 'Nam', 'Lan', 'Linh', 'Minh', 'Thủy')



## level 2

## 1. unpack anh chị và ba mẹ ra khỏi family_members
sibling1, sibling2, parent1, parent2, parent3, parent4, parent5 = family_tuple
print (sibling1) # Trung
print (sibling2) # Vân
print (parent1) # Nam
print (parent2) # Lan
print (parent3) # Linh
print (parent4) # Minh
print (parent5) # Thủy  

## 2. Tạo tuple trái cây , rau và sản phẩm của động vật 
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yogurt')

## 3. Kết hợp 3 tuple đó và gán nó cho một loại tuple LÀ food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print (food_stuff_tp) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion',


## 4. Chuyểm tup;e food_stuff_tp thành list food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print (food_stuff_lt) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'milk', 'meat', 'butter', 'yogurt']

## 5. Cắt bỏ phần tử giữa, ba mục đầu tiên và ba mục cuối cùng khỏi dnah sách food_stuff_lt
middle_index = len(food_stuff_lt) // 2
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print (first_three) # ['banana', 'orange', 'mango']
print (last_three) # ['butter', 'yogurt']
print (food_stuff_lt) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'milk', 'meat', 'butter', 'yogurt']        
food_stuff_lt = food_stuff_lt[3:middle_index] + food_stuff_lt[middle_index+1:-3]
print (food_stuff_lt) # ['lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'milk', 'meat

## 6. Xóa toàn bộ danh sách food_stuff_tp
food_stuff_tp = ()
print (food_stuff_tp) # ()

## 7. Kiểm tra xem 'Viet Nam' có tồn tại trong countries = ('Finland', 'Sweden', 'Viet Nam', 'Denmark', 'Iceland') không?
countries = ('Finland', 'Sweden', 'Viet Nam', 'Denmark', 'Iceland')
check_vn = 'Viet Nam' in countries
print (check_vn) # True