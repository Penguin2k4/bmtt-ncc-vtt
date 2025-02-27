def chiahet_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan,2)
    if so_thap_phan % 5 == 0 :
        return True
    else :
        return False
Chuoi_so =input("nhap chuoi số cách bỏi ,")
list_nhiphan = Chuoi_so.split(',')
so_chia_5_het = [so for so in list_nhiphan if chiahet_5(so)]
if len(so_chia_5_het)> 0:
    result = ','. join (so_chia_5_het)
    print ("các số chia hết 5 là", result)
else :
    print("ko có số nào thõa mãn")
