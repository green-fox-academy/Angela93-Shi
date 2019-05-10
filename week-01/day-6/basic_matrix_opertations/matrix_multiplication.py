matrix_A=[[1,2,3], [4,5,6]]
matrix_B=[[1,2],[4,5],[1,3]]

def matrix_multiplicate(matrix_A,matrix_B):
    #the new matrix row and col
    res_row=len(matrix_A)
    res_col=len(matrix_B[0])
    res = [[0] * res_col for i in range(res_row)]   
    #multiplication      
    for i in range(len(matrix_A)):         
        for j in range(len(matrix_B[0])):                
            for k in range(len(matrix_B)):                    
                res[i][j] +=matrix_A[i][k] * matrix_B[k][j]
    return res

print(matrix_multiplicate(matrix_A,matrix_B))


