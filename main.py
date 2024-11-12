# num1=10
# num2=5

# print("AND operator", num1&num2)

# print("OR operator", num1|num2)

# print("XOR operator", num1^num2)

# print("NOT operator", ~num1)

# print("Left shift operator",num1 << 1)

# print("Right shift operator", num1 >> 1)




def evenodd(num):
    if(num^1==num+1):
        return True
    else:
        return False
    
number=int(input("Enter a number:"))
if evenodd(number):
    print(number,"is even")
else:
    print(number,"is odd")