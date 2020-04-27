

def dateIntro():
    date = input("Introduce fecha (dd/mm/aaaa):")
    day,month,year = date.split("/")

    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if isValidDate:
        print("Input date is valid ..")
    else :
        print("Input date is not valid..")