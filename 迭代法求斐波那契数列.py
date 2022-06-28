def fib(n):
    f2=f1=1
    for i in range(3,n+1):
            f1,f2=f2,f1+f2
    return f2
n=int(input('输入需要计算的月份数：'))
print('兔子的总对数为：',fib(n))
