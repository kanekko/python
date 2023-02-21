def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


def fib(n) :
    if n==0 :
        return 0
    elif n ==1 :
        return 1
    else :
        return fib(n-1) +fib(n-2)

print(fib(7))


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


reverseme = 'Hola'
print(reverse(reverseme))

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(5))