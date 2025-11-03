# Accept

lis=[]
n = int(input("Enter the size of the list: "))
for i in range(n):
    w= input("Enter the words: ")
    lis.append(w)

def long():
    a=len(lis[0])
    for i in lis:
        if len(i) > a:
            a = len(i)
    print("The legth of longest word is: ",a)


long()

