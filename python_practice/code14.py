class Functor:
    def __init__(self, oA):
        self.m_Val = oA

    def __call__(self):
        return func(self.m_Val.self.m_Val)

def func(num):
    return 2 * num

class A:
    def __init__(self):
        self.m_Val = 100

val = 100
tmp = A
x = Functor(tmp)
print(x())