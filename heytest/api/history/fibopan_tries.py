import math


# Autor: Oscar Garcia

# First try normal iteration - EXPONENTIAL SLOW
def fiboNormalIteration():
    n = 1
    m = 1
    k = 0
    print("Iteration", "Lenght", "Fibonacci")

    for i in range(3, 10000000):
      h = m
      m = m + n
      n = h

      first_numbers = str(m)[0:9]
      last_numbers = str(m)[-9:]

      """
      if(i == 541):
          print(first_numbers, last_numbers)
          print(i, len(str(m)), m, sep=": ")
      """
      """
      # Gets the ones that finish with a pan-digital sequence
      if('1' in last_numbers and '2' in last_numbers and '3' in last_numbers and '4' in last_numbers 
      and '5' in last_numbers and '6' in last_numbers and '7' in last_numbers and '8' in last_numbers 
      and '9' in last_numbers):
          print("\nLAST", i, len(str(m)), m, sep=": ")
          print("LAST", first_numbers, last_numbers)

      # Gets the ones that starts with a pan-digital sequence
      if('1' in first_numbers and '2' in first_numbers and '3' in first_numbers and '4' in first_numbers 
      and '5' in first_numbers and '6' in first_numbers and '7' in first_numbers and '8' in first_numbers 
      and '9' in first_numbers):
          print("\nFIRST", i, len(str(m)), m, sep=": ")
          print("FIRST", first_numbers, last_numbers)
      """
      if(i > 100000):
          # Get the ones that finish and start with a pan-digital sequence
          if('1' in last_numbers and '2' in last_numbers and '3' in last_numbers and '4' in last_numbers  
          and '5' in last_numbers and '6' in last_numbers and '7' in last_numbers and '8' in last_numbers 
          and '9' in last_numbers and '1' in first_numbers and '2' in first_numbers and '3' in first_numbers 
          and '4' in first_numbers and '5' in first_numbers and '6' in first_numbers and '7' in first_numbers 
          and '8' in first_numbers and '9' in first_numbers):
            print("\nSTART AND FINISH", i, len(str(m)), m, sep=": ")
            print("nSTART AND FINISH", first_numbers, last_numbers)
            k = i
            break

    print("\nIt terminated")
    print("K is: " + k)


# Check if is pan-digital - OLD DEPRECATED
def is_pandigital(number, iteration):
    first_numbers = str(number)[0:9]
    last_numbers = str(number)[-9:]

    """
    # Gets the ones that finish with a pan-digital sequence
    if('1' in last_numbers and '2' in last_numbers and '3' in last_numbers and '4' in last_numbers 
    and '5' in last_numbers and '6' in last_numbers and '7' in last_numbers and '8' in last_numbers 
    and '9' in last_numbers):
        print("\nLAST", iteration, len(str(number)), number, sep=": ")
        print("LAST", first_numbers, last_numbers)
        return True
    
    # Gets the ones that start with a pan-digital sequence
    if('1' in first_numbers and '2' in first_numbers and '3' in first_numbers and '4' in first_numbers 
    and '5' in first_numbers and '6' in first_numbers and '7' in first_numbers and '8' in first_numbers 
    and '9' in first_numbers):
        print("\nFIRST", iteration, len(str(number)), number, sep=": ")
        print("FIRST", first_numbers, last_numbers)
        return True
    """

    # Get the ones that finish AND start with a pan-digital sequence
    if('1' in last_numbers and '2' in last_numbers and '3' in last_numbers and '4' in last_numbers  
    and '5' in last_numbers and '6' in last_numbers and '7' in last_numbers and '8' in last_numbers 
    and '9' in last_numbers and '1' in first_numbers and '2' in first_numbers and '3' in first_numbers 
    and '4' in first_numbers and '5' in first_numbers and '6' in first_numbers and '7' in first_numbers 
    and '8' in first_numbers and '9' in first_numbers):
        print("\nSTART AND FINISH", iteration, len(str(number)), number, sep=": ")
        print("nSTART AND FINISH", first_numbers, last_numbers)
        return True


