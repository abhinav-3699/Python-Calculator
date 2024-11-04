# creating Loop
while True: 

    print("----------Calculator----------")
    print()

    # Taking input from user 
    n1 = float(input("Enter the first number : "))
    n2 = float(input("Enter the second number : "))

    # Operation 
    opr = input("Enter the operation : ")

    # performing calculations under different conditions...
    if opr == "+":
        print(f"The sum of {n1} and {n2} is {n1+n2}")

    elif opr == "-":
        print(f"The sum of {n1} and {n2} is {n1-n2}")

    elif opr == "*" and "x":
        print(f"The product of {n1} and {n2} is {n1*n2}")

    elif opr == "/":
        print(f"The division of {n1} and {n2} is {n1/n2}")

    else :
        print("Enter a valid operator")

    print()

    continuecal = input("Let's do next calculation (yes/no) : ")

    if continuecal.lower() != "yes" :
        print()
        print("Thank you for using....")
        print()
        break


    


