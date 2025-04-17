# program for checking authentication

# email = "waqar00@gmail.com"
# password = "1234"

# userEmail = input("Enter yiur Email?")
# userpassword = input("Enter yiur Password?")


# if(userEmail == email):
#     if(userpassword == password):
#         print("Login Sucessfull!")
#     else:
#         print("PAssword is Incorrect!!!")
# else:
#         print("Email is Incorrect!!!")
    
name = input("Enter your name? ")
age = int(input("Enter your Age? "))
education = int(input("Enter your Education? (inter = 12)"))
deposit = input("Do your afford Block amount? i.e 11904Euro (Y/N)").upper()

if age >= 18:
    if education >= 12:
        if deposit == "Y":
            print(f"{name}, you're Eligible for Applying Visa")
        else:
            print(f"{name}, you're to low in BLock account amount...")
    else:
        print(f"{name}, you're to low in Education......")
else:
    print(f"{name}, you're to low in Age......")


