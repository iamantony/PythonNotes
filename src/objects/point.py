__author__ = 'Antony Cherepanov'

from exceptions import Exception
from math import fabs, pow, sqrt


class PointException(Exception):
    pass


class Point(object):
    """
    2D Point object
    """

    def __init__(self, t_x=0, t_y=0):
        self.__x = t_x
        self.__y = t_y

    def __str__(self):
        return "Point(" + str(self.__x) + ", " + str(self.__y) + ")"

    def __checkCoordType(self, t_coord):
        if isinstance(t_coord, (int, float, long)):
            return True
        return False

    def SetCoords(self, t_x, t_y):
        if not self.__checkCoordType(t_x) or not self.__checkCoordType(t_y):
            raise PointException("Invalid coordinate value type")

        self.__x = t_x
        self.__y = t_y

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    @staticmethod
    def distance(t_firstPoint, t_secondPoint):
        """
         Calculate euclidean distance between two points
         @input:
         - t_firstPoint - valid Point object
         - t_secondPoint - valid Point object
         @output:
         - value - distance between points

         Exception: PointException
        """

        if not isinstance(t_firstPoint, Point) or\
                not isinstance(t_secondPoint, Point):
            raise PointException("Invalid point objects")

        distX = fabs(t_firstPoint.GetX() - t_secondPoint.GetX())
        istXSq = pow(distX, 2)

        distY = fabs(t_firstPoint.GetY() - t_secondPoint.GetY())
        distYSq = pow(distY, 2)
        
        return sqrt(istXSq + distYSq)



