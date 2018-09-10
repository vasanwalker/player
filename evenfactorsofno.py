
def factors(y):
   for i in range(1, y + 1):
       if i%2 == 0:
         if y%i == 0:
           print(i)
n=int(input())

factors(n)
