class Progression:
    def __init__(self, start=0) -> None:
        self.current = start

    def _advance(self):
        self.current += 1

    def __next__(self):
        # Iterator implementation
        if self.current is None:
            raise StopIteration("end of sequence")

        current_ans = self.current
        self._advance()
        return current_ans

    def __iter__(self):
        return self

    def _print_progression(self, n):
        if n < 1:
            raise ValueError("n is less than 1")
        counter = 1
        for counter in range(n):
            print(self.__next__())


class ArithmeticProgression(Progression):
    # Needs to provide and override start and _advance(). Also, need to supply increment
    def __init__(self, start=0, inc=4) -> None:
        super().__init__(start)
        self.increment = inc

    def _advance(self):
        self.current += self.increment


class GeometricProgression(Progression):
    # Needs to provide and override start and _advance(). Also, need to supply increment
    def __init__(self, start=1, base=2) -> None:
        self.base = base
        super().__init__(start)

    def _advance(self):
        self.current *= self.base


class FibonacciProgression(Progression):
    # Needs to provide and override start and _advance(). Also, need to supply increment
    def __init__(self, start=0, second=1) -> None:
        self.second = second
        super().__init__(start)

    def _advance(self):
        temp = self.current  # 4
        self.current = self.second  # 6
        self.second += temp  # 10


if __name__ == "__main__":
    print("FibonacciProgression")
    FibonacciProgression(start=4, second=6)._print_progression(2)

    print("Arithmetic progression")
    ArithmeticProgression()._print_progression(2)

    print("Geometric Progression:")
    GeometricProgression(start=3, base=2)._print_progression(n=3)
