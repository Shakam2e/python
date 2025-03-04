num=int(input("enter the number:"))
def fibonucci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonucci(num-1)+fibonucci(num-2)
for i in range(num):
    print(fibonucci(i),end="")
