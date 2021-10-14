def fab (n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fab(n-2)+fab(n-1))
n=int (input('num'))
for i in range(0,n+1):
    print(fab(i))
    

