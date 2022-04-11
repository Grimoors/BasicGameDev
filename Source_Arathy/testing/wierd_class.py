class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class B(A):
    def __init__(self,):
        super().__init__(0, 3)


class C(B):
    def __init__(self, x, y):
        A.__init__(self, 10, 10)


c = C(20, 30)
