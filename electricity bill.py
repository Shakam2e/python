CustomerID=int(input("enter your ID:"))
CustomerName=input("enter your name:")
UnitConsumed=float(input("enter the units consumed:"))

def Bill(UnitConsumed):
    if UnitConsumed<=199:
        Unit=UnitConsumed*1.20
    elif UnitConsumed>=200 and UnitConsumed<400:
        Unit=UnitConsumed*1.50
    elif UnitConsumed>=400 and UnitConsumed<600:
        Unit=UnitConsumed*1.80
    elif UnitConsumed>=600:
        Unit=UnitConsumed*2.00
    else:
        print("out of range.Try again:")
    return Unit
Unit=Bill(UnitConsumed)
print("your bill is:",Unit)
if Unit>400:
    surcharge=Unit+(Unit*1.5)
    print("yor surcharge is:",surcharge)
else:
    print("you dont have any sucharges:")
if Unit<100:
    print("your bill is less than 100:")
else:
    print("")
charges_per_unit=Unit/UnitConsumed
print("your charges per unit are:",charges_per_unit)
total_amount_to_pay=Unit+surcharge
print("the total amount payable is",total_amount_to_pay)

 

