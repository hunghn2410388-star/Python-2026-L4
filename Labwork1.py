import math

def task1():
    radius = float(input("Enter circle radius? "))
    area = 3.14 * radius * radius
    print("Circle area =", area)

def task2():
    celsius = float(input("Enter the temperature in Celsius? "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "(C) =", fahrenheit, "(F)")

def task3():
    num = int(input("Enter a number? "))
    if num <= 1:
        print(num, "is a NOT prime number")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number")
        else:
            print(num, "is a NOT prime number")

def task4():
    num = int(input("Enter a number? "))
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors = sum_divisors + i
    if sum_divisors == num:
        print(num, "is a perfect number")
    else:
        print(num, "is a NOT perfect number")

def task5():
    colors = ["Blue", "Yellow", "Black", "Red", "White"]
    fav_color = input("What is your favorite color? ")
    found = False
    for i in range(len(colors)):
        if colors[i] == fav_color:
            print("Your color is at index", i, "in my list")
            found = True
            break
    if found == False:
        print("Sorry, I could not find your color")

def task6():
    print("range1:", list(range(0, 7)))
    print("range2:", list(range(1, 11, 3)))
    print("range3:", list(range(5, 0, -1)))
    print("range4:", list(range(6, -3, -2)))

def task7():
    s = input("Enter a string with $: ")
    new_s = s.replace("$", "")
    print("New string:", new_s)

def task8():
    my_list = [1, 4, 5, -1, 10]
    evens = []
    for x in my_list:
        if x % 2 == 0:
            evens.append(x)
    print("Original list:", my_list)
    print("Even numbers:", evens)

def task9():
    n = int(input("Enter a non-negative integer: "))
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial of", n, "is", fact)

def task10():
    n = int(input("Enter a number: "))
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    print("Divisors of", n, "are:", divisors)

def task11():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Distance is:", distance)

def task12():
    m = int(input("Enter rows (m): "))
    n = int(input("Enter columns (n): "))
    for i in range(m):
        for j in range(n):
            print("*", end=" ")
        print()

#Program control menu
while True:
    print("\n------------------------------")
    print("Select task (1-12) or 0 to Exit")
    choice = input("Enter number: ")

    if choice == '1': task1()
    elif choice == '2': task2()
    elif choice == '3': task3()
    elif choice == '4': task4()
    elif choice == '5': task5()
    elif choice == '6': task6()
    elif choice == '7': task7()
    elif choice == '8': task8()
    elif choice == '9': task9()
    elif choice == '10': task10()
    elif choice == '11': task11()
    elif choice == '12': task12()
    elif choice == '0':
        print("Goodbye!")
        break  
    else:
        print("Invalid choice, please try again.")