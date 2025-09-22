
# ?)- get a string from an input string where all occurences of first charecter replaced with doller symbol except first charecter ?

s = input("Enter a string: ")
a= s[0] + s[1: ].replace(s[0],"$")
print(a)
