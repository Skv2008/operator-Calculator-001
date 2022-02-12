#Mini Calculator
while(True):
    first=int(input('Enter first number : '))
    Operation=input("Enter operator (+,-,*,**,***,%) : ")
    second=int(input ('Enter second number : '))
    op='Your answer : '

    if Operation=='+' :
        print(str(op) ,  first+second)
        
        

    elif Operation=='-' :
        print(str(op) ,  first-second)
    
    elif Operation=='*' :
        print(str(op) ,  first*second)
    
        
    elif Operation=='**' :
        print(str(op) ,  first**second)
    
    elif Operation=='/' :
        print(str(op) ,  first/second)                
                                        
                    
    elif Operation=='***' :
        print(str(op) ,  first+second)                 

    elif Operation=='%':
        print(str(op) ,  first%second)
    
    else:       
        print("invalid number" )     
    op=input('Do you want to calculate again? /a press (y) for Yes and (n) for No : '  )
    if op=='n':
        print('See you later')
        break
    elif op=='y':
        print('ok')
        continue
   
        
        
