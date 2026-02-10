# 1
print("Task 1")
x = 10
y = 5
print(x + y)
# for spacing
print()

# 2
print("Task 2")
grade = int(input("Grade: "))
if grade < 0:
    print("Error. Input must be greater than or equal to 0. Try Again.")
elif grade > 100:
    print("Error. Input must be less than 100.  Try Again.")
elif grade >= 60:
    print("Pass")
else: 
    print("Fail")
# for spacing
print()

# 3
print("Task 3")
for i in range(1, 11):
    print(i)
# for spacing
print()

# 4
print("Task 4")
def greet(name):
    print("Hello", name + "!")
greet("Sean")
# for spacing
print()

# 5
print("Task 5")
nums = [10, 20, 30, 40 , 50]
print(nums[0], nums[-1])
print(sum(nums))