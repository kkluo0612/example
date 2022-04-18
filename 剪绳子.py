import math

def cuttingRope(n):
    if n<=3:
        return n-1
    a=n//3
    b=n%3
    if b==0:
        return int(math.pow(3,a))
    if b==1:
        return int(pow(3,a-1)*4)
    return int(pow(3,a)*2)

def cuttingRope2(n):
    if n<=3:
        return n-1
    a,b=n//3-1,n%3
    mod=1000000007
    x=3
    rem=1
    while a>0:
        if a%2:
            rem=(rem*x)%mod
        x=(x*x)%mod
        a=a//2
    if b==0:
        return (rem*3)%mod
    if b==1:
        return (rem*4)%mod
    return (rem*6)%mod

if __name__ == "__main__":
    n=8
    print(cuttingRope(n))
    print(cuttingRope2(n))