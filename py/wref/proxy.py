import weakref

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

obj = MyClass("example")
weak_proxy = weakref.proxy(obj)

print(weak_proxy.name)
print(weak_proxy.greet())

del obj
try:
    print(weak_proxy.name)
except ReferenceError as e:
    print(e)
