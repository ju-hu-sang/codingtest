year1 = int(input())
if year1%4 ==0 and (year1%100 !=0 or year1%400==0):
   print(1)
else:
   print(0)