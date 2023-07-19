import functools
import time


class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self

        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    """
    A lazy property decorator.

    The function decorated is called the first time to retrieve the result and
    then that calculated result is used the next time you access the value.
    """
    attr = "_lazy__" + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        time.sleep(3)
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    Jhon = Person("John", "Coder")

    print(Jhon.name)
    print(Jhon.occupation)

    # Before we access 'relatives'
    print(sorted(Jhon.__dict__.items()))

    print(Jhon.relatives)

    # After we access 'relatives'
    print(sorted(Jhon.__dict__.items()))

    print(Jhon.relatives)  # 이미 위에서 캐시해서 빠르게 호출

    print(Jhon.parents)

    print(sorted(Jhon.__dict__.items()))

    print(Jhon.parents)

    print(Jhon.call_count2)


if __name__ == "__main__":
    main()


"""
John
Coder
[('call_count2', 0), ('name', 'John'), ('occupation', 'Coder')]
Many relatives.
[('call_count2', 0), ('name', 'John'), ('occupation', 'Coder'), ('relatives', 'Many relatives.')]
Many relatives.
Father and mother
[('_lazy__parents', 'Father and mother'), ('call_count2', 1), ('name', 'John'), ('occupation', 'Coder'), ('relatives', 'Many relatives.')]
Father and mother
1
"""