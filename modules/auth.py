from modules import valid as v
from modules import projects
import json
import time
def fun():
    while True: 
        num=   input("Press 1 For resgister\nPress 2 For Login : ")
        if num in ["1","2"]:
            break
        
        else:
            print("Invalid Input")
            continue
    if num == '1':
        register()
    elif num == '2':
        login()            

    

def login():
    e= v.validateEmail()
    p=input("Enter Your Password : ")
    if p != '':
        getUserData(e ,p)
    else:
        print("Password is Empty")
        login()

def register():
    e= v.validateEmail()
    f= v.validateName("First")
    l= v.validateName("Last")
    p= v.validatePhone()
    pa=v.validatePassword(" ")
    cpa=v.validatePassword("confirm ")
    if pa != cpa:
      print(" Pass And Confirm not match")  
      pa=v.validatePassword(" ")
      cpa=v.validatePassword("confirm ")
    else :
        print("User Data Saved")
        saveUserData(name=f+l,email=e,phone=p,password=pa,)
        


def generateId():
    
  
# ts stores the time in seconds
   ts = time.time()
   return ts
     
def saveUserData(name , email ,password ,phone):
  
    #try:  
    # 
   
    
    user = {
        "user_id":generateId(),
         "User_email":email,
         "user_name":name,
         "password":password,
         "phone":phone
       }
   
        
    with open('users.json', "r") as file:
       data = json.load(file)

    data.append(user)    
          
    
    with open('users.json', 'w') as f:
         
         json.dump(data, f)
         #f.write("\n")
         f.close()       
    #except Exception as e:
     # print(e)

def getUserData(email ,password):
    
#user= (email,name,password,phone)
       
 with open('users.json', 'r') as f:
            data = f.read()
            if  email in data and password in data:
                    print("Success Login")
                    projects.afterLogin()
                    
            else :
                    print("Failed Login")

                         
            # print(list(filter(lambda x:x["user_email"]  == email, data)))
            #f.write("\n")
            f.close()  

                

