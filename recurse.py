def initialise(phrase):
    words=phrase.split()
    result=""
    for word in words:
        result=result+word[0].upper()
    return result
print(initialise("Uninterruptible Power Supply"))

def sum_numbers(numbers):
    if numbers<=1:
        return 1
    # for num in range(1,numbers+1):
        # sum=sum+num
        # num+=1
    return numbers+ sum_numbers(numbers-1)
print(sum_numbers(6))
