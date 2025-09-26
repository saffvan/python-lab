# ?) write a python menu program. the option contain,
#       1. Occurence of Word:
#       2. Charector Frequency:
#       3. Factors of a given number: 
#       4. Exit


z=1
while(z==1):   
    print("\n---MENU---\n")
    print("1. Occurence of Word: ")
    print("2. Charector Frequency: ")
    print("3. Factors of a given number: ")
    print("4. Exit ")

    n = int(input("\nChoose one of the option (1 - 4): "))
    if (n==1):
        a =input("\nEnter the text : ")
        b = a.split()
        s = set(b)
        for i in s:
            print(i, "=", b.count(i))
    elif (n==2):
        a = input("\nEnter the text : ")
        b = set(a)
        for i in b:
            print(f"\n{i} = {a.count(i)}")
    elif n==3 :
        a = int(input("\nEnter a number: "))
        print(f"\nfactors of {a} are: ")
        for i in range(1,a+1):
            if a%i==0:
                print(i)
    elif n==4 :
        z=4
        print("Exited")
    else :
        print("\ninvalid option")
        
        
            
        
        
            
     
