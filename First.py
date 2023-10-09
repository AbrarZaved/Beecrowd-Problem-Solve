n = int(input("Enter the last number: "))
i=1
temp =n
for i in range(n+1):
    print(" "*temp+"*"*i)
    
    i=i+1
    temp=temp-1

