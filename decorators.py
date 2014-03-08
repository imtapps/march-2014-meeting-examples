python
from functools import wraps


def log(filename):

    def logwrapper(func):

        @wraps(func)
        def wrapper(*args):

            with open(filename, 'w') as f:
                print >> f, "'{}' called with {}".format(func.__name__, args)
                return_value = func(*args)
                print >> f, "'{}' returning '{}'".format(func.__name__, return_value)
                return return_value

        return wrapper

    return logwrapper


@log('main.log')
def main(arg1, arg2):
    print "In Main"
    return "In Func with {} and {}".format(arg1, arg2)


print "Before Calling"
print main
print main('A', 'B')
print "After Calling"
