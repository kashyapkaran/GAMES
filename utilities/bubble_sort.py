'''in the list 'a' you can put words or numbers and it will sort it!!!'''

a = ["python","java","sql","c++","unity"]
for i in range(0,len(a)-1):
    for j in range(len(a)-1,i+1,-1):
        if a[j] < a[j-1]:
            t = a[j]  
            a[j] = a[j-1]
            a[j-1] = t
         
    if a[i] > a[i+1]:
        t = a[i]  
        a[i] = a[i+1]
        a[i+1] = t
        
print(a)