def check_prime (n):
    if n <= 1:
        return False
    for i in range (2,int (n**0.5)+1 ) :
        if n % i == 0:
            return False
        return True
number = int(input("nhập số kiểm tra "))
if check_prime(number):
    print(number,"là só nguyên tố")
else :
    print(number ," k phải số nguyên tố")