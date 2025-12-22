from abc import ABC, abstractmethod
import math

class RoundPeg:

    def __init__(self, radius: int) -> None:
        self.rayon = radius

    def getRadius(self) -> int:
        return self.rayon

class SquarePeg:
    def __init__(self, width: int) -> None:
        self.width = width

    def getwidth(self) -> int:
        return self.width

class RoundHole:

    def __init__(self, radius: int) -> None:
        self.rayon = radius

    def getRadius(self) -> int:
        return self.rayon

    def fits(self, peg: RoundPeg) -> bool:
        return self.rayon >= peg.getRadius()





class SquarePegAdapter(RoundPeg):

    def __init__(self, peg: SquarePeg) -> None:
        self.__peg = peg

    def getRadius(self) -> int:
        return (self.__peg.getwidth()*math.sqrt(2))/2





if __name__ == "__main__":
    hole= RoundHole(5)
    rpeg= RoundPeg(5)

    print(hole.fits(rpeg))

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)

    # hole.fits(small_peg)
    # # AttributeError: 'SquarePeg' object has no attribute 'getRadius'

    small_peg_adapter= SquarePegAdapter(small_sqpeg)
    large_peg_adapter= SquarePegAdapter(large_sqpeg)
    print(hole.fits(small_peg_adapter))
    print(hole.fits(large_peg_adapter))