n = int(input('Enter a positive integer number of rows in your triangle: '))
if n < 0 or n is float:
    print('Error. Enter a positive integer.')

triangle = []

for i in range(0,n):  #номер строки - i
    row = [1] * (i+1)
    for j in range(1,i): #номер строки - j  (показывает номер элемента в строке); идём от 1 так как на индексе 0 стоит 1
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
    
last_row_str = ' '.join(str(x) for x in triangle[-1])
max_width = len(last_row_str)

for row in triangle:
    row_str = ' '.join(str(x) for x in row)
    print(row_str.center(max_width))