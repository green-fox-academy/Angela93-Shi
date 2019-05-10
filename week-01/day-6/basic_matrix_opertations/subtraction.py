matrix_A=[[11,22,33], [14,25,46], [17,28,39]]
matrix_B=[[5,12,23], [4,5,6], [7,8,9]]

def subtract_matrix(matrix_A,matrix_B):
    matrix_C=[]
    for i in range(0,3):
        temp=[]
        for j in range(0,3):
            temp.append(matrix_A[i][j]-matrix_B[i][j])
        matrix_C.append(temp)
    return matrix_C
print(subtract_matrix(matrix_A,matrix_B))

