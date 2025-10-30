# Bài tập 

#1. Lọc các số âm và số 0 trong list dưới bằng cách sử dụng List comprehesion. number = [-4, -3, -2, -1, 0, 2, 4, 5, 6, 7]
number = [-4, -3, -2, -1, 0, 2, 4, 5, 6, 7]
positive_number = [i for i in number if i > 0]
print (positive_number) # [2, 4, 5, 6, 7]

# 2. Làm phẳng lits dưới thành list một chiều list_of_lists = [[[1,2,3]], [[4,5,6]], [[7,8,9]] ] output : [1,2,3,4,5,6,7,8,9]
list_of_list = [[[1,2,3]], [[4,5,6]], [[7,8,9]] ]
flat_list = [num for sublist1 in list_of_list for sublist2 in sublist1 for num in sublist2]
print (flat_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Chuyển list dưới thành dictionary
# countries = [l( 'Finland',"Helsinki' )l, [('Sweden',"Stockholm" )], [('Norway',"Oslo" )]
#output:
# [{'country': "FINLAND",'city': "HELSINKI"},
# {'country': "SWEDEN",'city': "STOCKHOLM"},
# {'country': "NORWAY",'city': "OSLO"}]
countries = [ ('Finland',"Helsinki" ), ('Sweden',"Stockholm" ), ('Norway',"Oslo" )]
country_dict = [{'country': country.upper(), 'city': city.upper()} for country, city in countries]
print (country_dict)
