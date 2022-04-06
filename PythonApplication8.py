matrix = [[100, 360, 520],
          [33, 24, 88],
          [66, 76, 99]]
for j in range (3):
    if matrix [j][0]<matrix[j][1]:
        min = matrix[j][0]
    else :
        min = matrix[j][1]
    if matrix[j][2] < min:
        min = matrix[j][2]
    b = (matrix[j].index(min))
    if matrix[j][b] >= matrix[0][b] and matrix[j][b] >= matrix[1][b] and matrix[j][b]>=matrix[2][b]:
         print("幸运数字为",matrix[j][b])