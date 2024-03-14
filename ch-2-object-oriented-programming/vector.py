class Vector:
    def __init__(self, d) -> None:
        self.__coords = [] * d

    def len(self) -> int:
        return len(self.__coords)

    def __get_item__(self, j):
        return self.__coords[j]

    def __set_item__(self, j, val):
        self.__coords[j] = val

    def add(self, other):
        """Return sum of two vectors"""
        if len(self.__coords) != len(other.__coords):
            raise ValueError("dimensions must agree!")
        else:
            result = Vector(len(self))
            for i in range(len(self.__coords)):
                result.__set_item__(i, self.__get_item__(i) + other.__get_item__(i))
                return result

    def __eq__(self, other: object) -> bool:
        if len(self.__coords) != len(other.__coords):
            return False
        else:
            return self.__coords == other.__coords

    def __ne__(self, other: object) -> bool:
        return self.__coords != other.__coords

    def __str__(self) -> str:
        return f"<{str(self.__coords[1:-1])}>"
