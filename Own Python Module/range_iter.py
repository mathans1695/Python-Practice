class Separator:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


sen = Separator(1, 10)

for i in sen:
	print(i)