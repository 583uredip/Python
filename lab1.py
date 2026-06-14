import string
user_input=input("Enter Char,Digit,Symbol:")
if user_input=="":
    print("You Did Not Provied Any input...")
else:
    char = user_input[0]
    if char.isalpha():
        if char.isupper():
            print(f"'{char}' Is Upper Alpabet..")
        elif char.islower():
            print(f"'{char}' Is Lowwer Alpabet..")
        else:
            print(f"'{char}' Is Alpabet..")
    elif char.isdigit():
            print(f"'{char}' Is Digit....")
            
    elif char is string.punctuation:
        print(f"'{char}' Is A P unctuation ...")
    elif char.isspace():
        print("You Pressed Only Space Bar")
        
    else:
        print(f"'{char}' Is A Another Symbol....")