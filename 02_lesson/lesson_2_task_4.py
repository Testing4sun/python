# Задачка с собеседования

def fizz_buzz(n):
    for a in range(1, n):
        if (a % 3 == 0):
            print("Fizz")
        elif (a % 5 == 0):
            print("Buzz")
        elif (a % 5 == 0) and (a % 3 == 0):
            print("FizzBuzz")


n = int(input("Введите число: "))
fizz_buzz(n)
