while True:

  Deposit=float(input("Enter Deposit: "))

  month=int(input("Enter month: "))

  Earned=float(input("interest rate: "))

  print("\n{:<10} {:<15} {:<20} {:<25} {:<25} {:<30}".format("Month", "Deposit", "Total Deposit", "This Month's interest", "Total-Interest Earned", "Total-value to-Date"))

  counter = 0 

  for R in range(1,month+1):

        Total_value_start  = (1+Earned/1200)**R

        counter += Total_value_start

        Total_value_end = counter * 100

        Total_Deposit = R*100

        Deposit = 100  

        Interest=Total_value_start-  Total_value_end

        month_int =   Total_value_end/101

    

        print(R,format((Deposit),"15"),format((Total_Deposit),"15"),format((month_int),"20.2f"),format((Interest),"26.2f"),format((  Total_value_end),"25.2f"))



  print("\nHello can I help you sometings? \nDo you want to do again?")

  Respon = input("Do you want to contiue?yes/no:")

  Respon == "yes"

