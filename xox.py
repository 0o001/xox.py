def xoxArray():
    x = 'x'
    o = 'o'

    xoxArray = [
        [x, x, x],
        [x, o, o],
        [o, x, x]
    ]

    return xoxArray

def xoxSolution(xoxArray):
    #Left to Right
    for index in xoxArray:
        if len(set(index)):
            return True

    #Up to Down
    for index in range(3):
        if xoxArray[0][index] == xoxArray[1][index] == xoxArray[2][index]:
            return True

    #Top-Left to Bottom-Right Cross
    if xoxArray[0][0] == xoxArray[1][1] == xoxArray[2][2]:
        return True

    #Top-Right to Bottom Cross
    if xoxArray[0][-1] == xoxArray[1][-2] == xoxArray[2][-3]:
        return True

    return False

print(xoxSolution(xoxArray()))
