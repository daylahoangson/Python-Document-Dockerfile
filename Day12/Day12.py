# create file module 
def generate_full_name (firstname, lastname):
    return firstname + ' ' + lastname

# import file main.py 
from random import random
import module   # type: ignore
print (module.generate_full_name('Arnold', 'Phạm')) 

from module import generate_full_name, sum_two_nums, person, gravity # type: ignore
print (generate_full_name ('Arnold', 'Phạm'  ))
print (sum_two_nums (5, 10))
print (person ['name'])
print (gravity) 
mass = 100
weight = mass * gravity
print(weight)
print (person['firstname'])

## Đổi tên hàm 
from module import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g  # type: ignore
print (fullname ('Arnold', 'Phạm'  ))
from module import person as p  # type: ignore
print (p ['name'])
print (p ['age'])
print (p ['gender'])

# import module os 
import os
# Tạo thư mục 
os.mkdir ('newfolder')
# Thay đổi đường dẫn thư mục làm việc hiện tại
os.chdir ('newfolder')
print (os.getcwd())
# Xem đường dẫn thư mục hiện tại 
os.getcwd()
# Xóa thư mục 
os.rmdir()  # type: ignore



