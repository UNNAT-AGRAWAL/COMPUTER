a=int(input('enter a no. a : '))
b=int(input('enter a no. b : '))
sq=a*a
s=b*b
cu=a*a*a
c=b*b*b
add=a+b
sub=a-b
s=b-a
pro=a*b    
print('the square of a is : ', sq)
print('the square of b is : ' , s)
print('the cube of a is : ' , cu)
print('the cube of b is : ' , c)
print('the sum of a and b is : ' , add)
if a>b:
    print('the difference if no. a is greater is : ' , sub)
elif b>a:
    print('the difference if no. b is greater is : ' , s)
print('the product is : ' , pro)