n=int(input())
for i in range(1,2*n):
     if i<=n :
            count=i
     else:
            count=2*n-i
          
     for j in range(count):
           print("* ",end="")

     spaces=2*(n-count)
     print("  "*spaces,end="")
  
     for j in range(count):
          print("* ",end="")
      
     print()

