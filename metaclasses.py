python

import unittest

SCENARIOS = (
    (1, 1, 2),
    (2, 2, 4),
    (4, 4, 8),
    (8, 8, 16),
)

class AdditionMetaclass(type):

    def __new__(cls, name, bases, data):
        for a, b, c in SCENARIOS:
            data['test_{}_plus_{}_is_{}'.format(a, b, c)] = cls.create_test(a, b, c)
        return type(name, bases, data)

    @classmethod
    def create_test(cls, a, b, c):
        def stub(self):
            self.assertEqual(c, a + b)
        return stub


class SomeTests(unittest.TestCase):
    __metaclass__ = AdditionMetaclass



if __name__ == '__main__':
    unittest.main()
