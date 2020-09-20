start=1
end=1000

print("pick a number from 1-1000(the computer will guess it in only 10 chance!!)")

a=0
while start < end :
    mid=(end+start)//2 
    ui = input("Is it greater than "+str(mid) + "?(press T if true,F if false or R if it is the exact number)")
    if ui == "T" or ui =="t" :
        start = mid
        a=a+1     
    elif ui == "F" or ui == "f":
        end = mid
        a=a+1
    elif ui =="R" or ui == "r":
        a=a+1
        print(str(mid)+" is the answer.It took "+str(a)+"chances to guess the answer")
         
        break

    
           
    