def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for the using this function")
    return mfx
@greet
def hello():
    print("hello world")

def add(a,b):
    print(a+b)

greet(add)(1,2)
hello()    