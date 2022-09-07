def adding_decorator(func):

    def extra_features():
        print("EXTRA_FEATURES() HAS BEEN EXECUTED!")
        func()
        print("EXTRA FEATURES HAVE NBEEN ADDED TO THE FUNCTION PASSED AS ARGUMENT!")

    # Notice the previous function itself is returned, not the argument of return in that function (which would be called as "extra_features()")
    return extra_features

@adding_decorator
def hello():
    print("Hello world!")

# The line of code below is equivalent to put the @adding_decorator above the hello() definition
# hello = adding_decorator(hello)
hello()