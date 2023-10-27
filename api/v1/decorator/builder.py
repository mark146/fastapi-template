class Builder:
    def __init__(self, cls):
        self.cls = cls
        self.kwargs = {}

    def __getattr__(self, key):
        def method(value):
            self.kwargs[key] = value
            return self
        return method

    def build(self):
        return self.cls(**self.kwargs)


def builder(cls):
    cls.builder = lambda: Builder(cls)
    return cls
