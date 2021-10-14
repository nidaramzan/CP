LIST=[]
X=int(input('GENERATE A NUMBER SERIES'))
for m in range (1,X+1):
    Y=int(input('ENTER A NUMBER'))
    X=X+1
    LIST.append(Y)
print('the largest integer  is', max(LIST))
