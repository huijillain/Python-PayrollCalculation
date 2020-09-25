# Program Name:     Payroll Calculations
#
# Programer:        Hui Jillain
#
# Date:             25-Jun-2020
#
# Description:      project to collect all the necessary values to compute the paytolltable, and then ouput the result.
#
#                   Demostrateds the use of return statement function for invalid value to remind user to fill in right number value.
#                   For employee's tax exempt status, will need to use boolean for two different options. If employee is not exempt, then ask
#                   for deduction precentage. Need to make sure user enter number without %, but calculation decimal equivalents respectively.
#
#                   All money amounts on pay-slip be displayed using typical currency format( dollar sign, 2 decimal digits representing the cents)
#                  
#
#
# use return statement function to validate value entered.
def getValue(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
        try :
             lineOfInput = input(prompt)
             value = int(lineOfInput)
             if (value < minimum) : # validate input to make sure in right form and in correct range. If it is 0, need to re-enter.
                  print("** Percentage entered must be greater than zero ... Try again.")
             else :
                    goodValue = True;
        except ValueError:
             print("** Percentage entered must be greater than zero ... Try again.")
             
    return value



#get input of employee information. Verify that they are good, and if not then ask to enter again.

employeeName = input("Entere the employee's name: ")
hoursWorked = float(input("Enter hours worked: "))
while hoursWorked <= 0:
    print("** Hours worked must be greater than zero ... Try again.")
    hoursWorked = float(input("Enter hours worked: "))
                       
hourlyRateOfPay = float(input("Enter hourly rate of pay: "))
while hourlyRateOfPay <= 0:
    print("** Hourly rate must be greater than zero ... Try again.")
    hourlyRateOfPay = float(input("Enter hourly rate of pay: "))



# get the answer for tax exempt status using boolean expressiton. If answer is N, then request enter of deduction percentage.

taxExemptStatus = input("Is employee tax exempt? [Y/N] :")

if taxExemptStatus == "N" or taxExemptStatus == "n" :
   deductionPercentage = getValue("Enter deduction percentage:", 1, 100)
   
else :
   deductionPercentage = 0  
   
grossPay = hoursWorked * hourlyRateOfPay    
deductionAmount = grossPay * deductionPercentage / 100
netPay = grossPay - deductionAmount


# output/print the results using dollar sign, two decimal digits representing the cents

print("______________________________________________________")
print("Employee Name:", employeeName)
print("Hourly Rate:          $       {:.2f}".format(hourlyRateOfPay))
print("Hours Worked:                 {:.2f}".format(hoursWorked))
print("                     -----------------")
print("Gross Pay:            $      {:.2f}".format(hoursWorked * hourlyRateOfPay))
print("Deductions:         - $       {:.2f}".format(grossPay * deductionPercentage / 100))
print("                     -----------------")
print("Net Pay:              $      {:.2f}".format(grossPay - deductionAmount))
