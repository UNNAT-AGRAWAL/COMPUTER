#program to print table of you own number
num=int(input('enter a number of which table you want : '))
u=int(input('enter a no. till where you want the table : '))
for a in range (1,u+1):
    print(num,"X",a,'=',num*a)
