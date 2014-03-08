
class MyLogger(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print "Starting {} Context Manager".format(self.name)
        return self

    def __exit__(self, exception_type, exception, traceback):
        print "Ending {} Context Manager".format(self.name)
        if exception_type:
            print "Uh, oh, got an error:", exception

from contextlib import contextmanager


@contextmanager
def otherlogger(name):
    print "Starting {}".format(name)
    try:
        yield
    except Exception as e:
        print "Got Exception", e
    print "Ending {}".format(name)


# with MyLogger('something') as x:
#     print "I'm in here with {}".format(x.name)
#     raise Exception("WTF?")

with otherlogger('newone') as y:
    print "I'm in here"
    raise Exception("HI")
