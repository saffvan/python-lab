
# find the fibinocci series of n terms using function


def fib(n):
    a=0
    b=1
    print(f"first {n} fibinocci numbers are : \n")
    if n==1:
        print(a)
    else:
        for i in range(n):
            print(a)
            c=a+b
            a=b
            b=c

            
n=int(input("enter the no:of terms: "))
if n < 1:
    print("invalid input!")
else:
    print(fib(n))


    