# A memoized solution - TOO SLOW
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


# A bottom-up solution - TOO SLOW
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        if(isPandigital(bottom_up[i], i) is True):
            return i
    return bottom_up[n]


# Generative - TOO SLOW
def fibGen(n):
    a, b = 0, 1
    while n>0:
        yield a
        a, b, n = b, a+b, n-1


# Call Generative - TOO SLOW
def callGenerative(n):
    i = 0
    for f in fibGen(n):
        #print(i, f)
        #if(is_pandigital(f, i) is True):
        #    return f
        i += 1
    return (i, f)


# Fast doubling Fibonacci algorithm - SUPER FAST BUT CAN'T CHECK EACH ITERATION
# SO IT IS USELESS FOR THIS TEST
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# Returns the tuple (F(n), F(n+1)). - SUPER FAST BUT CAN'T CHECK EACH ITERATION
# SO IT IS USELESS FOR THIS TEST
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b

        #print(a, b, c, d)

        if n % 2 == 0:
            print(c)
            return (c, d)
        else:
            print(d)
            return (d, c + d)


# Check if it is pandigital with sets
def isBothPandigital(number, iteration):
    first_numbers = set(str(number)[0:9])
    last_numbers = set(str(number)[-9:])

    """
    # Gets the ones that finish with a pan-digital sequence
    if(last_numbers == set("123456789")):
        print("\nLAST", iteration, len(str(number)), number, sep=": ")
        print("LAST", last_numbers)
        # return True
    """

    # Gets the ones that start with a pan-digital sequence
    if(first_numbers == set("123456789")):
        print("\nFIRST", iteration, len(str(number)), number, sep=": ")
        print("FIRST", first_numbers)
        # return True

    # Get the ones that finish AND start with a pan-digital sequence
    if(first_numbers == set("123456789") and last_numbers == set("123456789")):
        print("\nSTART AND FINISH", iteration, len(str(number)), number, sep=": ")
        print("nSTART AND FINISH", first_numbers, last_numbers)
        return True


# Using Golden ratio - IT WORKS! Founded! K is 329468!!!
def goldenRatio(n):
    golden_ratio = (1 + math.sqrt(5))/2
    start = 2
    m = 1
    l = 1
    for i in range(3, n):
        # Normal iteration of fibonacci
        h = m
        m = m + l
        l = h

        # start =  only the first numbers, we multiply it with the golden ratio to get an 
        # aproximation of the fibonacci number each iteration
        start = int(start * golden_ratio)

        # have to make it maximun 30 digits or else we will get overflow to infinite
        if(start>1E30):
            start = int(start*1E-3)
        
        # First we check if the first numbers are pandigital
        if(isPandigital(set(str(start)[0:9]))):
            #print("\nSTART", i, len(str(m)), m, sep=": ")
            #print("START", str(start)[0:9])
            
            # Second we check if the last numbers are pandigital, if they are we founded the number!
            if(isPandigital(set(str(m)[-9:]))):
                print("\nFINISH AND FINISH\nIteration  |  # of Digits  |  Full number\n", 
                    i, len(str(m)), m, sep=": ")
                print("START", str(start)[0:9], "FINISH", str(m)[-9:])
                return i

    


# Check if it is pandigital with sets simpler, had to use this one because in some cases the 30 digit
# golden number was pan-digital at the start and in the end, and stopped there we only need to found it 
# at the start so this simpler method had to be created
def isPandigital(number):
    if(number == set("123456789")):
        return True


# Main
if __name__ == '__main__':
    print("K = ", goldenRatio(1000000))
    #print(fib_bottom_up(3000))
    print("It terminated")

    # Founded! K is 329468!!!
    # The crucial thing was cheking firts with the golden ratio, that make even the normal iteration a lot
    # faster! I was not needed to make another algorithm just for the last numbers, although it would be
    # faster it would not show the full fibonacci number, this way is better but not totally efficient yet