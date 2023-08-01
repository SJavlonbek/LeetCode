def addDigits(num):
    while num>9:
        num=sum(int(digit) for digit in str(num))
    return num
num=int(input("num="))
print(addDigits(num))