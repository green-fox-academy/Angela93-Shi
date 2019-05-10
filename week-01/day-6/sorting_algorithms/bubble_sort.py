#bubble sort

a=[12,45,2,5,6,56,89,1]
def bubble_sort(b):
    for i in range(len(b)-1):
        for j in range(len(b)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    
    print(b)

bubble_sort(a)