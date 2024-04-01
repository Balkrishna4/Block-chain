def enter_pswd():
    password=input("Please reenter you Password:-  ")
    len_verification(password)
    # return password
    
global userid_pswd_verification
def userid_pswd_verification(userid,pswd):
    if(len(userid)>3):
        for a in range(len(pswd)-2): 
            check=0
            for b in range(len(userid)-2):
                if(pswd[a]==userid[b] and pswd[a+1]==userid[b+1] and pswd[a+2]==userid[b+2]):
                    print("Wrong Password type , continuous three character of UserId found in password")
                    enter_pswd()
                    check=1
                    break;
            if check==1:
                break;
                    
    print("Thank you your password has been set succesfully \n Not checking for history of password bcz code become messed up actually that is very simple, \n 1. After succesfull password setup ask user do you want to set password again if yes \n 2. Store previous password by appending it in a list \n 3.Now at the end match with that list if found equal to previous passwords then ask to reenter the password")
            
global detail_verification
def detail_verification(pswd):
    for a in range(0,len(pswd)-2):
        if(pswd[a]==pswd[a+1] and pswd[a+2]==pswd[a+1]):     #checking for continous 3 character whether they are equal
            print("Wrong Password type,continous three character match")
            enter_pswd()
    userid_pswd_verification(user_id,pswd)


global count_verification
def count_verification(pswd):
    #cuc count of upper case,clc count of lower case
    
    cuc=0
    clc=0
    csc=0  #special character
    cd=0   #count of digits
    cs=0   #count of space
    
    for a in pswd:
        if a.islower():
            clc+=1
        elif a.isupper():
            cuc+=1
        elif a.isdigit():
            cd+=1
        elif a.isspace():
            cs+=1
        else:
            csc+=1                   #if word is none of above then i guess it will be special character
    
   
   
    if(clc<2):
        print("Wrong Password type it should contain atleast two lowercase")
        enter_pswd()
    elif(cuc<2):
        print("Wrong Password type it should contain atleast two uppercase")
        enter_pswd()    
    elif(cd<2):
        print("Wrong Password type it should contain atleast two digits")
        enter_pswd()
    elif(cs!=0):
        print("Wrong Password type it should not contain any space")
        enter_pswd()
    elif(csc<2):
        print("Wrong Password type it should contain atleast two special character like @ # % & etc")
        enter_pswd()
    else:
        detail_verification(pswd)

global len_verification
def len_verification(pswd):

    if len(pswd)<10:
        print("Password is too small please enter atleast of size 10")
        
        while(len(pswd)<10):
            pswd=enter_pswd()
        
    count_verification(pswd)
    
    
user_id=input("Please Enter your User ID:-  ") 
pswd=input("Enter you Password:-  ")
global password
password = pswd
len_verification(password)