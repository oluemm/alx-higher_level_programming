# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#This prevents the code from being executed at import time
# it only runs when the function is called from a script OR
# this file is ran directlyin terminal mode
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))