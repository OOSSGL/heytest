import collections


# Autor: Oscar Garcia
# By doing it manually I found that the password is 73162890


# Main
if __name__ == '__main__':

    # Leemos el archivo y los pasamos a un array
    with open('keylog.txt') as f:
        array = []

        for line in f:
            array.append(line[0:3])

    #print(array)

    # Collection that will have all the digits of the password
    # A collection is used so we can put weights on them
    # UNUSED at the end i found a better way, just by sorting a normal array will work
    digitsh = {}

    # Normal array used, the index of the array will be the weight, and is sorted by 
    # swapping the two numbers each time they are in the wrong position
    digis = []

    # Get all the digits used
    for i in array:
        for j in i:

            # We start with putting erey character with a weight of 50
            if (j not in digitsh):
                digitsh[j] = 50
                digis.append(j)

    #print(digitsh)
    print(digis)

    # Compare the digits and put the digits in the correct order
    for i in array:
        # print(i[0], i[1], i[2])

        if(digis.index(i[0]) > digis.index(i[1])):
            digis[digis.index(i[0])] = i[1]
            digis[digis.index(i[1])] = i[0]

        if(digis.index(i[1]) > digis.index(i[2])):
            digis[digis.index(i[1])] = i[2]
            digis[digis.index(i[2])] = i[1]

        #print(i[0], digis.index(i[0]))

    print(digis)

    # wow it worked af first try! =D Normally you have to do this swaping a lot 
    # of times but the size of 50 samples was good enough, nice! I made it! =D
    # This one was a LOT easier than the fibonacci one xD

    password = ""
    for i in digis:
        password += i

    print(password)
