def increment(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry > 0:
        digits.insert(0, carry)

    return digits

result1 = increment([1, 2, 3, 4, 5])
print(result1)  

result2 = increment([9, 9, 9])
print(result2)  
