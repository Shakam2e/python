#employee bonus
salary=float(input("enter your salary:"))
Years=int(input("enter the years spent at the orgnization:"))
def period(salary,Years):
    if Years>10:
        net_bonus=0.1*salary
    elif Years>=6 and Years<=10:
        net_bonus=0.8*salary
    else: 
        Years<=6
        net_bonus=0.5*salary
    return net_bonus
net_bonus=period(salary,Years)
print("your net bonus is:",net_bonus)
 

