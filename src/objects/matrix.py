__author__ = 'Antony Cherepanov'

from exceptions import Exception


class MatrixException(Exception):
    pass


class Matrix(object):
    def __init__(self, t_rowNum=0, t_colNum=0, t_values=None):
        if not self.__checkDimensionType(t_rowNum) or\
                not self.__checkDimensionType(t_colNum):
            raise MatrixException("Invalid number of matrix size")

        self.__rows = max(t_rowNum, 0)
        self.__cols = max(t_colNum, 0)

        numOfElements = self.__rows * self.__cols
        if t_values is None or \
                not isinstance(t_values, list) or \
                len(t_values) != numOfElements:
            self.__matrix = [0 for i in range(numOfElements)]
        else:
            self.__matrix = t_values

    def __checkDimensionType(self, t_dim):
        if isinstance(t_dim, int):
            return True
        return False

    def __str__(self):
        return "Matrix of " + str(self.__rows) + " rows and " +\
               str(self.__cols) + " cols: " + str(self.__matrix)

    def __add__(self, other):
        if not isinstance(other, Matrix) or \
                (self.__rows != other.rows() and self.__cols != other.cols()):
            raise MatrixException("Failed to add matrix")

        sumData = list()
        for i in range(self.__rows):
            for j in range(self.__cols):
                value = self.GetValue(i, j) + other.GetValue(i, j)
                sumData.append(value)

        result = Matrix(self.__rows, self.__cols, sumData)
        return result

    def __sub__(self, other):
        if not isinstance(other, Matrix) or \
                (self.__rows != other.rows() and self.__cols != other.cols()):
            raise MatrixException("Failed to subtract matrix")

        subData = list()
        for i in range(self.__rows):
            for j in range(self.__cols):
                value = self.GetValue(i, j) - other.GetValue(i, j)
                subData.append(value)

        result = Matrix(self.__rows, self.__cols, subData)
        return result

    def __mul__(self, other):
        if not isinstance(other, Matrix) or \
                self.__cols != other.rows():
            raise MatrixException("Failed to multiply matrix")

        mulData = list()
        # Iterate by elements of result matrix
        for i in range(self.__rows):
            for j in range(other.cols()):
                sumValue = 0
                for iter in range(self.__cols):
                    sumValue += self.GetValue(i, iter) * other.GetValue(iter, j)

                mulData.append(sumValue)

        result = Matrix(self.__rows, other.cols(), mulData)
        return result

    def rows(self):
        return self.__rows

    def cols(self):
        return self.__cols

    def IsSquare(self):
        if self.__cols == self.__rows:
            return True
        return False

    def __getIndex(self, t_row, t_col):
        if not self.__checkDimensionType(t_row) or\
                not self.__checkDimensionType(t_col):
            raise MatrixException("Invalid coordinates type")

        index = self.__cols * t_row + t_col
        if index < 0 or len(self.__matrix) <= index:
            return None
        return index

    def GetValue(self, t_row, t_col):
        index = self.__getIndex(t_row, t_col)
        if index is None:
            raise MatrixException("Invalid index")

        return self.__matrix[index]

    def SetValue(self, t_row, t_col, t_value):
        index = self.__getIndex(t_row, t_col)
        if index is None:
            raise MatrixException("Invalid index")

        self.__matrix[index] = t_value

    def GetSlice(self, t_topLeft, t_bottomRight):
        # TODO: Definitely there could be a better approach
        if 2 != len(t_topLeft) or 2 != len(t_bottomRight):
            raise MatrixException("Invalid slice coordinates")

        data = list()
        startI = t_topLeft[0]
        endI = t_bottomRight[0] + 1
        startJ = t_topLeft[1]
        endJ = t_bottomRight[1] + 1
        for i in range(startI, endI):
            for j in range(startJ, endJ):
                value = self.GetValue(i, j)
                data.append(value)

        result = Matrix(endI - startI, endJ - startJ, data)
        return result

    def SetSlice(self, t_topLeft, t_bottomRight, t_slice):
        if 2 != len(t_topLeft) or 2 != len(t_bottomRight) or \
                not isinstance(t_slice, Matrix):
            raise MatrixException("Invalid slice coordinates or slice matrix")

        startI = t_topLeft[0]
        endI = t_bottomRight[0] + 1
        startJ = t_topLeft[1]
        endJ = t_bottomRight[1] + 1

        if (endI - startI) != t_slice.cols() or\
                (endJ - startJ) != t_slice.rows():
            return False

        for i, slI in zip(range(startI, endI), range(t_slice.rows())):
            for j, slJ in zip(range(startJ, endJ), range(t_slice.cols())):
                value = t_slice.GetValue(slI, slJ)
                self.SetValue(i, j, value)

        return True