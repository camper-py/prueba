
def product(x, y):
    return x * y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

print("Input 2 numbers")
x = int(input())
y = int(input())
print("Input operation")
op = input()
if op == "*":
    print(product(x, y))

elif op == "+":
    print(add(x, y))

elif op == "-":
    print(subtract(x, y))

elif op == "/":
    print(divide(x, y))

else:
    print("Invalid operation")

print("Done")
