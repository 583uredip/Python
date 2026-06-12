#1.write a python to disapaly a user entered name followed by good Afternoon using input() function.
name=input("Enter Your Name:")
print(f"Your Name Is:{name}")
print(f"Good Afternoon:{name}")

#2.Write a program to fill in a letter template give below with name and date.
letter='''Dear <|Name|>,
        Your are selected!
        <|Date|>'''
print(letter.replace("<|Name|>","Rahul").replace("<|Date|>","12 June,2026"))
print(letter.replace("<|Name|>","Sujoy").replace("<|Date|>"," For Footbal Team"))

#2.Write a program to detect double space in a string
cup=("Can   Brazil win the 2026 World   Cup?")
print(cup.find(" "))

#Replace the double space from problem 3 with single space.
cup=("Can   Brazil win the 2026 World   Cup?")
print(cup.replace(" ",""))
print(name)# String are immutable

#Write a program to formate the following letter using escape sequence charecters.
letter="I love footbal\n\t,I support the brazil team"
print(letter)


