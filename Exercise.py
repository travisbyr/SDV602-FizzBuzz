
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 5 == 0:
#         print("buzz")
#     elif number % 3 == 0:
#         print("fizz")
#     else:
#         print(number)

# fizz_buzz(2)

def fizz_buzz(fizz=3, buzz=5, up_to=15):
    x = 0
    result = []
    while x <= up_to:
        string = ""
        if x % 3 == 0: # If x can be divided by 3
            string += "Fizz"
        if x % 5 == 0: # If x can be divided by 5
            string += "Buzz"
        print((x, (str(x) if string == "" else string))) # Print x and its outcome.
        x += 1

fizz_buzz(3, 5, 56)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()