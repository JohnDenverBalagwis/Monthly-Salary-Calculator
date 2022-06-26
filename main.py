
AppRunning = True
while AppRunning == True:
    print("\n\n==============================================")
    print("\t\tM O N T H L Y \t\t")
    print("\tS A L A R Y  C A L C U L A T O R")
    print("==============================================")
    print("\nChoose your employment status:")
    print("\tR - Regular")
    print("\tC - Casual")
    print("\tJ - Job Order")
    print("\tP - Part Timer")
    typeOfEmp = input("\nEnter employment status:  ").strip().lower()
    daysWorked = int(input("\nEnter no. of working days: "))
    print("==============================================")
    if typeOfEmp == "r":
        rate = 1149.45
        tax = 0.12
        Pagibig = 150.0
        Gsis = 1250.0
        grossPay = rate * daysWorked
        totalDeduction = (Pagibig + Gsis) + (grossPay * tax)
        netPay = (grossPay - totalDeduction)
        print(f"Your actual salary or Gross pay: ${grossPay:.2f}")
        print(f"Your total deduction is: ${totalDeduction:.2f}")
        print(f"Your deducted salary or Net pay: ${netPay:.2f}")
    elif typeOfEmp == "c":
        rate = 709.00
        tax = 0.12
        Gsis = 1250.00
        grossPay = rate * daysWorked
        totalDeduction = (Gsis) + (grossPay * tax)
        netPay = (grossPay - totalDeduction)
        print(f"Your actual salary or Gross pay: ${grossPay:.2f}")
        print(f"Your total deduction is: ${totalDeduction:.2f}")
        print(f"Your deducted salary or Net pay: ${netPay:.2f}")
    elif typeOfEmp == "j":
        rate = 425.00
        tax = 0.12
        SSS = 333.00
        grossPay = rate * daysWorked
        totalDeduction = (SSS) + (grossPay * tax)
        netPay = (grossPay - totalDeduction)
        print(f"Your actual salary or Gross pay: ${grossPay:.2f}")
        print(f"Your total deduction is: ${totalDeduction:.2f}")
        print(f"Your deducted salary or Net pay: ${netPay:.2f}")
    elif typeOfEmp == "p":
        rate = 250.00
        tax = 0.0
        grossPay = rate * daysWorked
        totalDeduction = (grossPay * tax)
        netPay = (grossPay - totalDeduction)
        print(f"Your actual salary or Gross pay: ${grossPay:.2f}")
        print(f"Your total deduction is: ${totalDeduction:.2f}")
        print(f"Your deducted salary or Net pay: ${netPay:.2f}")
    else:
        print("Invalid input")
        exit()

    print("==============================================")
    print("\t\tT H A N K  Y O U!\t\t")
    print("==============================================\n\n")

    check = input(
        "\nDo you want to quit or start again? \nEnter Y to restart or another key to end: ")
    if check.upper() == "Y":
        continue
    print("\nBye...")
    break