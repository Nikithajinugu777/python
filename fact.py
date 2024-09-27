def rfact(n):
 if(n==0):
  return 1
 else:
  return n*rfact(n-1)
n = int(input("enter value:"))
if (n < 0):
  print("enter valid value")
else:
  print("factorial is" ,rfact(n))
