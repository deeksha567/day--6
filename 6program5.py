import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    if s*s == x:
        return True
def isFibonacci(n):
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    return isPerfectSquare(5 * (n*n) + 4) or isPerfectSquare(5 * (n*n) - 4)

n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = int(input("Enter element : "))
    arr.append(d)
sum1=0
for i in range(n):
    sum1=sum1+arr[i]
if isFibonacci(sum1) == True:
    print("Sum is a fibonacci number")
else:
    print("Sum is not a fibonacci number")

#code by Deeksha singh
