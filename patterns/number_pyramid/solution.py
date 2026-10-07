n=int(input())
for i in range(1,2*n):
    if i<=n :
        number=i 
    else:
        number=2*n-i
    print((str(number)+" ")*number) 