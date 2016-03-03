__author__ = 'Antony Cherepanov'


def Start():
    input = [4, 2, 8, 5, 3, 1, 6, 7]
    # input = [6, 5, 4, 3, 2, 1]
    # input = [1, 3, 5, 2, 4, 6]
    print "input =", input
    sortedInput, inversionsNum = InversionsCounter(input)
    print "number of inversions =", inversionsNum


# The main idea: use Merge Sort algorithm
def InversionsCounter(t_input):
    length = len(t_input)
    if 2 < length:
        halfLength = length / 2
        leftHalf = t_input[:halfLength]
        rightHalf = t_input[halfLength:]
        sortedLeft, leftInvNum = InversionsCounter(leftHalf)
        sortedRight, rightInvNum = InversionsCounter(rightHalf)

        i = 0
        maxI = len(sortedLeft)
        j = 0
        maxJ = len(sortedRight)
        sortedArray = list()
        inversionsNum = leftInvNum + rightInvNum
        for k in range(length):
            if maxI <= i:
                sortedArray.extend(sortedRight[j:])
                break

            if maxJ <= j:
                sortedArray.extend(sortedLeft[i:])
                break

            if sortedLeft[i] < sortedRight[j]:
                # that is ok, no inversion
                sortedArray.append(sortedLeft[i])
                i += 1
            else:
                sortedArray.append(sortedRight[j])
                j += 1
                # number of inversion = number of elements in the sorted left
                # half of the input array (in this case sortedLeft) that
                # we don't iterate yet (max number of elements - number of
                # current position)
                inversionsNum += maxI - i

        return sortedArray, inversionsNum

    else:
        if 1 == length:
            # no inversion in array that have only one number
            return t_input, 0
        elif 2 == length:
            sortedArray = t_input
            inversionsNum = 0
            first = t_input[0]
            second = t_input[1]
            if second < first:
                # if first number greater than the second, than there is
                # inversion!
                sortedArray = [second, first]
                inversionsNum = 1
            return sortedArray, inversionsNum


Start()
