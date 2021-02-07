print('请您想一个1~100的数字，我会尽力猜它。当我猜时，输入1表示我猜大了，0表示我猜小了，2表示我猜对了')
target = 50
small = 0
big = 100
print(str(target) + '对吗？')
status = int(input())
while status != 2:
    if(small == big):
        target = small
    else:
        if status == 1:
            sub = target - small
            big = target - 1
            target -= sub // 2
        elif status == 0:
            sub2 = big - target
            small = target + 1
            target += sub2 // 2
        else:
            print('输入不合法！')
    print(str(target) + '对吗？')
    status = int(input())
print("我知道我可以的！")
