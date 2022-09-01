proceed = True

while proceed:

    while True:

        try:

            Deposit = float(input("Enter monthly deposit: "))

            if Deposit < 0:  

                print("Invalid input. Please try again.")

                continue

        except ValueError as error:

            print("Pls enter only numbers and decimals.")

            continue

        else:

            break

    while True:

        try:

            AnnualInterest = float(input("Enter yearly interest rate: "))

            if AnnualInterest < 0:  

                print("Invalid input. Please try again.")

                continue

        except ValueError as error:

            print("Pls enter only numbers and decimals.")

            continue

        else:

            break
            while True:

        try:

                Month = int(input("Enter the number of months you shall be investing: "))

            if (Month < 0) or (Month > 60):  

                print("Input must be in range 0 and 60. Please try again.")

                continue

        except ValueError as error:

            print("Decimals not acceptable. Please enter months in whole number.")

            continue

        else:

            break

# format strings for displaying rows in line with columns, and

# print the header of the table

    A1 = "{:<8}{:^10}{:^20}{:^25}{:^20}{:^25}" 

    A2 = "{:3}{:12.2f}{:15.2f}{:20.2f}{:25.2f}{:25.2f}"

    print("\n")

    print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF $",round(float(Deposit),2)," EVERY MONTH AT AN INTEREST RATE OF ", round(float(AnnualInterest),2),"% FOR A PERIOD OF ", Month," MONTHS", sep = "")

    print("\n")

    print(A1.format("Month ", "Deposit ", "Total Deposits ", "This Month's Interest ", "Total Interest Earned ", "Total-Value To-Date "))

# for loop to caluclate the balance of the investment to date

# create a list of months invested for the loop

    MonthsInvested = range(1, Month+1)

# set the initial values for balance and interestTotal

# for loop to calculate the total deposits, interest for each month, the total  interest to date, and the new balance at the end of each month, plus the following loops

# for loop to print each row

# while loop asking if the user wants to continue

    TotalValueToDate = 0

    TotalInterest = 0

    for n in MonthsInvested:

        CompoundInterest = (Deposit*(1+(AnnualInterest/1200))**n)+(Deposit*n)-Deposit

        MonthlyInterest = CompoundInterest - (Deposit*n)

        TotalDeposits = Deposit * n

        TotalInterest = TotalInterest + MonthlyInterest

        TotalValueToDate = TotalDeposits + TotalInterest

        print(A2.format(No, round(Deposit,2), round(TotalDeposits,2), round

(MonthlyInterest,2), round(TotalInterest,2), round(TotalValueToDate,2)))

# prompt user for an input  to see if he/she wishes to repeat calculation with new inputs plus

# check if user wish to exit program n input, plus

# check if it is a valid input 

    choice = input("Please select Y to repeat the calculation with new inputs or N to exit program: ")

    while 'Y' not in choice or 'y' or 'N' or 'n': 

        if choice == 'Y' or choice == 'y':

             break

        elif choice == 'N' or choice == 'n': 

            print("Thank you for using the calculator.")

            sys.exit()

        else:

            print("Invalid input. Please try again.")

            choice = input("Input option: ")

