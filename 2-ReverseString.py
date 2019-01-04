def reverseString(string):
    print(string[::-1])


def reverseStringAlt(string):
    string = list(string)
    indexLeft = 0
    indexRight = len(string)-1

    while indexLeft < indexRight:
        string[indexLeft], string[indexRight] = string[indexRight], string[indexLeft]
        indexLeft += 1
        indexRight -= 1

    return ''.join(string)


string1 = "Hello World"
reverseString(string1)
print(reverseStringAlt(string1))