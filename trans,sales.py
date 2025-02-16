# Q.1Program to accept transactions made in day and items sold in day for a week and then print average sales made per transaction"""

Total_tarns,Total_sales = 0,0
count = 1
while count <= 7 : 
     trans = int(input("enter transaction made in a day  " +str(count)+":"))
     item = int(input("enter item sold  in a day  " +str(count)+":")) 
     Total_tarns+=trans
     Total_sales+=item
     count+=1
     
avg_sale=Total_sales/Total_tarns
print("total sale made ",Total_sales)
print("total trans made ",Total_tarns)
print("total avg sale",avg_sale)