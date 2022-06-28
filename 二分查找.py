x=int(input("请输入要查找的数据："))
step=0
left=1
right=1000
while(left<right):
    mid=(left+right)//2
    step+=1
    if mid>x:
        right=mid-1
    elif mid<x:
        left=mid+1
    else:
        break
print("查找的次数为：",step)
