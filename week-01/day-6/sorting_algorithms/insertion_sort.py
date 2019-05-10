#insert sort
def insert_sort(arr):
    for i in range(1,len(L)-1):
        key=arr[i]
        j=i-1
        while j >=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key

L=[1,5,6,3,7,8]
insert_sort(L)
print(L)