'''Email Slicer is a simple tool that slices the email adresses into two parts - the username and the domain name'''

print("Welcome to the Email Slicer tool")

#Importing a python library "email_validator" to validate email addresses
from email_validator import validate_email, EmailNotValidError


#Defining an empty list to store the email addresses
l = []

choice = "Yes"
while choice == "Yes" or choice == "yes" or choice=="Y" or choice=="y":
    email_address = input("Enter an email address - ").strip()   #Taking input from the user
    if email_address == "":   #Exception handling when user does not enter any input
        print("Please enter an email address.")
    else:    
        #Appending the email address to the list created
        l.append(email_address)

    #Asking the user whether to add another email address or to proceed
    choice = input("Do you want to add another email address ? (Yes/No) - ") 


#Function to slice the email addresses
def slicer(item):
    pos = item.index("@")
    user_name = item[0:pos]
    domain_name = item[(pos+1):]
    print("Username:",user_name,"and domain:",domain_name.upper())


#Function to validate email addresses
def check(email):
    global invalid
    try:
        valid = validate_email(email)
        email = valid["email"] 
        slicer(email)
    except EmailNotValidError as invalid:
        print("The email address",email,"is not valid.") 
        print("Reason - ")
        print(str(invalid))

            
#Function call
for item in l:
    check(item)


