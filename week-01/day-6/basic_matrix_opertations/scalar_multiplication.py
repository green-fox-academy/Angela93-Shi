num=2
matrix_A=[[1,2,3], [4,5,6], [7,8,9]]

def scalar_matrix(num,matrix_A):
    matrix_B=[]
    for i in range(0,3):
        temp=[]
        for j in range(0,3):
            temp.append(num*matrix_A[i][j])
        matrix_B.append(temp)
    return matrix_B
print(scalar_matrix(num,matrix_A))

