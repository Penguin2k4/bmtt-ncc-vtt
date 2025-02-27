def dem_so_lan(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item ]+=1
        else:
            count_dict[item] =1 
    return count_dict
input_str = input("nhập danh sách các từ cách space ,")
word_list = input_str.split()
so_lan = dem_so_lan(word_list)
print("số lần xuất hiên là",so_lan)