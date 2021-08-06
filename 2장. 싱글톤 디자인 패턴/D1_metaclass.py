### Metaclass: class of class
###     One class is an instance of its metaclass

class MyInt(type):
    ### 이미 존재하는 클래스의 객체를 생성할 때 호출되는 특수 메소드
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)
