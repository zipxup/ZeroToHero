team = input("Enter your favorite hockey team: ").upper()
#team = team.upper()
#if team == "FLYERS":
#    print("Best team ever!")
#elif team == "SENATORS":
#    print("Go Sens Go!")
#elif team == "RANGERS":
#    print("Go Rangers")
#else:
#    print("I don\'t have anything clever to say")

sport = input("Enter your favorite sport: ").upper()

#if sport == "HOCKEY" and team == "RANGERS":
#    print("I miss Messier")
#elif team == "LEAFS" or team == "SENATORS":
#    print("Good luck getting the cup this year")
#else:
#    print("I don't know that team")

#nested if statement
if sport == "HOCKEY":
    print("Go Hockey!")
    if team == "SENATORS":
        print("good luck")
    print("we do love hockey")