def tao_tuple_list (lst):
    return tuple (lst)
input_list= input("nhập sanh sách số cách bở i, ")
numbers = list (map(int,input_list.split(',')))
my_tuple = tao_tuple_list(numbers)
print("list:",numbers)
print("tuple từ list :", my_tuple)