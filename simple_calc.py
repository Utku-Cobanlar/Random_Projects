print("This is a simple calculator.")
while True:
    try:
        num1 = float(input("Enter a number: "))
        result = num1
        break
    except:
        print("Enter a proper number please.")
while True:
    oper = input("Chose operation(+,-,*,/,=):" )
    if oper == "+" or oper == "-" or oper == "*" or oper == "/":
        while True:
            try:
                num2 = float(input("Enter a number: "))
                break
            except:
                print("Enter a proper number please.")
        if oper == "+":
            result = result + num2
        elif oper == "-":
            result = result - num2
        elif oper == "*":
            result = result * num2
        elif oper == "/":
            result = result / num2
    elif oper == "=":
        print("Result is :" + str(result))
        break
    else:
        print("Enter a correct operator!")
    