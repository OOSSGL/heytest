# Autor: Oscar Garcia


# Makes the triangle - Works for a n < 1000, TOO SLOW for anything major
def makePascalTriangle(n):
    trianone = [1]
    triantwo = [1, 1]

    notmodseven = 3

    # print(trianone)
    # print(triantwo)

    # Makes the pascal triangle =)
    for i in range(2, n):

        trianone = [1]
        for j in range(1, i):
            trianone.append(triantwo[j-1] + triantwo[j])

            # Sums the counter if each number is not divisible by 7
            if(trianone[-1] % 7 != 0):
                notmodseven += 1

        trianone.append(1)
        # We sum too the two 1's ate the sides that are not divisible  by 7
        notmodseven += 2

        # print(trianone)

        triantwo = trianone

    return notmodseven


# Makes the triangle of pascal but with ones and ceros depending if is divisible by 7 or not
# Makes beautiful images and pattern - Useless for the purpose of the program
# Makes a Serpinski triangle pattern
def makePascalBinary(n):
    trianone = [1]
    triantwo = [1, 1]

    notmodseven = 3

    makeBinary(trianone)
    makeBinary(triantwo)

    # Makes the pascal triangle =)
    for i in range(2, n):

        trianone = [1]
        for j in range(1, i):
            trianone.append(triantwo[j-1] + triantwo[j])

            # Sums the counter if each number is not divisible by 7
            if(trianone[-1] % 7 != 0):
                notmodseven += 1

        trianone.append(1)
        # We sum too the two 1's ate the sides that are not divisible  by 7
        notmodseven += 2

        makeBinary(trianone)

        triantwo = trianone

    return notmodseven


# Change the array from normal pascal to binary mod 7
def makeBinary(normal):
    binary = []
    for i in normal:
        if(i % 7 == 0):
            binary.append(1)
        else:
            binary.append(0)

    print(*binary)

    return binary


# Main
if __name__ == '__main__':
    # # Takes too long to execute
    # print(makePascalTriangle(1000)) 

    # Produces beautiful triangles and patterns but those patterns are like the serpinski
    # triangle, so is like a fractal, not an easy formula to get from these, time to read
    # more about it
    print(makePascalBinary(100))
    print("It terminated")

    # There has to be a mathematic formula for this problem

    """
    Found an article that says it has a formula for this problem:
    https://akira08280.com/euler148

    Supposedly the result is 118335, but it has really advanced mathematics elements that 
    i don't quiite understand and i don't know if that answer is corret

    """

    """
    I also found two articles whit the solution in another languages:

    http://cjordan.github.io/2013/12/29/solving-project-euler-148/
    This one in haskell

    https://euler.stephan-brumme.com/148/
    And this one in C++

    Althought they explain the code and how they get there (specially the haskell one)
    i still don't understand well why the use of base 7 and how this solves the problem.
    Both solutions get the result: 2129970655314432 
    So I guess that's the correct answer and the one from the formula is incorrect.

    Anyway I won't keep going with this exercise because translating it from any of 
    those two algorithms would not be an original answer, and also i don't understand 
    quite well how it works, I don't like to write code that i don't understand

    So this problem I will leave it there.

    """
