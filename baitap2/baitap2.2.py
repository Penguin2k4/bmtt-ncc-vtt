def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input ("nhap cac chữ cần đỏa ngược vào cách nhau bởi ,  ")
numbers = list (map(int,input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print ("chuỗi cần đảo ngược là",list_dao_nguoc)