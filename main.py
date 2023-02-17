#1

def text():
    print(f"Don't compare yourself with anyone in this world...\n"
          f"if you do so, you are insulating yourself.\n"
          f"\t\t\t\t\t\t\t\t\t\tBill Gates")

text()

#2

def even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
even(1, 10)

#3

def square(length, symbol, logic = True):
    if logic:
        for i in range(length):
            print(f"{length * symbol}")
    else:
        print(f"{(length) * symbol}")
        for i in range(length):
            print(symbol + " " * (length - 2) + symbol)
        print(f"{length * symbol}")

square(4, "*", False)

#4

def find_min(*args):
    print(min(args))

find_min(100,200,300,400,500, -1100)

#5

def result(a, b, f = 1):
    if a > b:
        c = a
        a = b
        b = c
    while a <= b:
        a = a + 1
        f = f * a
    return f
print(result(1, 5))

#6

def count_numbers(a):
    a = str(a)
    print(len(str(a)))

count_numbers(111)


#7

def palindrome(a):
    a = str(a)
    if a == a[::-1]:
        return True
    else:
        return False
print(palindrome(123321))