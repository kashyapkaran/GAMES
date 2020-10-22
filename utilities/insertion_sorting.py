'''in the list 'a' you can put words or numbers and it will sort it!!!'''


a = [5,6,2,"frie",4,3,6]

for j in range(1,len(a)):
    print(str(j))
    key=a[j]
    i = j - 1
    #change the '>=' in between a[i] and key to make it decreasing or increasing order.  
    while i>=0 and a[i] >=key:
        
        a[i+1] = a[i]
        i -= 1
    a[i+1] = key

    print(a)

