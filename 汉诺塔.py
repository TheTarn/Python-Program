def hanoi(n,s,m,t):
    if n==1:
        print(s,'-->',t)
    else:
        hanoi(n-1,s,t,m)
        print(s,'-->',t)
        hanoi(n-1,s,t,m)
n=int(input('请输入木盘的个数：'))
hanoi(n,'A','B','C')
