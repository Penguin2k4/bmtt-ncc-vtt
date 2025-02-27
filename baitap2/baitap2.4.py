def truy_cap_so (tuple_data):
    frist_elements = tuple_data[0]
    last_elements = tuple_data[-1]
    return frist_elements,last_elements
input_tuple =eval(input("nhặp tuple :"))
frist,last = truy_cap_so(input_tuple)
print("phần tử đầu",frist)
print("phần tử cuói",last)
