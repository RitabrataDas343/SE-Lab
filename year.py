def checkLeapYear():
    year = input("Enter the year:")
    leap = False
    if(year % 100 == 0):
        if(year % 400 == 0):
            leap = True
    else:
        if(year % 4 == 0):
            leap = True
    if(leap):
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
    print("Ending Code...")

checkLeapYear()
