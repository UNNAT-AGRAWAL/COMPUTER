# string opreters
#    concatenation opreator
name1='1'+'1'
print(name1)
#     replication 
name2=9* ' u'
print(name2)
# membership opretor
# task  : 
name3='123' 
name4='Japan' 
c=name3 not in name4
print(c)
#comparison opretor 
name5='avinash'
name6='raghav'
a=name5!=name6
print(a)
# string slices
u='#'
pa=" "
for a in range(5):
    pa+=u
    print(pa)
# string functions (string capitalisation)
sen='i love my india'
print(sen.capitalize())
# find function 
name='It goes as ringa ringa roses pocket full of foes'
print(name)
sub=input('enter a letter from above sentence : ')
ra=int(input('enter a range : '))
ge=int(input('enter a range : '))
print(name.find(sub,ra,ge))
#    string.isalnum
string='abc123'
string1='hello'
string2='12345'
string3=''
print(string.isalnum())
print(string1.isalnum())
print(string2.isalnum())
print(string3.isalnum())
#    string.isalpha
string='abc123'
string1='hello'
string2='12345'
string3=''
print(string.isalpha())
print(string1.isalpha())
print(string2.isalpha())
print(string3.isalpha())
#    string.isdigit
string='abc123'
string1='hello'
string2='12345'
string3=''
print(string.isdigit())
print(string1.isdigit())
print(string2.isdigit())
print(string3.isdigit())
#   read a line and print the number of lower , upper case is there
user_in=input('Enter a line of text : ')
lower_count=upper_count=0
digit_count=0
alpha_count=0
for a in user_in:
    if a.islower():
        lower_count+=1
    elif a.isupper():
        upper_count+=1
    elif a.isdigit():
        digit_count+=1
    if a.isalpha():
        alpha_count+=1
print('no. lower letter ', lower_count)
print('no. upper letter ', upper_count)
print('no. number in line ', digit_count)
print('no. alpha letter in line ', alpha_count)
# string  triversal
name='raghav'
print('the ', name, ' in reverse order is ')
lenght=len(name)
i=0
for a in range(-1,-lenght-1,-1):
    print(name[i],'\t' , name[a])
    i=i+1
