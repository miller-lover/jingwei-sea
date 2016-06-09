class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''
    '''All three of these class methods, __init__, __iter__, and __next__, begin
     and end with a pair of underscore (_) characters. Why is that? There's
     nothing magical about it, but it usually indicates that these are "special
     methods." The only thing "special" about special methods is that they
     aren't called directly; Python calls them when you use some other syntax on
      the class or an instance of the class.'''

    def __init__(self, max):
        self.max = max

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

for n in Fib(1000):
    print(n, end=' ')
