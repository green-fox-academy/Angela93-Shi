matrix_A=[[1,2,3], [4,5,6], [7,8,9]]
def transport_matrix(matrix_A):
    matrix_B=[]
    for i in range(0,3):
        temp=[]
        for j in range(0,3):
            temp.append(matrix_A[j][i])
        matrix_B.append(temp)
    return matrix_B
print(transport_matrix(matrix_A))