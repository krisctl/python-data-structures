from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def __len__(self):
        """Returns the length of the string"""

    @abstractmethod
    def __getitem__(self, index):
        """Gets a particular item"""

    def __contains__(self, s):
        for i in range(len(self)):
            if s == self[i]:
                return True
        return False

    def index(self, val):
        for i in range(len(self)):
            if val == self[i]:
                return i
        raise ValueError("value not in sequence")

    def count(self, v):
        counter: int = 0
        for i in range(len(self)):
            if v == self[i]:
                counter += 1
        return counter


class SubSequence(Sequence):
    def __init__(self) -> None:
        super().__init__()

    # Deliberately missing to implement abstract methods to see the behavior during init


if __name__ == "__main__":
    print("testing sequence")
    SubSequence()
