#Q.2 program to calculate total amount raised in charity camp where people can coordinate items or even make
#  monetary donations. The charity camp ran for 3 days. Also calculate if they were able to raise the target
#  amount of Rs 2,00,000
total_amount=0
count=1
while count<=3:
    charity_sales=float(input("charity sales amount on day : "+str(count)+':'))
    total_amount+=charity_sales
    donation=float(input('donation amount in day : '+str(count)+':'))
    total_amount+=donation
    count+=1
if total_amount >= 200000:
    print('charity camp has rise sucessfully to more than $200000')
else:
    less = 200000-total_amount
    print('we are short of rupees', less ,'from the intened amount Rs. to back')