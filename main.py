
# Task 1 ----------
print("______________________________________________________________________________________")
print("This function will print a list of integers from the smallest number to the largest")
a = int(input("\tPlease input the smallest number: "))
b = int(input("\tPlease input the largest number: "))
l = [i for i in range(a, b + 1)]
print(*l, sep=" ")
print("------------------------------------------")


# Task 2 --------------------
print("This function will print a sum of two integer number")
a2 = None
b2 = None
while a2 is None or b2 is None:
    first_input = input("Please input the first number: ")
    second_input = input("Please input the second number: ")
    try:
        a2 = int(first_input)
        b2 = int(second_input)
    except ValueError:
        print("{f} or {s} is not an integer, please enter only integer".format(f=first_input, s=second_input))
print()
if a2 % 2 == 1:
    print("The first number {f} is an odd number".format(f=first_input))
else:
    print("The first number {f} is an even number".format(f=first_input))
if b2 % 2 == 1:
    print("The second number {s} is an odd number".format(s=second_input))
else:
    print("The second number {s} is an even number".format(s=second_input))
print("The sum of {f} and {s} is ".format(f=first_input, s=second_input), a2+b2)
print("-----------------------------------------------------------------------")


# Task 3
import math
print("The sum of Pi and square root of 2 is {:.2f}".format(math.pi + math.sqrt(2)))
print("-----------------------------------------------------------------------------------")

# Task 4
print("This function will print the result of    cos A + sin B with A and B are in degree")
A = None
B = None
while A is None or B is None:
    first_input = input("\tPlease input the angle A: ")
    second_input = input("\tPlease input the angle B: ")
    try:
        A = int(first_input)
        B = int(second_input)
    except ValueError:
        print("{f} or {s} is not an integer, please enter only integer".format(f=first_input, s=second_input))
cos = math.cos(A*(math.pi)/180)
sin = math.sin(B*(math.pi)/180)
print("\t ==> cos {} + sin {} = {:.2f}".format(A, B, cos + sin))

