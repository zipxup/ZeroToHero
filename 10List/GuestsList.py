guests = []
keyword = "quit"

currentGuest = input("please enter your guest name: specify 'quit' to stop\n").lower()
while currentGuest != keyword.lower():
    guests.append(currentGuest)
    currentGuest = input("please enter your guest name: specify 'quit' to stop\n").lower()

guests.sort()
#guests.reverse()
print("Here are your guests followed by alphabetic order: ")
for guest in guests:
    print(guest.capitalize())