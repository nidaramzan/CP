list1=input('enter the element of list1')
list2=input('enter the elememt of list2')
list3=[]
list4=[]
list5=[]
for m in list1:
    if m in list2:
        list3.append(m)
    elif m not in list2:
        list4.append(m)
for n in list2:
    if n in list1:
        list5.append(n)
    else:
        list4.append(n)
print('COMMOM=',list3)
print('UNCOMMON=',list4)
            
