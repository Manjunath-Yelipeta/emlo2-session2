class Testclass:
    def __init__(self,foo,bar):
        self.foo = foo
        self.bar = bar
    
    def __repr__(self):
        return  repr(f"Testclass foo:{self.foo} and bar :{self.bar}")

def test_func(*args,**kwargs):
    print("args", args )
    print("kwargs",kwargs)
    return "something"