#quick sort

def quicksort(list,p,r):
    if p<r:
        q=partion(list,p,r)		
        quicksort(list,p,q)		
        quicksort(list,q+1,r)
def partion(list,p,r):	
    i=p-1	
    for j in range(p,r):		
        if list[j]<=list[r]:			
            i+=1			
            list[i],list[j]=list[j],list[i]	
    list[i+1],list[r]=list[r],list[i+1]	
    print(i)
    return i
list1=[2,8,7,1,3,5,6,4]
quicksort(list1,0,len(list1)-1)
print (list1)
