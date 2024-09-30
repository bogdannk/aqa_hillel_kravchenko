"""Solution iterators"""
class MyIteranorForReverse:

    __data: list[int] = []

    def __init__(self, data):
        self.__data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration(f'Iteration was stopped because the last element was printed')
        self.index -= 1
        return self.__data[self.index]


for item in MyIteranorForReverse([1, 2, 3, 4, 5]):
    print(item)


class IteratorForEvenNumbers:

    __n: int = 0
    __current: int = 0

    def __init__(self, n):
        self.__n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < self.__n:
            result = self.__current
            self.__current += 2
            return result
        else:
            raise StopIteration(f"Itetation was stopped because the next expected element {self.__current} out of range.")


iterator = IteratorForEvenNumbers(13)
while True:
    try:
        print(next(iterator))
    except StopIteration as exeption:
        print(exeption)
        break









