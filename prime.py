import math

def is_prime(n):
    if n<=1:
        return 0
    elif n==2:
        return 1
    elif n%2==0:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return 0
        return True

print(is_prime(11))