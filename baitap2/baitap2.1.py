def tong_chan(list):
    tong = 0 
    for num in list :
        if num % 2 == 0 :
            tong += num

    return tong 
list_so = input ("nhap cac số vào cách nhau bởi ,  ")
number = list(map(int,list_so.split(',')))
tong_chan = tong_chan(number)
print ("tổng số chẳn là ",tong_chan)