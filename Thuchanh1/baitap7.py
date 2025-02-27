print("nhập các dòng văn bản (nhập 'done 'dể kết thúc)")
lines = []
while True:
    line = input()
    if line.lower()== 'done':
        break
    lines.append(line)
print("các dòng đã nhập in hoa")
for line in lines :
    print(line.upper())