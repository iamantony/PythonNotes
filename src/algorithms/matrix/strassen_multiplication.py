__author__ = 'Antony Cherepanov'

from matrix import Matrix, MatrixException


def Start():
    first = Matrix(4, 4, [i for i in range(1, 17)])
    second = Matrix(4, 4, [i for i in range(17, 33)])
    print "First = ", first
    print "Second = ", second
    print "Multiplication: ", first * second
    print "Strassen multiplication = ", StrassenMultiplication(first, second)


def StrassenMultiplication(t_first, t_second):
    # Work only with square Matrices of same even dimensions
    if not isinstance(t_first, Matrix) or not isinstance(t_second, Matrix) or \
            not t_first.IsSquare() or not t_second.IsSquare() or \
            t_first.rows() != t_second.rows():
        return None

    isPowerOf2 = t_first.rows() & (t_first.rows() - 1)
    if 0 != isPowerOf2:
        return None

    # Check if we work with smallest square matrices 4x4
    if 4 == t_first.rows():
        mA = t_first.GetSlice([0, 0], [1, 1])
        mB = t_first.GetSlice([0, 2], [1, 3])
        mC = t_first.GetSlice([2, 0], [3, 1])
        mD = t_first.GetSlice([2, 2], [3, 3])

        mE = t_second.GetSlice([0, 0], [1, 1])
        mF = t_second.GetSlice([0, 2], [1, 3])
        mG = t_second.GetSlice([2, 0], [3, 1])
        mH = t_second.GetSlice([2, 2], [3, 3])

        p1 = mA * (mF - mH)
        p2 = (mA + mB) * mH
        p3 = (mC + mD) * mE
        p4 = mD * (mG - mE)
        p5 = (mA + mD) * (mE + mH)
        p6 = (mB - mD) * (mG + mH)
        p7 = (mA - mC) * (mE + mF)

        resA = p5 + p4 - p2 + p6
        resB = p1 + p2
        resC = p3 + p4
        resD = p1 + p5 -p3 - p7

        result = Matrix(t_first.rows(), t_first.cols())
        result.SetSlice([0, 0], [1, 1], resA)
        result.SetSlice([0, 2], [1, 3], resB)
        result.SetSlice([2, 0], [3, 1], resC)
        result.SetSlice([2, 2], [3, 3], resD)

        return result


Start()
