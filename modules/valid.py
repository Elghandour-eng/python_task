import re

def validateEmail():
    email=input("Enter Your Email :")
    if email != '':
    
        if re.fullmatch('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email):
           print('valid')
           print(email)
        else:       
           print("Email Not Valid")
           validateEmail() 
    else :
        print("Email is Empty")
        validateEmail() 
                 
    return email
  
def validateName(n):
    name=input(f"Enter Your {n} Name :")
    if name != '':

    
        if re.fullmatch('^[A-Za-z][A-Za-z0-9_]{7,29}$' ,name): 
            print("Name is Valid")
        else:       
         print("name Not Valid")
         validateName(n) 
    else :
        print("Name is Empty")
        validateName(n)        
    return name   

def validatePhone():
    phone=input("Enter Your Phone :")
    if phone != '':
        
        if re.fullmatch('^[0-9\-\+]{9,15}$',phone):
          print("Phone is valid")   
        else: 
            print("Phone is invalid")
            validatePhone()      
    else :
        print("Phone is Empty")
        validatePhone()
               
    return phone
def validatePassword(passa):
    password=input(f"Enter Your {passa} Password :")
    if password != '':
 
           print("Valid pass")    
    else :
        print("Password is Empty")
        validatePassword(passa)
    return password  


    

 
  
            
