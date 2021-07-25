def fizz_buzz(number):
    #fizz - multiples 3 /3
    # buzz - multiples 5 /5

    #buzz = number / 5
    #fizz = number / 3

    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)





fizz_buzz(2)