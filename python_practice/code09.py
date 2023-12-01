class Functor:
    def __init__(self, val):
        self.m_Val = val

    def __call__(self):
        return func(self.m_Val)

def func(num):
    return 2 * num

val = 100
x = Functor(val)
print(x())