def maxNumber(listOfElems):

    listOfElems.sort()
    print(listOfElems)
    print("max number  " + str(listOfElems[-1]))


def main():
    listOfElems = [2, 3, 4, 1, 3, 4, 7, 10]
    maxNumber(listOfElems)


if __name__ == '__main__': main()