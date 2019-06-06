## Fibonacci series
## 

def print_fib(n):
    
    if n<0:
        print("Incorrect")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return print_fib(n-1) + print_fib(n-2)
        
def print_fib_dp(n):
    a=0
    b=1
    
    if n==0:
        return a
    elif n==1:
        return b
      
    else:  
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        
    return c
        
def fb_dp(n):
    fib=[0] * (n+1)
    fib[1]=1
    
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2] 
        
    return fib[n]
        
n=print_fib_dp(9)
print(n)
n=fb_dp(19)
print(n)