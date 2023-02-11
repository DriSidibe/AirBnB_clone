class Test:
    def say_hi(self):
        print("hi")

test = Test()

fun = getattr(test, "say_hi")

fun()
