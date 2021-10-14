List=[]
hkey=87
if hkey<100:
     List.append(hkey)
     print(List)
     file=open('myfile.txt', 'a')
     List=str(List)
     file.write(List)
