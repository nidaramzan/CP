
def fibonic_series(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return (fibonic_series(n-2)+fibonic_series(n-1))
n=int(input('enter the number'))
for num in range(0,n):
  print(fibonic_series(num))


    
