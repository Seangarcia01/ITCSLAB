def calculate_average(grades):
    return sum(grades) / len(grades)

SeanGarcia = (97, 99, 98, 92, 88)
PaulGarcia = (79, 90, 88, 92, 95)
JoyRollan = (95, 90, 98, 92, 98)

print("SeanGarcia: ", SeanGarcia)
print("Average: ", calculate_average(SeanGarcia))
print() # for spacing

print("PaulGarcia: ", PaulGarcia)
print("Average: ", calculate_average(PaulGarcia))
print() # for spacing

print("JoyRollan: ", JoyRollan)
print("Average: ", calculate_average(JoyRollan))