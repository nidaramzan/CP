while True:
    ID=input('Enter your ID')
    MENU=('MAIN MENU\n'
       '1-DEPOSITE MONEY\n'
       '2_WITHDRAW AMOUNT\n'
       '3_LOGIN IN DIFFERENT USER')
    print(MENU)
    A=int(input('Enter your choice'))
    if A==1:
        print('How much amount you deposited?')
        AMOUNT=int(input('Enter amount'))
        print("THANKS!, if you want to continue press KEY 1, if not then KEY 2")
              
        key=int(input('SELECT KEY'))
        if key==2:
         print('GOOD BYE!, TRANSACTION HAS COMPLETED')
         break
        elif key==1:
         print('chose again')
         CH=int(input('YES press key 1 or NO press key 2?'))
         if CH==1:
            print(MENU)
         elif CH==2:
            print('OK BYE!')

    elif A==2:
        AMOUNT=int(input('how much do yo want to withdraw?'))
        print('THANKS!, if you want to continue press KEY 1, if not then KEY 2')
        KEY=int(input('SELECT KEY'))
        if KEY==2:
         print('GOOD BYE!, TRANSACTION HAS COMPLETED')
         break
        elif KEY==1:
            print('chose again')
        CH=int(input('YES press key 1 or NO press key 2?'))
        if CH==1:
            print(MENU)
        elif CH==2:
            print('ok bye')

    elif A==3:
     print('do you want to login with another account? if yes press key 1, if not then key 2')
     key=int(input('SELECT KEY'))
     if key==2:
         print('you are not able to login with another account, GOOD BYE!')
     elif key==1:
         print('Now you can use another account')
     CH=int(input('SELECT CHOICE'))
     if CH==1:
          print(MENU)
     elif CH==2:
          print('GOOD BYE!')
     
        
        
            
         
            
            
        
            
        
              
