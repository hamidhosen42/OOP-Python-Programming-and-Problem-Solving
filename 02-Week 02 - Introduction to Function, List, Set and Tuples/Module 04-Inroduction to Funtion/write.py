# with open('message.txt','w') as fileWrite:
#     fileWrite.write('Hello from Python')

# with open('message.txt','a') as fileWrite:
#     fileWrite.write('Hello from Python')

with open('message.txt','r') as fileWrite:
    text = fileWrite.read()
    print(text)