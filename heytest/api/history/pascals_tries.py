# Autor: Oscar Garcia


# Makes the triangle - Works for a n < 1000, TOO SLOW for anything major
def makePascalTriangle(n):
    trianone = [1]
    triantwo = [1, 1]

    notmodseven = 3

    #print(trianone)
    #print(triantwo)

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
