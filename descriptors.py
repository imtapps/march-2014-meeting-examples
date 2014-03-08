class CharField(object):
    _field_count = 0

    def __init__(self, max_length=100):
        type(self)._field_count += 1
        self._field = type(self)._field_count
        self.max_length = max_length

    @property
    def field_name(self):
        return "_field_{}".format(self._field)

    def __get__(self, obj, typ):
        return getattr(obj, self.field_name)

    def __set__(self, obj, value):
        if len(value) > self.max_length:
            raise TypeError("{} > max length of {}".format(len(value), self.max_length))
        setattr(obj, self.field_name, value)


class MyObject(object):
    first_name = CharField(max_length=10)
    last_name = CharField(max_length=10)


my_object = MyObject()
my_object.first_name = "Matt"
my_object.last_name = "Morrison"

print my_object.first_name
print my_object.last_name

my_object.first_name = 'x' * 11
