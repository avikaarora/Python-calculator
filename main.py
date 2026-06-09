print ("Calculator")
print ("Do you want to add, subtract, multiply, or divide?")
operator = input ("Type + for addition, - for subtraction, * for multiplication, and / for division.")
num1 = input (int("Enter number 1"))
num2 = input (int("Enter number 2"))
if operator == "+":
    ans = num1 + num2
    print (ans)
else:
    if operator == "-":
        ans = num1 - num2
        print (ans)
    else:
        if operator == "*":
            ans = num1*num2
            print (ans)
        else:
            if operator == "/":
                ans = num1/num2
                print (ans)
            else:
                print ("I am sorry. I didn't get you.")
