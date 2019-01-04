def riffleShuffle(half1, half2, shuffledDeck):

    index1 = 0
    index2 = 0
    index1Max = len(half1) - 1
    index2Max = len(half2) - 2

    for card in shuffledDeck:

        if index1 < index1Max and card == half1[index1]:
            index1 += 1

        elif index2 < index2Max and card == half2[index2]:
            index2 += 1

        else:
            return False

    return True