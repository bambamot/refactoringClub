print("FizzBuzz for Refactoring Club by P'Yothin")

value = ""

for i in range(1, 100):
    
    if i % 3 == 0 and i % 5 == 0:
        value += "FizzBuzz "
    elif i % 3 == 0:
        value += "Fizz "
    elif i % 5 == 0:
        value += "Buzz "
    else:
        value += str(i) + " "
    if i % 10 == 0:
        value += "\n"

print(value)