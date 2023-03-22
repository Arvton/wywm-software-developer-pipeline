hourly_wage = 5.89
hours = 8
daily_wage = hourly_wage * hours
print(daily_wage)

for variable in range(0,10,2):
    print(variable)

texttest = open('D:\\Personal\\WYWM Software Developer Pipeline\\Python Programming Fundamentals\\textfile-exercise.txt', mode = 'r')
for line in texttest:
    print(texttest.readline())
texttest.close()