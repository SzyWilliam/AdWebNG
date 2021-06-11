class A:
    def __init__(self):
        self.abc=["1"]
    def a(self):
        ab=self.abc
        ab.append("2")
        print(self.abc)

aaa=A()
aaa.a()