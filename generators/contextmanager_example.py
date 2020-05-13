from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1

class Some_Obj(object):
    def __init__(self, arg):
        self.some_property = arg
