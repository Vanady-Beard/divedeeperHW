#1. Decisions at the Crossroad
# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif  number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")

# 2. The Greatest Showdown

num = [int (x)for x in input("Enter three numbers: ").split (" ")]
greatest = max(num)

print ("The largest number is" + ' ' + str(greatest))

