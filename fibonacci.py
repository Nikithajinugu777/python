def rfibo(n):
 if(n<=1):
  return 1
 else:
  return rfibo(n-1)+rfibo(n-2)
a=int(input("enter number of digits:"))
if(a<=0):
 print("enter valid")
else:
 print("fibonacci sequence is:")
 for i in range(a):
   print(rfibo(i))

