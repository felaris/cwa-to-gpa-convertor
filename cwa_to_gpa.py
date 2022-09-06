def cwa_calc(cwa):
    cwa = int(cwa)
    if cwa >=80:
        print("Your GPA is 4.0" ,"\U0001F973","\U0001F973","\U0001F973")

    elif cwa<80 and cwa>=75:
        print("Your GPA is 3.5 ","\U0001F38A","\U0001F38A","\U0001F38A")

    elif cwa<75 and cwa>=70:
        print("Your GPA is  3.0 " ,"\U0001F609","\U0001F609","\U0001F609")

    elif cwa<70 and cwa>=65:
        print("Your GPA is 2.5 ","\U0001F37E","\U0001F37E","\U0001F37E")

    elif cwa<65 and cwa>=60:
        print("Your GPA is 2.0 ","\U0001F942","\U0001F942","\U0001F942")

    elif cwa<60 and cwa>=55:
        print("Your GPA is 1.5 ","\U0001F60E","\U0001F60E","\U0001F60E")

    elif cwa<55 and cwa>=50:
        print("Your GPA is 1.0 ","\U0001F615","\U0001F615","\U0001F615")

    elif cwa<50 and cwa>=45:
        print("Your GPA is  0.5 ","\U0001F61F")

    elif cwa<45:
        print("Ahh Chairman, you have failed","\U0001F923","\U0001F923","\U0001F923")

cwa_calc(input("Enter your CWA:  "))
