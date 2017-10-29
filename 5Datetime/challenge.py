import datetime
deadlineStr = input('please enter the deadline of your project' \
    + '(mm/dd/yyyy)')

deadlineDate = datetime.datetime.strptime\
    (deadlineStr, '%m/%d/%Y').date()
currentDate = datetime.date.today()
days = deadlineDate - currentDate
print("%d days" % days.days)

weeks = days.days / 7
remainDays = days.days % 7
print("You have %d weeks, %d days until your deadline" %(weeks, remainDays))