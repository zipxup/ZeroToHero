# ** exponent 5 ** 2 = 25
# / divide as float
# // divide as int

#initialize
area = 0
height = 10;
width = 20;
#calculate the area of a triangle
area = width * height / 2

#d stands for decimal, f stands for float
#%6d - characters with fixed width
print("The area pf the traingel would be %6d" % area) 
#06d - characters begin with 0 
print("The area pf the traingel would be %06d" % area)
#.2f - numbers with 2 
print("The area pf the traingel would be %.2f" % area)

#.format numeric values
#first 0 stands for counting starts from 0
print("I have {0:d} cats".format(6,8,9))
print("I have {0:3d} cats".format(6))
print("I have {0:.2f} cats".format(6))
#multiple numbers
print("Here are three numbers! The first is {0:d}" + \
    " The second is {1:4d} and {2:d}".format(7,8,9))

#\ to indicate command will continue on next line
# be careful when you use \ in strings.