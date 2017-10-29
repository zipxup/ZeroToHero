import datetime

##weak type data
currentDate = datetime.date.today()
#print(currentDate)
#print(currentDate.year)
#print(currentDate.month)
#print(currentDate.day)

##strftime allows you to specify the date format
##%d -- day, #b -- month, #Y -- year
#print(currentDate.strftime('%d %b, %Y'))


#print(currentDate.strftime('please attend event %A, %B %d in the year %Y'))

birthday = input("what is your birthday? (mm/dd/yyyy) ")
#datetime class, datetime module
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date();

nextBirthday = \
    datetime.datetime.strptime("04/12/2014", "%m/%d/%Y").date()
days = currentDate - birthdate
print(days.days)

currentTime = datetime.datetime.now()
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(datetime.datetime.strftime(currentTime, '%I:%M %p'))