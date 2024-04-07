def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    total = 1

    for i in range(number):
        if i == 0:
            pass
        else:
            total = total * 2

    return total


def total():
    total = 0

    for i in range(64):
        total = total + square(i+1)

    return total

