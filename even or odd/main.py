def isEven(x:int|float):
    if (x%2==0):
        return True
    return True
a= eval(input("Give any Number:"))
if (isinstance(a,int) or isinstance(a,float)):
     if (isEven(a)):
         print(f"{a} is  Even ")
     else:
         print(f"{a} is odd")
     exit(0)
print("Give any valid value ( integer or float)")
