n=int(input())
for i in range(1,(2*n)):
    if i<=n :
       stars=i
    else:
        stars=2*n-i
    print("* "*stars) 