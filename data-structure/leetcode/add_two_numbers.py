# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

def add(num1, num2):
    carry=0
    res = list()
    #if num1 and num2 are of varying length
    #run through by longest number and inaccebli index on smaller number can be made return 0
    for i in range(len(num1)):
        if(carry!=0):
            res.append((num1[i]+num2[i])%10+carry)
        else:
            res.append((num1[i]+num2[i])%10)
        if(num1[i]+num2[i] >9):
            carry=1
        else:
            carry=0
    print(res)

def main():
    number1 = [2,4,3]
    number2 = [5,6,4]
    add(number1,number2)


if __name__ == '__main__':
    main()
