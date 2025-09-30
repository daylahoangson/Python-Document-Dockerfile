# Cú pháp 
dic = {'key1':'value1', 'key2':'value2'}
value1 = dic['key1'] # Lấy giá trị của key1
print (dic['key1']) # value1
print (dic['key2']) # value2

## ví dụ 

person = {
    'first_name': 'Arnold', 
    'last_name': 'Pham',
    'age': 22,
    'country': 'Viet Nam',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Hoang Quoc Viet',
        'zipcode': '10000'
    }
}   
print (person) 
print (person['first_name']) # Arnold
print (person['last_name']) # Pham
print (person['age']) # 22
print (person['country']) # Viet Nam
print (person['is_married']) # False
print (person['skills']) # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print (person['address']) # {'street': 'Hoang Quoc Viet', 'zipcode': '10000'}
print (person['address']['street']) # Hoang Quoc Viet
print (person['address']['zipcode']) # 10000    

dct = {'key1':'value1', 'key2':'value2'}
print (len(dct)) # 2

# ví dụ 

person = {
    'first_name': 'Arnold',
    'last_name': 'Pham',
    'age': 22,
    'country': 'Viet Nam',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Hoang Quoc Viet',
        'zipcode': '10000'
    }
}
print (len(person)) # 7

## Cứ pháp toán tử in 
dct = {'key1':'value1', 'key2':'value2'}
print ('key1' in dct) # True
print ('key3' in dct) # False
 
# ví dụ get()

person = {
    'first_name': 'Arnold',
    'last_name': 'Pham',
    'age': 22,
    'country': 'Viet Nam',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Hoang Quoc Viet',
        'zipcode': '10000'
    }
}
print (person.get('first_name')) # Arnold
print (person.get('age')) # 22
print (person.get('address')) # {'street': 'Hoang Quoc Viet', '
print (person.get('address').get('street')) # Hoang Quoc Viet
print (person.get('address').get('zipcode')) # 10000
print (person.get('country')) # Viet Nam
print (person.get('city')) # None

## Cú pháp sửa items
dct = {'key1':'value1', 'key2':'value2'}
dct['key1'] = 'value3' # Sửa giá trị của key1

#vi dụ
person = {
    'first_name': 'Arnold',
    'last_name': 'Pham',
    'age': 22,
    'country': 'Viet Nam',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Hoang Quoc Viet',
        'zipcode': '10000'
    }
}
person['first_name'] = 'John'
person['age'] = 25
person['country'] = 'Finland'

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dct.pop('key2') # Xóa key2 và giá trị của nó
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dct.popitem() # Xóa phần tử cuối cùng trong dictionary
del dct['key1'] # Xóa key1 và giá trị của nó

preson = {
    'first_name': 'Arnold',
    'last_name': 'Pham',
    'age': 22,
    'country': 'Viet Nam',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {                
        'street': 'Hoang Quoc Viet',
        'zipcode': '10000'
    }
}

preson.pop('is_married') # Xóa key is_married và giá trị của nó
preson.popitem() # Xóa phần tử cuối cùng trong dictionary
del preson['age'] # Xóa key age và giá trị của nó





