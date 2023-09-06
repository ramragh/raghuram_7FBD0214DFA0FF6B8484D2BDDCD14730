#program to check a leap yar using elif

year=int(input("please enter the year number (eg:2019):"))

if(year%400==0):
      print("%d is a leap year"%year)
elif(year%100==0):
      print("%d is a leap year"%year)
elif(year%4==0):
      print("%d is Leap Year"%year)
else:
      print("%d is Not the Leap Year"%year)