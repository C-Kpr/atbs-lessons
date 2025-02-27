def commaConcat(someList):
    newString = ''

    if len(someList) > 0:
        for i in range(0, len(someList)):
            if i < len(someList) - 2:
                newString += someList[i] + ', '
            elif i < len(someList) - 1:
                newString += someList[i] + ' and '
            else:
                newString += someList[i]
    else:
        newString = ''

    return newString

#spam = ['hi', 'test', 'banana', 'coffee', 'milk', 'oat']
spam = []
testString = commaConcat(spam)

print(testString)


