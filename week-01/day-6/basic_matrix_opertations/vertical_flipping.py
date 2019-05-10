matrix_A=[[1,2], [4,5], [7,8]]

def vertical_flipping_matrix(matrix_A):
    res_row=len(matrix_A)
    res_col=len(matrix_A[0])
    res = [[0] * res_col for i in range(res_row)]   
    for i in range(res_row):
        for j in range(res_col):
            res[i][j] = matrix_A[i][res_col-1-j]
    return res
    
print(vertical_flipping_matrix(matrix_A))