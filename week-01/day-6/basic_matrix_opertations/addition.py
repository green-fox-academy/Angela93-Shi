matrix_A=[[1,2,3], [4,5,6], [7,8,9]]
matrix_B=[[1,2,3], [4,5,6], [7,8,9]]

def add_matrix(matrix_A,matrix_B):
    matrix_C=[]
    for i in range(0,3):
        temp=[]
        for j in range(0,3):
            temp.append(matrix_A[i][j]+matrix_B[i][j])
        matrix_C.append(temp)
    return matrix_C
print(add_matrix(matrix_A,matrix_B))

