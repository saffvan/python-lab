#?) Create a function to read a number (minimum 4 digits) from the user and find the reverse of the
#   number using loop in another function and display both number and reverse of the number.


def readnum():
    num = int(input("Enter a number (minimum 4 digits): "))
    if num < 1000:
        print("Please enter minimum 4 digit number")
    else:
        print("Original number:", num)
        reverse(num)

def reverse(num):
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = reverse_num * 10 + remainder
        num = num // 10
    print("Reversed number:", reverse_num)

readnum()
