class FibonacciGenerator:
    def __init__(self):
        self.prev = 0
        self.cur = 1

    def __next__(self):
        res = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        return res

    def __iter__(self):
        return self

for i in FibonacciGenerator():
    print(i)
    if i > 100:
        break

print("*" * 50)
def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

fib = fibonacci()
print(next(fib))
print(next(fib))

for num, fib in enumerate(fibonacci()):
    print('{0}: {1}'.format(num, fib))
    if num > 9:
        break
