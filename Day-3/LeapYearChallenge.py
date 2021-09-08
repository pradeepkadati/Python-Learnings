print("Leap Year Challenge")

year = int(input("Enter the year:"))


if year % 4 == 0:
    print("year divided by 4")
    if year % 100 == 0:
        print("year divided by 100")
        if year % 400 == 0:
            print("LEAP YEAR")
        else:
            print("not a LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("not a LEAP YEAR")

