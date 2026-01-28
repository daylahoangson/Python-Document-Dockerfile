## Bài tập 

# 1. Tạo package calculator với các chức năng sau: cộng, trừ, nhân, chia, mũ, căn bậc 2, luỹ thừa.
## Tạo packge sắp xếp list có tham số là cách sắp xếp. Ví dụ 0 là từ lớn đề bé, 1 là từ bé đến lớn.
from Day20.mypackage.arrangement.arrange import sort_list

numbers = [5, 2, 9, 1, 7]

print(sort_list(numbers, 1))  # bé -> lớn
print(sort_list(numbers, 0))  # lớn -> bé
