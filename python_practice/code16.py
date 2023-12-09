class A:
    def __init__(self):
        self.num = 100

    def __del__(self):
        print(111111)

def Fun():
    x = A()

Fun()