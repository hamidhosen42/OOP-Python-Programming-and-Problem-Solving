name = input("Enter the name : ")
name1=''

for i in name:
     if i.islower():
        print(i.upper(),end="")
     else:
        print(i.lower(),end="")