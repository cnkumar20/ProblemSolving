def sum_of_two_numbers(number1,number2):
    number1.reverse()
    number2.reverse()
    number = list()
    carry = 0
    max_length = len(number2)
    for x in range(max(len(number1),len(number2))):
        temp = number1[x]+number2[x]+carry
        if(temp > 9):
            carry = temp // 10
            number.append(temp % 10)
        else:
            carry = 0
            number.append(temp)
    if(carry !=0):
        number.append(carry)
    number.reverse()
    return number
if __main__():
    n1 = [4,3,2]
    n2 = [9,3,9]
    sum_of_two_numbers(n1,n2)
