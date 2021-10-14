number=int(input('enter the number'))
while number>0:
    if number%2!=0:
      print('the number you enter is odd')
      break
    elif number%2==0:
      print('the number you enter is even')
      break
    else:
      print('enter the positive number')
