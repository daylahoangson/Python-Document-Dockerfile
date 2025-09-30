## Bài tập 
 ## Level 1

## 1. Tìm độ dài của tập hợp it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length_it_companies = len(it_companies)
print (length_it_companies) # 7

## Thêm 'Twitter' vào it_companies
it_companies.add('Twitter')
print (it_companies) # {'Apple', 'IBM', 'Microsoft', 'Amazon', 'Oracle', 'Google', 'Facebook', 'Twitter'}

## 3. Chèn nhiều công ty CNTT cùng 1 lúc vào tập hợp it_companies
it_companies.update(['Meta', 'Intel', 'AMD'])
print (it_companies) # {'Apple', 'IBM', 'Microsoft', 'Amazon', 'Oracle', 'Google', 'Facebook', 'Twitter', 'Meta', 'Intel', 'AMD

## 4. Xóa một công ty khỏi tập hợp it_companies
it_companies.remove('AMD') # Nếu phần tử không tồn tại sẽ báo lỗi
print (it_companies) # {'Apple', 'IBM', 'Microsoft', 'Amazon', 'Oracle', 'Google', 'Facebook', 'Twitter', 'Meta', 'Intel'}
it_companies.discard('AMD') # Nếu phần tử không tồn tại sẽ không báo lỗi
print (it_companies) # {'Apple', 'IBM', 'Microsoft', 'Amazon', 'Oracle', 'Google', 'Facebook', 'Twitter', 'Meta', 'Intel'}

## 5. Sự khác biệt giữa remove và discard
# remove sẽ báo lỗi nếu phần tử không tồn tại trong tập hợp, còn discard sẽ không báo lỗi

## level 2

## 1. Kết hợp hai tập hợp A và B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union_A_B = A.union(B)
print (union_A_B) # {19, 20, 22, 24, 25, 26, 27, 28}

## 2. Tìm A giao B 
intersection_A_B = A.intersection(B)
print (intersection_A_B) # {19, 20, 22, 24, 25, 26} 

## Tập con của B là gì? kiểm tra tập con đó 
is_subset = A.issubset(B)
print (is_subset) # True
is_subset = B.issubset(A)
print (is_subset) # False

## 4. Tập hợp A và B có rời rạc không 
is_disjoint = A.isdisjoint(B)
print (is_disjoint) # False
is_disjoint = A.isdisjoint({30, 40})
print (is_disjoint) # True

## 5. Nối A với B và B với A 
A_update_B = A.update(B)
print (A) # {19, 20, 22, 24, 25, 26, 27, 28}
B_update_A = B.update(A)
print (B) # {19, 20, 22, 24, 25, 26, 27, 28}

## 6. Tập hợp đới xứng giữa A và B
symmetric_difference_A_B = A.symmetric_difference(B)
print (symmetric_difference_A_B) # {27, 28}
symmetric_difference_B_A = B.symmetric_difference(A)
print (symmetric_difference_B_A) # {27, 28}

## 7. Xóa tất cả các phần tử trong tập hợp A và B
A.clear()
print (A) # set()
B.clear()
print (B) # set()



