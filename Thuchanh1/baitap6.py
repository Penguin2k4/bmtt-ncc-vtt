input_str = input("nhap x,y")
dimensions = [int (x) for x in input_str.split(',')]
rowMun = dimensions[0]
colMun = dimensions[1]
multilist=[[0 for col in range (colMun)]for now in range(rowMun)]
for row in range(rowMun):
    for col in range(colMun):
        multilist [row][col]= row*col
print (multilist)