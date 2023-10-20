name1=input("Enter the First Name : ")
name2=input("Enter the First Name : ")

if name1=="rock" and name2=='scissors':
    print('Player 1 is the winner')
elif name2=="rock" and name2=='scissors':
    print('Player 2 is the winner')
elif name1=="paper" and name2=='rock':
    print('Player 1 is the winner')
elif name2=="paper" and name1=='rock':
    print('Player 2 is the winner')
elif name1=="scissors" and name2=='paper':
    print('Player 1 is the winner')
elif name2=="scissors" and name1=='paper':
    print('Player 2 is the winner')